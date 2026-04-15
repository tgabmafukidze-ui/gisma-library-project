"""Book class for the library system."""


class Book:
    """Represents a book in the library."""

    def __init__(self, book_id, title, author, Year, is_available=True):
        """
        Initialize a Book object.

        Args:
            book_id (int): Unique identifier for the book
            title (str): Title of the book
            author (str): Author of the book
            Year (int): Year the book was published
            is_available (bool): Whether the book is available for borrowing
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.Year = Year
        self.is_available = is_available

    def display_info(self):
        """Display book details."""
        status = "Available" if self.is_available else "Borrowed"
        return (
            f"ID: {self.book_id}, Title: {self.title}, "
            f"Author: {self.author}, Year: {self.Year}, Status: {status}"
        )

    def borrowed_book(self):
        """Mark the book as borrowed."""
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        self.is_available = True

    def to_file_string(self):
        """Convert book data to a storable string."""
        return (
            f"{self.book_id},{self.title},{self.author},"
            f"{self.Year},{self.is_available}\n"
        )

    @staticmethod
    def from_file_string(line):
        """Create a Book object from a file string."""
        parts = line.strip().split(',')
        if len(parts) == 5:
            book_id = int(parts[0])
            title = parts[1]
            author = parts[2]
            Year = int(parts[3])
            is_available = parts[4] == 'True'
            return Book(book_id, title, author, Year, is_available)
        return None
