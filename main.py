from book import Book
from librarian import Librarian
from library import Library
from member import Member
from person import Person
from student import Student
from teacher import Teacher


if __name__ == "__main__":

    print("\n" + "=" * 60)
    print("  LIBRARY MANAGEMENT SYSTEM")
    print("=" * 60)

    # 1. Create a library
    print("\n[ SETTING UP LIBRARY ]")

    library = Library("City Central Library", "Bengaluru")

    # 2. Add a librarian
    print("\n[ ADDING LIBRARIAN ]")

    librarian = Librarian(
        name="Ananya Rao",
        age=35,
        contact="9876543210",
        employee_role="Senior Librarian"
    )

    library.add_librarian(librarian)

    # 3. Add books
    print("\n[ ADDING BOOKS ]")

    book1 = Book(
        "Python Crash Course",
        "Eric Matthes",
        "Programming",
        2019,
        3
    )

    book2 = Book(
        "Clean Code",
        "Robert C. Martin",
        "Software Engineering",
        2008,
        2
    )

    book3 = Book(
        "Learning Python",
        "Mark Lutz",
        "Programming",
        2013,
        2
    )

    librarian.add_book(library, book1)
    librarian.add_book(library, book2)
    librarian.add_book(library, book3)

    # 4. Register members
    print("\n[ REGISTERING MEMBERS ]")

    member1 = Student(
        "Vibhu Kumar", 22, "9000000001", "B.Tech CSE"
    )

    member2 = Student(
        "Riya Sharma", 24, "9000000002", "B.Tech ECE"
    )

    student1 = Student(
        "Aman Verma", 20, "9000000003", "B.Tech IT"
    )

    teacher1 = Teacher(
        "Meera Singh", 38, "9000000004", "Computer Science"
    )

    librarian.register_member(library, member1)
    librarian.register_member(library, member2)
    librarian.register_member(library, student1)
    librarian.register_member(library, teacher1)

    # 5. Demonstrate magic methods
    print("\n[ MAGIC METHODS DEMO ]")

    print(f"  str(book1) -> {book1}")
    print(f"  repr(book1) -> {repr(book1)}")
    print(f"  len(library) -> {len(library)} titles")
    print(f"  len(member1) -> {len(member1)} borrowed books")

    print(f"  book1 in library -> {book1 in library}")
    print(f"  member1 in library -> {member1 in library}")

    # 6. Search for books
    print("\n[ SEARCHING CATALOGUE ]")

    for book in library.search_books("python"):
        print(f"  Found: {book}")

    # 7. Borrow books
    print("\n[ CHECKING OUT BOOKS ]")

    library.checkout_book(
        member1.member_id, book1.book_id, borrow_days=14
    )

    library.checkout_book(
        member1.member_id, book2.book_id, borrow_days=7
    )

    library.checkout_book(
        member2.member_id, book1.book_id, borrow_days=14
    )

    # 8. Demonstrate abstraction and polymorphism
    print("\n[ ABSTRACTION AND POLYMORPHISM ]")

    entities = [
        book1,
        book2,
        book3,
        member1,
        student1,
        teacher1,
        librarian
    ]

    for entity in entities:
        entity.introduce()

    # 9. Return a book
    print("\n[ RETURNING A BOOK ]")

    library.return_book(
        member1.member_id, book1.book_id
    )

    # 10. Demonstrate encapsulation and validation
    print("\n[ ENCAPSULATION DEMO ]")

    print(f"  Member contact: {member1.contact}")

    try:
        member1.age = 200

    except ValueError as error:
        print(f"  Validation error: {error}")

    try:
        _ = member1.__borrowed_books

    except AttributeError:
        print(
            "  Private borrowed-loan list cannot "
            "be accessed directly."
        )

    # 11. Demonstrate class variables
    print("\n[ CLASS VARIABLES DEMO ]")

    print(f"  Library name: {Person.library_name}")

    print(
        f"  Total registered people: "
        f"{Person.get_total_persons()}"
    )

    print(
        f"  Total libraries created: "
        f"{Library.get_total_libraries()}"
    )

    # 12. Generate the library report
    print("\n[ FULL LIBRARY REPORT ]")

    library.generate_report()

    print("\n[ PROGRAM FINISHED ]")