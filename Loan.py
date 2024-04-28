from datetime import datetime


class Loan:
    def __init__(self, book, reader, loan_type="Borrowed"):
        self.book = book
        self.reader = reader
        self.loan_type = loan_type  # Typ operacji
        self.loan_date = datetime.now()
        self.return_date = None
        self.base_fee = 0
        self.daily_late_fee = 0.5
        self.late_days = 0

    def calculate_fee(self):
        if not self.return_date:
            return 0
        late_days = max(0, (self.return_date - self.loan_date).days - 14)  # Załóżmy 14 dni bez opłaty
        return self.base_fee + late_days * self.daily_late_fee

    def __str__(self):
        return_date_str = self.return_date.strftime('%Y-%m-%d') if self.return_date else "Not returned"
        return f"{self.loan_type}: {self.book.title} (Loan Date: {self.loan_date.strftime('%Y-%m-%d')}, Return Date: {return_date_str})"
