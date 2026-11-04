CREATE DATABASE library_management;

USE library_management;

CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    member_code VARCHAR(20) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    age INT,
    contact VARCHAR(15),
    email VARCHAR(100) UNIQUE,
    member_type ENUM('Student', 'Teacher') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CHECK (age IS NULL OR age > 0)
);


CREATE TABLE librarians (
    librarian_id INT AUTO_INCREMENT PRIMARY KEY,
    librarian_code VARCHAR(20) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    contact VARCHAR(15),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    book_code VARCHAR(20) NOT NULL UNIQUE,
    title VARCHAR(150) NOT NULL,
    category_id INT,
    publication_year YEAR,

    FOREIGN KEY (category_id)
        REFERENCES categories(category_id)
);

CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(100) NOT NULL
);



CREATE TABLE book_authors (
    book_id INT NOT NULL,
    author_id INT NOT NULL,

    PRIMARY KEY (book_id, author_id),

    FOREIGN KEY (book_id)
        REFERENCES books(book_id),

    FOREIGN KEY (author_id)
        REFERENCES authors(author_id)
);


CREATE TABLE book_copies (
    copy_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    barcode VARCHAR(30) NOT NULL UNIQUE,

    copy_status ENUM(
        'Available',
        'Unavailable'
    ) DEFAULT 'Available',

    FOREIGN KEY (book_id)
        REFERENCES books(book_id)
);

CREATE TABLE borrowings (
    borrowing_id INT AUTO_INCREMENT PRIMARY KEY,

    member_id INT NOT NULL,
    copy_id INT NOT NULL,
    librarian_id INT,

    checkout_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE DEFAULT NULL,

    FOREIGN KEY (member_id)
        REFERENCES members(member_id),

    FOREIGN KEY (copy_id)
        REFERENCES book_copies(copy_id),

    FOREIGN KEY (librarian_id)
        REFERENCES librarians(librarian_id),

    CHECK (due_date >= checkout_date),

    CHECK (
        return_date IS NULL
        OR return_date >= checkout_date
    )
);


CREATE TABLE fines (
    fine_id INT AUTO_INCREMENT PRIMARY KEY,

    borrowing_id INT NOT NULL UNIQUE,
    fine_amount DECIMAL(10,2) NOT NULL DEFAULT 0.00,

    payment_status ENUM(
        'Pending',
        'Paid'
    ) DEFAULT 'Pending',

    FOREIGN KEY (borrowing_id)
        REFERENCES borrowings(borrowing_id),

    CHECK (fine_amount >= 0)
);


CREATE INDEX idx_book_title
ON books(title);

CREATE INDEX idx_book_category
ON books(category_id);

CREATE INDEX idx_member_name
ON members(name);

CREATE INDEX idx_member_type
ON members(member_type);

CREATE INDEX idx_author_name
ON authors(author_name);

CREATE INDEX idx_copy_book
ON book_copies(book_id);

CREATE INDEX idx_copy_status
ON book_copies(copy_status);

CREATE INDEX idx_borrowing_member
ON borrowings(member_id);

CREATE INDEX idx_borrowing_copy
ON borrowings(copy_id);

CREATE INDEX idx_borrowing_due_date
ON borrowings(due_date);

CREATE INDEX idx_borrowing_return_date
ON borrowings(return_date);



-- =========================================
-- 1. CATEGORIES
-- =========================================

INSERT INTO categories (category_id, category_name)
VALUES
(1, 'Programming'),
(2, 'Database'),
(3, 'Software Engineering'),
(4, 'Algorithms'),
(5, 'Computer Networks');


-- =========================================
-- 2. AUTHORS
-- =========================================

INSERT INTO authors (author_id, author_name)
VALUES
(1, 'Mark Lutz'),
(2, 'Robert C. Martin'),
(3, 'Abraham Silberschatz'),
(4, 'Thomas H. Cormen'),
(5, 'Brian W. Kernighan'),
(6, 'Andrew S. Tanenbaum'),
(7, 'Martin Fowler'),
(8, 'Eric Matthes'),
(9, 'Donald E. Knuth'),
(10, 'Kurose and Ross');


-- =========================================
-- 3. BOOKS
-- =========================================

INSERT INTO books
(book_id, book_code, title, category_id, publication_year)
VALUES
(1, 'BOOK-1001', 'Learning Python', 1, 2022),
(2, 'BOOK-1002', 'Clean Code', 3, 2008),
(3, 'BOOK-1003', 'Database System Concepts', 2, 2020),
(4, 'BOOK-1004', 'Introduction to Algorithms', 4, 2022),
(5, 'BOOK-1005', 'The C Programming Language', 1, 1988),
(6, 'BOOK-1006', 'Computer Networks', 5, 2021),
(7, 'BOOK-1007', 'Refactoring', 3, 2018),
(8, 'BOOK-1008', 'Python Crash Course', 1, 2023),
(9, 'BOOK-1009', 'The Art of Computer Programming', 4, 2011),
(10, 'BOOK-1010', 'Computer Networking: A Top-Down Approach', 5, 2021);


-- =========================================
-- 4. BOOK AUTHORS
-- =========================================

INSERT INTO book_authors (book_id, author_id)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);


-- =========================================
-- 5. BOOK COPIES
-- =========================================

INSERT INTO book_copies
(copy_id, book_id, barcode, copy_status)
VALUES
(1, 1, 'COPY-0001', 'Available'),
(2, 1, 'COPY-0002', 'Unavailable'),
(3, 2, 'COPY-0003', 'Available'),
(4, 2, 'COPY-0004', 'Available'),
(5, 3, 'COPY-0005', 'Unavailable'),
(6, 3, 'COPY-0006', 'Available'),
(7, 4, 'COPY-0007', 'Available'),
(8, 5, 'COPY-0008', 'Available'),
(9, 6, 'COPY-0009', 'Unavailable'),
(10, 7, 'COPY-0010', 'Available'),
(11, 8, 'COPY-0011', 'Available'),
(12, 9, 'COPY-0012', 'Available'),
(13, 10, 'COPY-0013', 'Available'),
(14, 10, 'COPY-0014', 'Available'),
(15, 10, 'COPY-0015', 'Available');


-- =========================================
-- 6. MEMBERS
-- =========================================

INSERT INTO members
(member_id, member_code, name, age, contact, email, member_type)
VALUES
(1, 'MEM-2001', 'Rahul Kumar', 22, '9876543210', 'rahul@gmail.com', 'Student'),
(2, 'MEM-2002', 'Amit Sharma', 35, '9876543211', 'amit@gmail.com', 'Teacher'),
(3, 'MEM-2003', 'Priya Singh', 21, '9876543212', 'priya@gmail.com', 'Student'),
(4, 'MEM-2004', 'Neha Verma', 23, '9876543213', 'neha@gmail.com', 'Student'),
(5, 'MEM-2005', 'Rohit Gupta', 32, '9876543214', 'rohit@gmail.com', 'Teacher'),
(6, 'MEM-2006', 'Anjali Mishra', 20, '9876543215', 'anjali@gmail.com', 'Student'),
(7, 'MEM-2007', 'Vikash Kumar', 24, '9876543216', 'vikash@gmail.com', 'Student'),
(8, 'MEM-2008', 'Sneha Patel', 29, '9876543217', 'sneha@gmail.com', 'Teacher');


-- =========================================
-- 7. LIBRARIANS
-- =========================================

INSERT INTO librarians
(librarian_id, librarian_code, name, contact, email)
VALUES
(1, 'LIB-3001', 'Suresh Kumar', '9988776655', 'suresh@library.com'),
(2, 'LIB-3002', 'Pooja Sharma', '9988776656', 'pooja@library.com'),
(3, 'LIB-3003', 'Ankit Verma', '9988776657', 'ankit@library.com');


-- =========================================
-- 8. BORROWINGS
-- =========================================

INSERT INTO borrowings
(borrowing_id, member_id, copy_id, librarian_id,
 checkout_date, due_date, return_date)
VALUES

(1, 1, 1, 1, '2026-09-01', '2026-09-15', '2026-09-12'),

(2, 2, 2, 1, '2026-10-01', '2026-10-15', NULL),

(3, 3, 3, 2, '2026-09-10', '2026-09-20', '2026-09-25'),

(4, 4, 4, 2, '2026-10-01', '2026-10-15', '2026-10-10'),

(5, 5, 5, 3, '2026-10-20', '2026-11-02', NULL),

(6, 6, 6, 1, '2026-09-15', '2026-09-30', '2026-09-28'),

(7, 7, 7, 2, '2026-10-05', '2026-10-20', '2026-10-18'),

(8, 8, 8, 3, '2026-10-10', '2026-10-25', '2026-10-22'),

(9, 1, 9, 1, '2026-10-30', '2026-11-13', NULL),

(10, 3, 10, 2, '2026-10-15', '2026-10-30', '2026-10-29');


-- =========================================
-- 9. FINES
-- =========================================

INSERT INTO fines
(fine_id, borrowing_id, fine_amount, payment_status)
VALUES
(1, 2, 50.00, 'Pending'),
(2, 3, 30.00, 'Paid'),
(3, 5, 20.00, 'Pending');


-- =========================================
-- 10. VERIFY ALL TABLES
-- =========================================

SELECT 'Members' AS table_name, COUNT(*) AS total FROM members
UNION ALL
SELECT 'Librarians', COUNT(*) FROM librarians
UNION ALL
SELECT 'Categories', COUNT(*) FROM categories
UNION ALL
SELECT 'Books', COUNT(*) FROM books
UNION ALL
SELECT 'Authors', COUNT(*) FROM authors
UNION ALL
SELECT 'Book Authors', COUNT(*) FROM book_authors
UNION ALL
SELECT 'Book Copies', COUNT(*) FROM book_copies
UNION ALL
SELECT 'Borrowings', COUNT(*) FROM borrowings
UNION ALL
SELECT 'Fines', COUNT(*) FROM fines;


-- =========================================
-- 11. DISPLAY BOOK DETAILS
-- =========================================

SELECT
    b.book_code,
    b.title,
    a.author_name,
    c.category_name,
    bc.barcode,
    bc.copy_status
FROM books b
JOIN book_authors ba ON b.book_id = ba.book_id
JOIN authors a ON ba.author_id = a.author_id
JOIN categories c ON b.category_id = c.category_id
JOIN book_copies bc ON b.book_id = bc.book_id
ORDER BY b.book_id;


-- =========================================
-- 12. DISPLAY BORROWING HISTORY
-- =========================================

SELECT
    br.borrowing_id,
    m.name AS member_name,
    b.title AS book_title,
    bc.barcode,
    br.checkout_date,
    br.due_date,
    br.return_date,
    CASE
        WHEN br.return_date IS NOT NULL THEN 'Returned'
        WHEN br.due_date < CURDATE() THEN 'Overdue'
        ELSE 'Borrowed'
    END AS borrowing_status
FROM borrowings br
JOIN members m ON br.member_id = m.member_id
JOIN book_copies bc ON br.copy_id = bc.copy_id
JOIN books b ON bc.book_id = b.book_id;


-- =========================================
-- 13. DISPLAY FINE DETAILS
-- =========================================

SELECT
    f.fine_id,
    m.name AS member_name,
    b.title AS book_title,
    f.fine_amount,
    f.payment_status
FROM fines f
JOIN borrowings br ON f.borrowing_id = br.borrowing_id
JOIN members m ON br.member_id = m.member_id
JOIN book_copies bc ON br.copy_id = bc.copy_id
JOIN books b ON bc.book_id = b.book_id;
