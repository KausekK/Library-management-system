from datetime import datetime


class Loan:
    def __init__(self, book, reader):
        self.book = book
        self.reader = reader
        self.base_fee = 0
        self.daily_late_fee = 1
        self.late_days = 0
        self.loan_date = datetime.now()

    def add_late_days(self, days):
        self.late_days += days

    def calculate_fee(self):
        return self.base_fee + (self.late_days * self.daily_late_fee)

    def __str__(self):
        return f"Loan: {self.book.title} to {self.reader.first_name} {self.reader.last_name}, Base Fee: {self.base_fee}, Daily Late Fee: {self.daily_late_fee}, Late Days: {self.late_days}"