class Book:
    def __init__(self, title, author, pages, isbn=None):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_borrowed = False

    def update_book_details(self, title=None, author=None, pages=None, isbn=None):
        print("Updating details of the book.")
        if title:
            self.title = title
        if author:
            self.author = author
        if pages:
            self.pages = pages
        if isbn:
            self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages, ISBN: {self.isbn if self.isbn else 'Not available'}, {'Borrowed' if self.is_borrowed else 'Available'}"
