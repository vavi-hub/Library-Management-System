from person import Person
from book import Book
from library import Library
from member import Member


class Librarian(Person):
    """Staff member responsible for library operations."""

    _librarian_counter = 0

    def __init__(self, name, age, contact, employee_role="Librarian"):
        super().__init__(name, age, contact)
        Librarian._librarian_counter += 1
        self.__employee_id = f"STAFF-{3000+Librarian._librarian_counter}"
        self._employee_role = employee_role

    @property
    def employee_id(self):
        return self.__employee_id

    def add_book(self, library:Library, book:Book):
        library.add_book(book)

    def register_member(self, library:Library, member:Member):
        library.register_member(member)

    def get_role(self) -> str:
        return "Librarian"

    def get_details(self) -> str:
        return (
            f"Name: {self.name}, "
            f"Age: {self._age}, "
            f"Employee Role: {self._employee_role}"
        )