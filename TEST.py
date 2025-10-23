# Import your functions here if they are in another file
# from library_system import add_book, view_books, search_book, update_book, delete_book, library

# For this test, we'll simulate the library list directly

library = []
def add_book(isbn, title, author, publisher, genre, quantity):
    book = {
        "ISBN": isbn,
        "Title": title,
        "Author": author,
        "Publisher": publisher,
        "Genre": genre,
        "Quantity": quantity
    }
    library.append(book)


def search_book(keyword):
    return [book for book in library if any(keyword.lower() in str(value).lower() for value in book.values())]


def update_book(isbn, new_data):
    for book in library:
        if book["ISBN"] == isbn:
            book.update(new_data)
            return True
    return False


def delete_book(isbn):
    for book in library:
        if book["ISBN"] == isbn:
            library.remove(book)
            return True
    return False




    def setUp(self):
        library.clear()
        add_book("123", "Python Basics", "John Doe", "TechPress", "Programming", 5)

    def test_add_book(self):
        self.assertEqual(len(library), 1)
        self.assertEqual(library[0]["Title"], "Python Basics")

    def test_search_book(self):
        results = search_book("Python")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["Author"], "John Doe")

    def test_update_book(self):
        success = update_book("123", {"Title": "Advanced Python", "Quantity": 10})
        self.assertTrue(success)
        self.assertEqual(library[0]["Title"], "Advanced Python")
        self.assertEqual(library[0]["Quantity"], 10)

    def test_delete_book(self):
        success = delete_book("123")
        self.assertTrue(success)
        self.assertEqual(len(library), 0)

    def test_search_not_found(self):
        results = search_book("Java")
        self.assertEqual(len(results), 0)

    def test_update_not_found(self):
        success = update_book("999", {"Title": "Ghost Book"})
        self.assertFalse(success)

    def test_delete_not_found(self):
        success = delete_book("999")
        self.assertFalse(success)