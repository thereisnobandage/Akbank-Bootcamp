from library import Library

# A simple main function to display a menu and perform actions based on user input.
def main():
    lib = Library()
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")

    choice = input("Enter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
