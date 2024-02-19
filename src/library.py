class Library:
    # Initializes the object, opens the "data/books.txt" file in append mode for both reading and writing.
    def __init__(self):
        self.file = open("data/books.txt", "a+")

    # Closes the "data/books.txt" file
    def __del__(self):
        self.file.close()

    # Reads the contents of the "data/books.txt" file and prints them to the console
    def list_books(self):
        self.file.seek(0)  # Move cursor to the beginning of the file
        books = self.file.readlines()
        if not books:
            print("No books available.")
        else:
            print("List of Books:")
            for book in books:
                book_info = book.strip().split(",")
                if len(book_info) >= 2:
                    print(f"Title: {book_info[0]}, Author: {book_info[1]}")
                else:
                    print("Invalid book format in the database.")

    # Adds a new book to the "data/books.txt" file
    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        release_year = input("Enter the release year of the book: ")
        num_pages = input("Enter the number of pages of the book: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    # Removes a book from the "data/books.txt" file
    def remove_book(self):
        title = input("Enter the title of the book you want to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        found = False
        updated_books = []
        for book in books:
            if title in book:
                found = True
            else:
                updated_books.append(book)
        if not found:
            print("Book not found.")
        else:
            self.file.seek(0)
            self.file.truncate()
            for book in updated_books:
                self.file.write(book)
            print("Book removed successfully.")
