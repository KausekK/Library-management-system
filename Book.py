from datetime import datetime, timedelta


class Book:
    def __init__(self, title, author, pages, isbn=None):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_borrowed = False
        self.is_reserved = False
        self.reservation_expiry = None

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
        status = "Available"
        if self.is_borrowed:
            status = "Borrowed"
        elif self.is_reserved:
            status = f"Reserved until {self.reservation_expiry.strftime('%Y-%m-%d %H:%M')}"
        return f"{self.title} by {self.author}, {self.pages} pages, ISBN: {self.isbn if self.isbn else 'Not available'}, Status: {status}"

    def reserve_book(self):
        if not self.is_borrowed and not self.is_reserved:
            self.is_reserved = True
            self.reservation_expiry = datetime.now() + timedelta(days=7)
            print(f"Book '{self.title}' has been reserved. It must be picked up within 7 days.")
        else:
            print(f"Cannot reserve '{self.title}', it is already reserved or borrowed.")

    def release_reservation(self):
        if self.is_reserved:
            self.is_reserved = False
            self.reservation_expiry = None
            print(f"Reservation for '{self.title}' has been cancelled.")
        else:
            print(f"No reservation found for '{self.title}'.")

    def check_reservation_expiry(self):
        if self.is_reserved and self.reservation_expiry < datetime.now():
            self.is_reserved = False
            self.reservation_expiry = None
            print(f"Reservation for '{self.title}' has expired and has been cancelled.")