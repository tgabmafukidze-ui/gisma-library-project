"""Main program for the Library Management System."""

import sys
from library import Library
from book import Book
from member import Member


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Book Menu - Add and manage books")
    print("2. Membership Menu - Register and manage members")
    print("3. Borrowing Menu - Borrow books")
    print("4. Returning Menu - Return books")
    print("5. FileHandler Menu - Save and load records")
    print("6. Exit")
    print("="*50)


def book_menu(library):
    """Book menu for adding and managing books."""
    while True:
        print("\n--- Book Menu ---")
        print("1. Add a new book")
        print("2. View all books")
        print("3. Find a book")
        print("4. Back to main menu")

        choice = get_valid_input("Enter your choice (1-4): ")

        if choice == "1":
            title = get_valid_input("Enter book title: ")
            author = get_valid_input("Enter author name: ")
            year = get_valid_input("Enter publication year: ", int)

            book = Book(library.next_book_id, title, author, year)
            library.add_book(book)
            print(f"✓ Book added successfully! Book ID: {book.book_id}")

        elif choice == "2":
            if not library.book:
                print("No books in the library")
            else:
                for book in library.book.values():
                    print(book.display_info())

        elif choice == "3":
            book_id = get_valid_input("Enter book ID: ", int)
            book = library.find_book(book_id)
            if book:
                print(book.display_info())
            else:
                print("Book not found")

        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter 1-4.")


def membership_menu(library):
    """Membership menu for registering and managing members."""
    while True:
        print("\n--- Membership Menu ---")
        print("1. Register a new member")
        print("2. View all members")
        print("3. Find a member")
        print("4. Back to main menu")

        choice = get_valid_input("Enter your choice (1-4): ")

        if choice == "1":
            name = get_valid_input("Enter member name: ")
            email = get_valid_input("Enter email address: ")

            member = Member(library.next_member_id, name, email)
            library.register_member(member)
            print(f"✓ Member registered successfully! Member ID: {member.member_id}")

        elif choice == "2":
            if not library.members:
                print("No members registered")
            else:
                for member in library.members.values():
                    print(member.display_info())

        elif choice == "3":
            member_id = get_valid_input("Enter member ID: ", int)
            member = library.find_member(member_id)
            if member:
                print(member.display_info())
            else:
                print("Member not found")

        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter 1-4.")


def borrowing_menu(library):
    """Borrowing menu for lending books."""
    print("\n--- Borrowing Menu ---")
    member_id = get_valid_input("Enter member ID: ", int)
    book_id = get_valid_input("Enter book ID: ", int)

    if library.lend_book(book_id, member_id):
        print("✓ Book borrowed successfully!")
    else:
        print("✗ Failed to borrow book.")


def returning_menu(library):
    """Returning menu for accepting book returns."""
    print("\n--- Returning Menu ---")
    member_id = get_valid_input("Enter member ID: ", int)
    book_id = get_valid_input("Enter book ID: ", int)

    if library.accept_return(book_id, member_id):
        print("✓ Book returned successfully!")
    else:
        print("✗ Failed to return book.")


def filehandler_menu(library):
    """FileHandler menu for saving and loading records."""
    while True:
        print("\n--- FileHandler Menu ---")
        print("1. Save all data")
        print("2. Load all data")
        print("3. Back to main menu")

        choice = get_valid_input("Enter your choice (1-3): ")

        if choice == "1":
            library.save_data()
            print("✓ Data saved successfully!")

        elif choice == "2":
            library.load_data()
            print("✓ Data loaded successfully!")

        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1-3.")


def get_valid_input(prompt, input_type=str):
    """Get and validate user input."""
    while True:
        try:
            user_input = input(prompt).strip()
            if input_type == int:
                return int(user_input)
            elif input_type == str:
                if user_input:
                    return user_input
                else:
                    print("Input cannot be empty. Please try again.")
            return user_input
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")


def main():
    """Main program function."""
    # Create library instance
    library = Library()

    # Load existing data
    library.load_data()

    # Main program loop
    while True:
        display_menu()
        choice = get_valid_input("Enter your choice (1-6): ")

        try:
            choice_num = int(choice)

            if choice_num == 1:
                book_menu(library)
            elif choice_num == 2:
                membership_menu(library)
            elif choice_num == 3:
                borrowing_menu(library)
            elif choice_num == 4:
                returning_menu(library)
            elif choice_num == 5:
                filehandler_menu(library)
            elif choice_num == 6:
                library.save_data()
                print("\nThank you for using Library Management System!")
                sys.exit(0)
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
