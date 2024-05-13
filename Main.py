from Book import Book
from Library import Library
from Reader import Reader


def main():
    library = Library()

    library.add_book(Book("1984", "George Orwell", 328, "9780451524935"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 281, "9780446310789"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 180, "9780743273565"))
    library.add_book(Book("Pride and Prejudice", "Jane Austen", 432, "9781503290563"))
    library.add_book(Book("Brave New World", "Aldous Huxley", 288, "9780060850524"))
    library.add_book(Book("Moby Dick", "Herman Melville", 720, "9781503280786"))
    library.add_book(Book("War and Peace", "Leo Tolstoy", 1225, "9781420951083"))
    library.add_book(Book("Crime and Punishment", "Fyodor Dostoevsky", 671, "9780486415871"))
    library.add_book(Book("The Catcher in the Rye", "J.D. Salinger", 277, "9780316769488"))
    library.add_book(Book("The Hobbit", "J.R.R. Tolkien", 310, "9780345339683"))
    library.add_book(Book("The Lord of the Rings", "J.R.R. Tolkien", 1178, "9780544003415"))
    library.add_book(Book("The Brothers Karamazov", "Fyodor Dostoevsky", 796, "9780374528379"))
    library.add_book(Book("Ulysses", "James Joyce", 730, "9781840226355"))
    library.add_book(Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez", 417, "9780060883287"))
    library.add_book(Book("The Divine Comedy", "Dante Alighieri", 798, "9780142437223"))

    library.add_reader(Reader(1, "John", "Doe", "123 Main St", "555-1234"))
    library.add_reader(Reader(2, "Jane", "Doe", "124 Main St", "555-5678"))

    library.add_reservation(1, "1984", "George Orwell")
    library.add_reservation(2, "To Kill a Mockingbird", "Harper Lee")
    library.borrow_book(1, "9780743273565")

    while True:
        print("\nAvailable commands:")
        print("ADD BOOK - Add a new book to the library")
        print("EDIT BOOK - Edit a book's details")
        print("REMOVE BOOK - Remove a book from the library")
        print("FIND BOOK - Find a book by title from the library")
        print("ADD READER - Add a new reader to the library")
        print("REMOVE READER - Remove a reader from the library")
        print("EDIT READER - Edit a reader's details")
        print("BORROW BOOK - Borrow a book")
        print("RETURN BOOK - Return a book")
        print("DISPLAY BOOKS - Display all books")
        print("DISPLAY READERS - Display all readers")
        print("DISPLAY BORROWED BOOKS - Display all borrowed books")
        print("RESERVE BOOK - Reserve a book")
        print("CANCEL RESERVATION - Cancel a book reservation")
        print("DISPLAY HISTORY - Display reader history")
        print("CHECK EXPIRY - Check the expire date")
        print("EXIT - Exit the program")

        command = input("Enter command: ").strip().upper()

        if command == "ADD BOOK":
            title = input("Enter title: ")
            author = input("Enter author: ")
            pages = int(input("Enter number of pages: "))
            isbn = input("Enter ISBN: ")
            library.add_book(Book(title, author, pages, isbn))

        elif command == "EDIT BOOK":
            isbn = input("Enter ISBN of the book to edit: ")
            title = input("Enter new title (or leave blank for no change): ")
            author = input("Enter new author (or leave blank for no change): ")
            pages = input("Enter new number of pages (or leave blank for no change): ")
            pages = int(pages) if pages else None
            library.edit_book(isbn, title, author, pages)

        elif command == "REMOVE BOOK":
            isbn = input("Enter ISBN of the book to remove: ")
            library.remove_book(isbn)

        elif command == "ADD READER":
            reader_id = int(input("Enter reader ID: "))
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            address = input("Enter address: ")
            phone_number = input("Enter phone number: ")
            library.add_reader(Reader(reader_id, first_name, last_name, address, phone_number))

        elif command == "FIND BOOK":
            title = input("Enter title: ")
            library.find_book_by_title(title)

        elif command == "EDIT READER":
            reader_id = int(input("Enter reader ID: "))
            first_name = input("Enter new first name: ")
            last_name = input("Enter new last name: ")
            address = input("Enter new address: ")
            phone_number = input("Enter new phone number: ")
            library.edit_reader(reader_id, first_name, last_name, address, phone_number)

        elif command == "REMOVE READER":
            reader_id = int(input("Enter reader ID to remove: "))
            library.remove_reader(reader_id)

        elif command == "BORROW BOOK":
            library.check_reservations_expiry()
            reader_id = int(input("Enter reader ID: "))
            isbn = input("Enter ISBN of the book to borrow: ")
            library.borrow_book(reader_id, isbn)

        elif command == "RETURN BOOK":
            reader_id = int(input("Enter reader ID: "))
            isbn = input("Enter ISBN of the book to return: ")
            library.return_book(reader_id, isbn)

        elif command == "DISPLAY BOOKS":
            library.display_books()

        elif command == "DISPLAY READERS":
            library.display_readers()

        elif command == "DISPLAY BORROWED BOOKS":
            library.display_borrowed_books()

        elif command == "RESERVE BOOK":
            reader_id = int(input("Enter your reader ID: "))
            title = input("Enter the title of the book to reserve: ")
            author = input("Enter the author of the book: ")
            library.add_reservation(reader_id, title, author)

        elif command == "CANCEL RESERVATION":
            reader_id = int(input("Enter your reader ID: "))
            title = input("Enter the title of the book to cancel reservation: ")
            author = input("Enter the author of the book: ")
            library.cancel_reservation(reader_id, title, author)

        elif command == "CHECK EXPIRY":
            library.check_reservations_expiry()

        elif command == "DISPLAY HISTORY":
            reader_id = int(input("Enter reader ID: "))
            reader = library.find_reader_by_id(reader_id)
            if reader:
                reader.display_activity_history()
            else:
                print("Reader not found.")

        elif command == "EXIT":
            print("Exiting program.")
            break
        else:
            print("Invalid command, please try again.")


if __name__ == "__main__":
    main()
