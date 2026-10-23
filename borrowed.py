from datetime import date, timedelta

class Borrowed:
    """Tracks a book checkout, due date, return date, and fine."""

    _borrowed_counter = 0
    fine_per_day = 5.0

    def __init__(self, member, book , borrow_days=14):
        if not isinstance(borrow_days, int) or borrow_days <= 0:
            raise ValueError("Loan period must be a positive integer.")

        Borrowed._borrowed_counter += 1
        self.__borrow_id = f"LOAN-{4000+Borrowed._borrowed_counter}"
        self.member = member
        self.book = book
        self.checkout_date = date.today()
        self.due_date = self.checkout_date + timedelta(days=borrow_days)
        self.return_date = None

    @property
    def borrow_id (self):
        return self.__borrow_id 

    @property
    def is_returned(self):
        return self.return_date is not None

    def calculate_fine(self, on_date=None):
        check_date = self.return_date or on_date or date.today()
        overdue_days = max((check_date - self.due_date).days, 0)
        return overdue_days * self.fine_per_day

    def mark_returned(self):
        self.return_date = date.today()

    def __str__(self):
        status = "Returned" if self.is_returned else "Borrowed"
        return (
            f"{self.__borrow_id }: '{self.book.title}' by {self.member.name} | "
            f"Due: {self.due_date} | {status}"
        )

    def __repr__(self):
        return (
            f"Loan(id='{self.__borrow_id }', member='{self.member.name}', "
            f"book='{self.book.title}')"
        )

