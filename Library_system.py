class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class FictionBook(Book):
    def __init__(self, title, author, isbn, genre):
        super().__init__(title, author, isbn)
        self.genre = genre

    def __str__(self):
        return super().__str__() + f" [Genre: {self.genre}]"


class AcademicBook(Book):
    def __init__(self, title, author, isbn, subject):
        super().__init__(title, author, isbn)
        self.subject = subject

    def __str__(self):
        return super().__str__() + f" [Subject: {self.subject}]"


class Borrower:
    def __init__(self, name, borrower_id):
        self.name = name
        self.borrower_id = borrower_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} has successfully borrowed {book.title}.")
        else:
            print(f"Sorry, {book.title} is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title}.")

    def __str__(self):
        borrowed_titles = ', '.join([book.title for book in self.borrowed_books]) or "No books borrowed"
        return f"{self.name} (ID: {self.borrower_id}) - Borrowed Books: {borrowed_titles}"


class Library:
    def __init__(self):
        self.books = []
        self.borrowers = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}.")

    def add_borrower(self, borrower):
        self.borrowers.append(borrower)
        print(f"Added borrower: {borrower.name}.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            print(book)
        print()

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_borrowers(self):
        print("\nLibrary Borrowers:")
        for borrower in self.borrowers:
            print(borrower)
        print()


# Main program
def main():
    library = Library()

    # Adding sample books
    library.add_book(FictionBook("1984", "George Orwell", "234537", "Dystopian"))
    library.add_book(AcademicBook("Linear Algebra", "Gilbert Strang", "987654321", "Mathematics"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "243837465"))

    # Adding sample borrowers
    borrower1 = Borrower("Alice", 1)
    borrower2 = Borrower("Bob", 2)
    library.add_borrower(borrower1)
    library.add_borrower(borrower2)

    # Menu
    while True:
        print("\nLibrary Management System")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Borrowers")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()

        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            type_of_book = input("Is it Fiction or Academic? (Enter 'F' or 'A', leave blank for general): ").strip().upper()

            if type_of_book == "F":
                genre = input("Enter genre: ")
                library.add_book(FictionBook(title, author, isbn, genre))
            elif type_of_book == "A":
                subject = input("Enter subject: ")
                library.add_book(AcademicBook(title, author, isbn, subject))
            else:
                library.add_book(Book(title, author, isbn))

        elif choice == "3":
            borrower_name = input("Enter borrower's name: ")
            book_title = input("Enter book title to borrow: ")

            borrower = next((b for b in library.borrowers if b.name.lower() == borrower_name.lower()), None)
            book = library.find_book_by_title(book_title)

            if borrower and book:
                borrower.borrow_book(book)
            else:
                print("Borrower or Book not found!")

        elif choice == "4":
            borrower_name = input("Enter borrower's name: ")
            book_title = input("Enter book title to return: ")

            borrower = next((b for b in library.borrowers if b.name.lower() == borrower_name.lower()), None)
            book = library.find_book_by_title(book_title)

            if borrower and book:
                borrower.return_book(book)
            else:
                print("Borrower or Book not found!")

        elif choice == "5":
            library.display_borrowers()

        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

     