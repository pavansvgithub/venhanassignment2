class Book:
    def __init__(self,title,author,isbn,genre,quantity):
        self.title = title 
        self.author = author 
        self.isbn = isbn 
        self.genre = genre 
        self.quantity = quantity 
    def update_quantity(self,quantity):
        self.quantity = quantity 
    def update_details(self,title=None,author=None,genre=None,quantity=None):
        if title:
            self.title = title 
        if author:
            self.author = author 
        if genre:
            self.genre = genre 
        if quantity is not None:
            self.quantity = quantity 
class Borrower:
    def __init__(self,name,contact_details,membership_id):
        self.name = name 
        self.contact_details = contact_details 
        self.membership_id = membership_id 
    def update_contact_details(self,contact_details):
        self.contact_details = contact_details 

class Library:
    def __init__(self):
        self.books = {} 
        self.borrowers = {} 
        self.borrowed_books = {} 
    def add_book(self,book):
        self.books[book.isbn] = book 
    def update_book(self,isbn,title=None,author=None,genre=None,quantity=None):
        if isbn in self.books:
            self.books[isbn].update_details(title,author,genre,quantity) 
    def remove_book(self,isbn):
        del self.books[isbn]
    def add_borrower(self, borrower):
        self.borrowers[borrower.membership_id] = borrower
    
    def update_borrower(self, membership_id, contact_details):
        if membership_id in self.borrowers:
            self.borrowers[membership_id].update_contact_details(contact_details)
    
    def remove_borrower(self, membership_id):
        if membership_id in self.borrowers:
            del self.borrowers[membership_id]
    
    def borrow_book(self, isbn, membership_id, due_date):
        if isbn in self.books and membership_id in self.borrowers:
            if self.books[isbn].quantity > 0:
                self.books[isbn].quantity -= 1
                self.borrowed_books[(isbn, membership_id)] = due_date
                print(f"Book borrowed: {self.books[isbn].title}")
            else:
                print(f"Book '{self.books[isbn].title}' is out of stock.")
        else:
            print("Invalid book ISBN or membership ID.")
    
    def return_book(self, isbn, membership_id):
        if (isbn, membership_id) in self.borrowed_books:
            self.books[isbn].quantity += 1
            del self.borrowed_books[(isbn, membership_id)]
            print(f"Book returned: {self.books[isbn].title}")
        else:
            print("Invalid return. This book was not borrowed by this member.")
    
    def search_books(self, title=None, author=None, genre=None):
        results = []
        for book in self.books.values():
            if (title and title.lower() in book.title.lower()) or \
               (author and author.lower() in book.author.lower()) or \
               (genre and genre.lower() in book.genre.lower()):
                results.append(book)
        return results
    
    def check_availability(self, isbn):
        if isbn in self.books:
            return self.books[isbn].quantity
        return 0

# Example usage:

library = Library()

# Adding books
book1 = Book("2024", "John Steinbeck", "1234567890", "Dystopian", 4)
book2 = Book("Frankenstein", "Mary Shelley", "1234567891", "Fiction", 3)

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


