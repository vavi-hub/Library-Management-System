from person import Person
from book import Book
from borrowed import Borrowed

class Member(Person):
    """A registered library member who can borrow books."""
    _member_counter = 0
    maxBooks = 3

    def __init__(self, name: str, age: int, contact: str):
        super().__init__(name, age, contact)
        Member._member_counter += 1
        self._member_id = f"MEM-{2000 + Member._member_counter}"
        self._borrowed_books = []
        self._borrowed_history=[]
        self._is_active = True

    @property
    def member_id(self):
        return self._member_id

    @property
    def get_borrowed_books(self):
        return self._borrowed_books.copy()

    @property
    def is_active(self):
        return self._is_active

    def borrow_book(self, book : Book , loan_days=14 ):
        if not self._is_active:
            print(f"  Membership inactive for {self.name}.")
            return None
        if len(self._borrowed_books) >= self.maxBooks:
            print(f"  Borrowing limit reached for {self.name}.")
            return None
        if any(borrowed.book is book for borrowed in self._borrowed_books):
            print(f"  {self.name} already borrowed '{book.title}'.")
            return None
        if not book.borrow_copy():
            print(f"  No copies available for '{book.title}'.")
            return None

        borrowed = Borrowed(self, book, loan_days)
        self._borrowed_books.append(borrowed)
        self._borrowed_history.append(borrowed)
        print(f"{self.name} borrowed '{book.title}'. Due: {borrowed.due_date}")
        return borrowed

    def return_book(self, book : Book):
        for borrowed in self._borrowed_books:
            if borrowed.book is book:
                self._borrowed_books.remove(borrowed)
                book.return_copy()
                borrowed.mark_returned()
                fine = borrowed.calculate_fine()
                print(f"{self.name} returned '{book.title}'.")
                print(f"  Overdue fine: ₹{fine:.2f}" if fine else "  No overdue fine.")
                return fine

        print(f"  {self.name} has not borrowed '{book.title}'.")
        return None

    def deactivate(self):
        self._is_active = False
        print(f"  Membership deactivated for {self.name}.")


    def __len__(self):
        return len(self._borrowed_books)