# Library Management System

This is a simple library management system implemented in Python using Object-Oriented Programming (OOP) concepts. The system allows you to manage books, borrowers, and borrowing/returning of books.

## Features

### Book Management
- Add new books to the library database with details like title, author, ISBN, genre, and quantity.
- Update existing book information (e.g., title, author, quantity) if needed.
- Remove books from the library database when they are no longer available.

### Borrower Management
- Add new borrowers to the library system, including information like name, contact details, and membership ID.
- Update borrower information when required (e.g., contact details).
- Remove borrowers from the system if necessary.

### Book Borrowing and Returning
- Allow borrowers to borrow books by linking the borrower's membership ID to the book details.
- Record the due date for each borrowed book and handle overdue books.
- Implement a mechanism for borrowers to return books, updating the database accordingly.

### Book Search and Availability
- Provide a search feature that enables users to find books by title, author, or genre.
- Show the availability status (number of copies available) for each book in the search results.

## Example Usage

Here is an example of how to use the library management system:

```python
library = Library()

# Adding books
book1 = Book("1984", "John Steinbeck", "1234567890", "Dystopian", 3)
book2 = Book("Frankenstein", "Mary Shelley", "1234567891", "Fiction", 2)

library.add_book(book1)
library.add_book(book2)

# Adding borrowers
borrower1 = Borrower("Spongebob", "spongebob@example.com", "MEM001")
borrower2 = Borrower("Patrick", "patrick@example.com", "MEM002")

library.add_borrower(borrower1)
library.add_borrower(borrower2)

# Borrowing a book
library.borrow_book("1234567890", "MEM001", "2024-07-01")

# Returning a book
library.return_book("1234567890", "MEM001")

# Searching for books
search_results = library.search_books(title="1984")
for book in search_results:
    print(book)

# Checking availability
availability = library.check_availability("1234567890")
print(f"Copies available: {availability}")

