##  Mini Library Management System (Python)

  # Book storage
library = []
# Add a new book
def add_book():
    isbn = input("Enter ISBN: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    publisher = input("Enter Publisher: ")
    genre = input("Enter Genre: ")
    try:
        quantity = int(input("Enter Quantity: "))
    except ValueError:
        print("Invalid quantity. Must be a number.")
        return

    book = {
        "ISBN": isbn,
        "Title": title,
        "Author": author,
        "Publisher": publisher,
        "Genre": genre,
        "Quantity": quantity
    }
    library.append(book)
    print(" Book added successfully!")

# View all books
def view_books():
    if not library:
        print(" No books in the library.")
        return
    for i, book in enumerate(library, 1):
        print(f"\n Book {i}")
        for key, value in book.items():
            print(f"{key}: {value}")

# Search for a book
def search_book():
    keyword = input(" Enter search keyword: ").lower()
    found = False
    for book in library:
        if any(keyword in str(value).lower() for value in book.values()):
            print("\n Book Found:")
            for key, value in book.items():
                print(f"{key}: {value}")
            found = True
    if not found:
        print(" Book not found.")

# Update book info
def update_book():
    isbn = input("Enter ISBN of the book to update: ")
    for book in library:
        if book["ISBN"] == isbn:
            print(" Enter new details (leave blank to keep current):")
            for key in ["Title", "Author", "Publisher", "Genre", "Quantity"]:
                new_value = input(f"{key} ({book[key]}): ")
                if new_value:
                    book[key] = int(new_value) if key == "Quantity" else new_value
            print("Book updated successfully!")
            return
    print(" Book not found.")

# Delete a book
def delete_book():
    isbn = input("Enter ISBN of the book to delete: ")
    for book in library:
        if book["ISBN"] == isbn:
            library.remove(book)
            print("🗑 Book deleted successfully!")
            return
    print(" Book not found.")

# Menu
def menu():
    while True:
        print("\nLibrary Menu")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            update_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            print(" Exiting Library System. Goodbye!")
            break
        else:
            print(" Invalid choice. Please select from 1 to 6.")