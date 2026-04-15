"""Library class for the library system."""

from book import Book
from member import Member
from file_handler import FileHandler


class Library:
    """Represents the main library system."""

    def __init__(self):
        """Initialize a Library object."""
        self.book = {}  # Dictionary with book_id as key
        self.members = {}  # Dictionary with member_id as key
        self.next_book_id = 1
        self.next_member_id = 1

    def add_book(self, book):
        """Add a book to the library."""
        self.book[book.book_id] = book
        if book.book_id >= self.next_book_id:
            self.next_book_id = book.book_id + 1

    def register_member(self, member):
        """Register a member to the library."""
        self.members[member.member_id] = member
        if member.member_id >= self.next_member_id:
            self.next_member_id = member.member_id + 1

    def lend_book(self, book_id, member_id):
        """Lend a book to a member."""
        try:
            if book_id not in self.book:
                raise ValueError(f"Book ID {book_id} not found")
            if member_id not in self.members:
                raise ValueError(f"Member ID {member_id} not found")

            book = self.book[book_id]
            member = self.members[member_id]

            if not book.is_available:
                raise ValueError(f"Book '{book.title}' is not available")

            # Update book and member
            book.borrowed_book()
            member.borrow_book(book_id)

            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def accept_return(self, book_id, member_id):
        """Accept a book return from a member."""
        try:
            if book_id not in self.book:
                raise ValueError(f"Book ID {book_id} not found")
            if member_id not in self.members:
                raise ValueError(f"Member ID {member_id} not found")

            book = self.book[book_id]
            member = self.members[member_id]

            if book.is_available:
                raise ValueError(f"Book '{book.title}' is not borrowed")

            # Update book and member
            book.return_book()
            member.return_book(book_id)

            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def find_book(self, book_id):
        """Find a book by ID."""
        return self.book.get(book_id, None)

    def find_member(self, member_id):
        """Find a member by ID."""
        return self.members.get(member_id, None)

    def load_data(self):
        """Load all library data from files."""
        file_handler = FileHandler()
        self.book = file_handler.load_books()
        self.members = file_handler.load_members()

        # Update next IDs based on loaded data
        if self.book:
            self.next_book_id = max(self.book.keys()) + 1
        if self.members:
            self.next_member_id = max(self.members.keys()) + 1

    def save_data(self):
        """Save all library data to files."""
        file_handler = FileHandler()
        file_handler.save_book(self.book)
        file_handler.save_members(self.members)
