"""FileHandler class for the library system."""


class FileHandler:
    """Handles file I/O operations for library data."""

    def __init__(self, book_file="../data/books.csv", member_file="../data/members.csv"):
        """
        Initialize a FileHandler object.

        Args:
            book_file (str): Path to the books file
            member_file (str): Path to the members file
        """
        self.book_file = book_file
        self.member_file = member_file

    def save_book(self, books):
        """Save all books to a CSV file."""
        try:
            with open(self.book_file, 'w') as file:
                for book in books.values():
                    file.write(book.to_file_string())
            return True
        except IOError as e:
            print(f"Error saving books: {e}")
            return False

    def load_books(self):
        """Load books from a CSV file."""
        books = {}
        try:
            with open(self.book_file, 'r') as file:
                for line in file:
                    from book import Book
                    book = Book.from_file_string(line)
                    if book:
                        books[book.book_id] = book
            return books
        except FileNotFoundError:
            print(f"File {self.book_file} not found. Creating new library.")
            return {}
        except IOError as e:
            print(f"Error loading books: {e}")
            return {}

    def save_members(self, members):
        """Save all members to a CSV file."""
        try:
            with open(self.member_file, 'w') as file:
                for member in members.values():
                    file.write(member.to_file_string())
            return True
        except IOError as e:
            print(f"Error saving members: {e}")
            return False

    def load_members(self):
        """Load members from a CSV file."""
        members = {}
        try:
            with open(self.member_file, 'r') as file:
                for line in file:
                    from member import Member
                    member = Member.from_file_string(line)
                    if member:
                        members[member.member_id] = member
            return members
        except FileNotFoundError:
            print(f"File {self.member_file} not found. Creating new member database.")
            return {}
        except IOError as e:
            print(f"Error loading members: {e}")
            return {}