from datetime import datetime, timedelta

from Loan import Loan


class Reader:
    def __init__(self, reader_id, first_name, last_name, address, phone_number):
        self.reader_id = reader_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.activity_history = []

    def record_activity(self, book, activity_type, fee=0, date=None):
        if not date:
            date = datetime.now()
        activity = {
            "date": date,
            "book": book.title,
            "type": activity_type,
            "fee": fee
        }
        self.activity_history.append(activity)
        print(f"Activity recorded: {book.title} - {activity_type}, Fee: {fee:.2f}")

    def borrow_book(self, book):
        if not book.is_borrowed and not book.is_reserved:
            book.is_borrowed = True
            new_loan = Loan(book, self)
            self.activity_history.append({
                "date": new_loan.loan_date,
                "book": book.title,
                "type": "Borrowed",
                "loan": new_loan
            })
            print(f"{book.title} has been borrowed by {self.first_name} {self.last_name}.")
        else:
            print(f"Cannot borrow {book.title}, it is already borrowed or reserved.")

    def update_reader_details(self, first_name=None, last_name=None, address=None, phone_number=None):
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if address is not None:
            self.address = address
        if phone_number is not None:
            self.phone_number = phone_number

    def reserve_book(self, book):
        if not book.is_borrowed and not book.is_reserved:
            book.is_reserved = True
            book.reservation_expiry = datetime.now() + timedelta(days=7)
            self.record_activity(book, "Reserved")
            print(f"{book.title} has been reserved by {self.first_name} {self.last_name}.")
        else:
            print(f"Cannot reserve {book.title}, it is already borrowed or reserved.")

    def display_activity_history(self):
        if not self.activity_history:
            print("No activities recorded.")
            return

        print(f"Activity History for {self.first_name} {self.last_name}:")
        for activity in self.activity_history:
            date_str = activity['date'].strftime('%Y-%m-%d %H:%M:%S')
            print(f"{date_str} - {activity['book']}: {activity['type']} (Fee: {activity['fee']:.2f} zł)")

    def __str__(self):
        return f"Reader {self.reader_id}: {self.first_name} {self.last_name}, Phone: {self.phone_number}, Address: {self.address}"