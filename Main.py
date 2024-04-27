from Book import Book
from Library import Library
from Reader import Reader


def main():

    library = Library()

    library.add_book(Book("1984", "George Orwell", 328, "978-0451524935"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 281, "978-0446310789"))

    library.add_reader(Reader(1, "John", "Doe", "123 Main St", "555-1234"))
    library.add_reader(Reader(2, "Jane", "Doe", "124 Main St", "555-5678"))

    library.display_readers()

    library.borrow_book(1, "978-0451524935")
    library.return_book(1, "978-0451524935")
    library.display_books()
    library.display_readers()

if __name__ == "__main__":
    main()
