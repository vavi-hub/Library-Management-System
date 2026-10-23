from person import Person
from book import Book
from member import Member
from borrowed import Borrowed


class Library:
    """Main class that manages books, members, staff, and borrows."""

    _total_libraries = 0
    _all_libraries = []

    def __init__(self, name, city):
        if not name or not name.strip():
            raise ValueError("Library name cannot be empty.")

        Library._total_libraries += 1
        self.__library_id = f"LIBRARY-{Library._total_libraries:03d}"
        self.__name = name.strip()
        self.__city = city.strip()
        self.__catalogue = {}
        self.__members = {}
        self.__librarians = []
        self.__borrow = []

        Person.set_library_name(f"{self.__name}, {self.__city}")
        Library._all_libraries.append(self)

        print(f"Library '{self.__name}' opened in {self.__city}.")

    @property
    def library_id(self):
        return self.__library_id

    @classmethod
    def get_total_libraries(cls):
        return cls._total_libraries

    @classmethod
    def find_library(cls, library_id):
        return next(
            (lib for lib in cls._all_libraries
             if lib.__library_id == library_id),
            None
        )

    @staticmethod
    def report_header(title):
        line = "=" * 60
        return f"\n{line}\n  {title}\n{line}"

    def add_book(self, book):
        if book.book_id in self.__catalogue:
            print(f"  Book {book.book_id} already exists.")
            return False

        self.__catalogue[book.book_id] = book
        print(f"  Added: {book}")
        return True

    def register_member(self, member):
        if member.member_id in self.__members:
            print(f"  Member {member.member_id} already registered.")
            return False

        self.__members[member.member_id] = member
        print(f"  Registered: {member.name} ({member.member_id})")
        return True

    def add_librarian(self, librarian):
        if librarian not in self.__librarians:
            self.__librarians.append(librarian)
            print(f"  Librarian added: {librarian.name}")

    def find_book(self, book_id):
        return self.__catalogue.get(book_id)

    def find_member(self, member_id):
        return self.__members.get(member_id)

    def search_books(self, query):
        query = query.casefold().strip()

        return [
            book for book in self.__catalogue.values()
            if query in book.title.casefold()
            or query in book.author.casefold()
        ]

    def checkout_book(self, member_id, book_id, borrow_days=14):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member is None:
            print(f"  Member not found: {member_id}")
            return None

        if book is None:
            print(f"  Book not found: {book_id}")
            return None

        borrow = member.borrow_book(book, borrow_days)

        if borrow is not None:
            self.__borrow.append(borrow)

        return borrow

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member is None:
            print(f"  Member not found: {member_id}")
            return None

        if book is None:
            print(f"  Book not found: {book_id}")
            return None

        return member.return_book(book)

    def generate_report(self):
        print(
            self.report_header(
                f"LIBRARY REPORT — {self.__name}, {self.__city}"
            )
        )

        print(f"\nBOOK CATALOGUE ({len(self.__catalogue)} titles):")

        for book in self.__catalogue.values():
            book.introduce()

        print(f"\nREGISTERED MEMBERS ({len(self.__members)}):")

        for member in self.__members.values():
            member.introduce()
            print(f"  Books currently borrowed: {len(member)}")

        print(f"\nLIBRARY STAFF ({len(self.__librarians)}):")

        for librarian in self.__librarians:
            librarian.introduce()

        print(f"\nBORROW HISTORY ({len(self.__borrow)} transactions):")

        for borrow in self.__borrow:
            print(f"  {borrow}")

        print(f"\nTotal registered people: {Person.get_total_persons()}")
        print("=" * 60)

    def __len__(self):
        return len(self.__catalogue)

    def __contains__(self, item):
        if isinstance(item, Book):
            return item.book_id in self.__catalogue

        if isinstance(item, Member):
            return item.member_id in self.__members

        return False

    def __str__(self):
        return f"{self.__name}, {self.__city} ({len(self)} book titles)"

    def __repr__(self):
        return (
            f"Library(id='{self.__library_id}', "
            f"name='{self.__name}')"
        )