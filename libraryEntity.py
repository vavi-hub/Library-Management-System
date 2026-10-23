from abc import ABC, abstractmethod


class LibraryEntity(ABC):
    """Abstract base class for library entities."""

    @abstractmethod
    def get_role(self) -> str:
        pass

    @abstractmethod
    def get_details(self) -> str:
        pass

    def introduce(self):
        print(f"[{self.get_role()}] {self.get_details()}")