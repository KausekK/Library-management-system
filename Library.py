from datetime import datetime

from Loan import Loan


class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.books.append(book)
        print("Added new book to the library.")

    def remove_book(self, isbn):
        book_to_remove = next((book for book in self.books if book.isbn == isbn), None)
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f"Removed {book_to_remove.title} from the library.")
        else:
            print("Book not found.")

    def edit_book(self, isbn, title=None, author=None, pages=None):
        book_to_edit = next((book for book in self.books if book.isbn == isbn), None)
        if book_to_edit:
            book_to_edit.update_book_details(title=title, author=author, pages=pages)
            print(f"Updated book details: {book_to_edit}")
        else:
            print("Book not found.")

    def display_books(self):
        if self.books:
            print("Library Catalog:")
            for book in self.books:
                print(book)
        else:
            print("No books available in the library.")

    def display_borrowed_books(self):
        counter = 0
        print("Library Borrowed Books:")
        for book in self.books:
            if book.is_borrowed:
                counter += 1
                print(book)
        if counter == 0:
            print("No books currently borrowed.")

    def find_book_by_title(self, title):
        found_books = [book for book in self.books if book.title == title]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("No books found with that title.")

    def add_reader(self, reader):
        existing_reader = self.find_reader_by_id(reader.reader_id)
        if existing_reader is None:
            self.readers.append(reader)
            print("Added new reader to the library.")
        else:
            print(f"Reader with ID {reader.reader_id} already exists and cannot be added.")

    def find_reader_by_id(self, reader_id):
        for reader in self.readers:
            if reader.reader_id == reader_id:
                return reader
        return None

    def remove_reader(self, reader_id):
        reader_to_remove = next((reader for reader in self.readers if reader.reader_id == reader_id), None)
        if reader_to_remove:
            self.readers.remove(reader_to_remove)
            print(f"Removed reader {reader_to_remove.first_name} {reader_to_remove.last_name} from the library.")
        else:
            print("Reader not found.")

    def edit_reader(self, reader_id, first_name=None, last_name=None, address=None, phone_number=None):
        reader_to_edit = next((reader for reader in self.readers if reader.reader_id == reader_id), None)
        if reader_to_edit:
            reader_to_edit.update_reader_details(first_name=first_name, last_name=last_name, address=address,
                                                 phone_number=phone_number)
            print(f"Updated reader details: {reader_to_edit}")
        else:
            print("Reader not found.")

    def borrow_book(self, reader_id, isbn):
        reader = next((r for r in self.readers if r.reader_id == reader_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if book and reader:
            if not book.is_borrowed and not book.is_reserved:
                book.is_borrowed = True
                reader.record_activity(book, "Borrowed")
                print(f"Book {book.title} has been borrowed by {reader.first_name} {reader.last_name}.")
            elif book.is_reserved:
                print(f"Book {book.title} is currently reserved and cannot be borrowed.")
            else:
                print(f"Book {book.title} is already borrowed.")
        else:
            print("Book or reader not found.")

    def return_book(self, reader_id, book_isbn):
        reader = next((r for r in self.readers if r.reader_id == reader_id), None)
        book = next((b for b in self.books if b.isbn == book_isbn), None)
        if reader and book:
            if book.is_borrowed:
                loan_record = next((item for item in reader.activity_history if
                                    item.get('book') == book.title and item.get('type') == 'Borrowed' and item.get(
                                        'date') and
                                    'return_date' not in item), None)

                if loan_record:
                    loan = loan_record.get('loan', None)
                    if not loan:
                        loan = Loan(book, reader)
                        loan.loan_date = loan_record['date']

                    loan.return_date = datetime.now()
                    fee = loan.calculate_fee()
                    loan_record['return_date'] = loan.return_date

                    reader.record_activity(book, "Returned", fee)
                    book.is_borrowed = False
                    print(f"{book.title} has been returned by {reader.first_name} {reader.last_name}. Fee: {fee:.2f}")
                else:
                    print(f"Could not find loan record for {book.title}.")
            else:
                print(f"This book was not borrowed by this reader or it has already been returned.")
        else:
            print("Book or reader not found.")

    def display_readers(self):
        if self.readers:
            print("List of Readers:")
            for reader in self.readers:
                print(reader)
        else:
            print("No readers registered in the library.")

    def add_reservation(self, reader_id, title, author):
        reader = next((r for r in self.readers if r.reader_id == reader_id), None)
        book = next((b for b in self.books if b.title == title and b.author == author), None)
        if book and reader:
            if not book.is_borrowed and not book.is_reserved:
                reader.reserve_book(book)
            else:
                print(f"Book {title} by {author} is already borrowed or reserved.")
        else:
            print("Book or reader not found.")

    def cancel_reservation(self, reader_id, title, author):
        book = next((b for b in self.books if b.title == title and b.author == author and b.is_reserved), None)
        reader = next((r for r in self.readers if r.reader_id == reader_id), None)
        if book and reader:
            book.release_reservation()
            reader.record_activity(book,"Reservation Cancelled")
        else:
            print("No reservation found for cancellation or reader not found.")

    def check_reservations_expiry(self):
        has_reserved_books = False
        for book in self.books:
            if book.is_reserved:
                has_reserved_books = True
                reservation_expiry = book.reservation_expiry.strftime('%Y-%m-%d %H:%M')
                if book.reservation_expiry < datetime.now():
                    book.check_reservation_expiry()
                    print(f"Reservation for '{book.title}' has expired and has been cancelled.")
                else:
                    print(f"Reservation for '{book.title}' is still active, expires on {reservation_expiry}.")
        if not has_reserved_books:
            print("There are no reserved books to check.")

