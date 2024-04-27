class Reader:
    def __init__(self, reader_id, first_name, last_name, address, phone_number):
        self.reader_id = reader_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.borrowing_history = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowing_history.append((book, "Borrowed"))
            print(f"{book.title} has been borrowed by {self.first_name} {self.last_name}.")
        else:
            print(f"Cannot borrow the book as it is already borrowed.")

    def return_book(self, book):
        if book.is_borrowed:
            book.is_borrowed = False
            self.borrowing_history.append((book, "Returned"))
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

    def __str__(self):
        return f"Reader {self.reader_id}: {self.first_name} {self.last_name}, Phone: {self.phone_number}, Address: {self.address}"
