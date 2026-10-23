from libraryEntity import LibraryEntity

class Book(LibraryEntity):
    """A physical book in the library catalogue."""

    _book_counter = 0

    def __init__(
        self, title: str, author: str, genre: str,
        publication_year: int, copies: int = 1
    ):
        if not title or not title.strip():
            raise ValueError("Book title cannot be empty.")
        if not author or not author.strip():
            raise ValueError("Author cannot be empty.")
        if not isinstance(copies, int) or copies < 0:
            raise ValueError("Copies must be a non-negative integer.")

        Book._book_counter += 1
        self.__book_id = f"BOOK-{1000+Book._book_counter}"
        self._title = title.strip()
        self._author = author.strip()
        self._genre = genre.strip()
        self._publication_year = publication_year
        self._total_copies = copies
        self._available_copies = copies

    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author

    @property
    def genre(self):
        return self._genre

    @property
    def total_copies(self):
        return self._total_copies

    @property
    def available_copies(self):
        return self._available_copies

    def borrow_copy(self):
        if self._available_copies == 0:
            return False
        self._available_copies -= 1
        return True

    def return_copy(self):
        if self._available_copies >= self._total_copies:
            return False
        self._available_copies += 1
        return True

    def get_role(self):
        return "Book"

    def get_details(self):
        return (
            f"{self._title} by {self._author} | Genre: {self._genre} | "
            f"Available: {self._available_copies}/{self._total_copies}"
        )

    def __str__(self):
        return (
            f"{self.__book_id}: {self._title} by {self._author} "
            f"({self._available_copies} available)"
        )

    def __repr__(self):
        return (
            f"Book(id='{self.__book_id}', title='{self._title}', "
            f"author='{self._author}')"
        )

