from datetime import datetime


class Loan:
    def __init__(self, book, reader, loan_type="Borrowed"):
        self.book = book
        self.reader = reader
        self.loan_type = loan_type
        self.loan_date = datetime.now()
        self.return_date = None
        self.base_fee = 0
        self.daily_late_fee = 0.5
        self.late_days = 0

    def calculate_fee(self):
        if not self.return_date:
            return 0
        total_seconds_late = (self.return_date - self.loan_date).total_seconds() - 5
        periods_late = max(0, int(total_seconds_late // 5))
        return self.base_fee + periods_late * self.daily_late_fee

    def __str__(self):
        return_date_str = self.return_date.strftime('%Y-%m-%d') if self.return_date else "Not returned"
        return f"{self.loan_type}: {self.book.title} (Loan Date: {self.loan_date.strftime('%Y-%m-%d')}, Return Date: {return_date_str})"
