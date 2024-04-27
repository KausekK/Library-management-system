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

    def find_book_by_title(self, title):
        found_books = [book for book in self.books if book.title == title]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("No books found with that title.")

    def add_reader(self, reader):
        self.readers.append(reader)
        print("Added new reader to the library.")

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
            reader_to_edit.update_reader_details(first_name=first_name, last_name=last_name, address=address, phone_number=phone_number)
            print(f"Updated reader details: {reader_to_edit}")
        else:
            print("Reader not found.")

    def borrow_book(self, reader_id, book_isbn):
        reader = next((r for r in self.readers if r.reader_id == reader_id), None)
        book = next((b for b in self.books if b.isbn == book_isbn and not b.is_borrowed), None)
        if reader and book:
            reader.borrow_book(book)
        else:
            print("Book is not available for borrowing or reader not found.")

    def return_book(self, reader_id, book_isbn):
        reader = next((r for r in self.readers if r.reader_id == reader_id), None)
        book = next((b for b in self.books if b.isbn == book_isbn), None)
        if reader and book:
            reader.return_book(book)
        else:
            print("Book or reader not found.")

    def display_readers(self):
        if self.readers:
            print("List of Readers:")
            for reader in self.readers:
                print(reader)
        else:
            print("No readers registered in the library.")