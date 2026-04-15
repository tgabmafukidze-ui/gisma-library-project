"""Member class for the library system."""


class Member:
    """Represents a library member."""

    def __init__(self, member_id, name, email, borrowed_books=None):
        """
        Initialize a Member object.

        Args:
            member_id (int): Unique identifier for the member
            name (str): Name of the member
            email (str): Email address of the member
            borrowed_books (list): List of borrowed book IDs
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = borrowed_books if borrowed_books else []

    def display_info(self):
        """Display member details."""
        return (
            f"ID: {self.member_id}, Name: {self.name}, "
            f"Email: {self.email}, Books Borrowed: {len(self.borrowed_books)}"
        )

    def borrow_book(self, book_id):
        """Add a borrowed book to member's list."""
        if book_id not in self.borrowed_books:
            self.borrowed_books.append(book_id)
            return True
        return False

    def return_book(self, book_id):
        """Remove a returned book from member's list."""
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False

    def to_file_string(self):
        """Convert member data to a storable string format."""
        books_str = ";".join(map(str, self.borrowed_books))
        return (
            f"{self.member_id},{self.name},{self.email},{books_str}\n"
        )

    @staticmethod
    def from_file_string(line):
        """Create a Member object from a file string."""
        parts = line.strip().split(',')
        if len(parts) >= 3:
            member_id = int(parts[0])
            name = parts[1]
            email = parts[2]
            member = Member(member_id, name, email)
            if len(parts) > 3 and parts[3]:
                member.borrowed_books = [int(x) for x in parts[3].split(";")]
            return member
        return None
