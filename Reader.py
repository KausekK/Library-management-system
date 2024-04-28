from datetime import datetime, timedelta

from Loan import Loan


class Reader:
    def __init__(self, reader_id, first_name, last_name, address, phone_number):
        self.reader_id = reader_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.borrowing_history = []

    def record_activity(self, book, activity_type, date=None):
        if not date:
            date = datetime.now()
        self.borrowing_history.append((date, book.title, activity_type))

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            new_loan = Loan(book, self)
            # self.borrowing_history.append(new_loan)
            self.record_activity(book, "Borrowed")
            print(f"{book.title} has been borrowed by {self.first_name} {self.last_name}.")
        else:
            print(f"Cannot borrow the book as it is already borrowed.")

    def return_book(self, book):
        if book.is_borrowed:
            book.is_borrowed = False
           # self.borrowing_history.append((book, "Returned"))
            print(f"{book.title} has been returned by {self.first_name} {self.last_name}.")
        else:
            print(f"This book was not borrowed by this reader or it has already been returned.")

    def update_reader_details(self, first_name=None, last_name=None, address=None, phone_number=None):
        print("Updating reader details.")
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if address:
            self.address = address
        if phone_number:
            self.phone_number = phone_number

    def calculate_total_fees(self):
        total_fees = 0
        for loan in self.borrowing_history:
            if loan.return_date:
                total_fees += loan.calculate_fee()
        return total_fees

    def reserve_book(self, book):
        if not book.is_borrowed and not book.is_reserved:
            book.is_reserved = True
            book.reservation_expiry = datetime.now() + timedelta(days=7)
            self.record_activity(book, "Reserved")
            print(f"{book.title} has been reserved by {self.first_name} {self.last_name}.")
        else:
            print(f"Cannot reserve {book.title}, it is already borrowed or reserved.")

    def display_activity_history(self):
        if not self.borrowing_history:
            print("No activities recorded.")
            return

        print(f"Activity History for {self.first_name} {self.last_name}:")
        for entry in self.borrowing_history:
            date, title, activity_type = entry
            print(f"{date.strftime('%Y-%m-%d')} - {title}: {activity_type}")

    def __str__(self):
        return f"Reader {self.reader_id}: {self.first_name} {self.last_name}, Phone: {self.phone_number}, Address: {self.address}"