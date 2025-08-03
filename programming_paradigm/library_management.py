
class Book:
    """Represents a book in the library."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Cannot check out an already checked-out book

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Returning a book that's already available

    def is_available(self):
        """Return True if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """Manages a collection of Book objects."""
    
    def __init__(self):
        self._books = []  # private 

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False  

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False  # Book not found or was never checked out

    def list_available_books(self):
        """Print all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
