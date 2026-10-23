from libraryEntity import LibraryEntity
from datetime import date

class Person(LibraryEntity):
    """Abstract intermediate class for people in the Library."""
    library_name = "ACTE General Library"
    _total_persons = 0

    def __init__(self, name: str, age: int, contact: str):
            if not name or not name.strip():
                raise ValueError("Name cannot be empty")
            if not Person.is_valid_age(age):
                raise ValueError(f"Invalid age: {age}. Must be 1–120.")
            if not Person.is_valid_contact(contact):
                raise ValueError("Contact must be 10 digits")
    
            self._name = name.strip().title()
            self._age = age
            self.__contact = contact
            self._joined = date.today()
    
            Person._total_persons += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be blank")
        self._name = value.strip()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not Person.is_valid_age(value):
            raise ValueError(f"Invalid age: {value}")
        self._age = value

    @property
    def contact(self):
        return self.__contact

    @contact.setter
    def contact(self, value):
        if not Person.is_valid_contact(value):
            raise ValueError("Contact must be 10 digits")
        self.__contact = value

    @classmethod
    def get_total_persons(cls):
        """Return the Total number of registered people."""
        return cls._total_persons

    @classmethod
    def get_library_name(cls):
        """Return the Library Name"""
        return cls.library_name

    @classmethod
    def set_library_name(cls, name):
        """Change the library name system-wide."""
        if not name or not name.strip():
            raise ValueError("Name cannot be blank")
        cls.library_name=name

    @staticmethod
    def is_valid_age(age):
        """Check whether an age is an integer between 1 and 120."""
        return isinstance(age, int) and 1 <= age <= 120

    @staticmethod
    def is_valid_contact(contact):
        """Check whether a contact number contains exactly 10 digits."""
        return isinstance(contact, str) and contact.isdigit() and len(contact) == 10

    def __str__(self):
        return f"{self._name} (Age: {self._age}) — {self.library_name}"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(name='{self._name}', age={self._age})"
        )

    def __eq__(self, other):
        """Compare people by name, age, and contact."""
        if not isinstance(other, Person):
            return False
        return (
            self._name == other._name
            and self._age == other._age
            and self.__contact == other.contact
        )