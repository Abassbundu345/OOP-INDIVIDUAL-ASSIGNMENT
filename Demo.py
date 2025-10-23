# demo.py


print("=== DEMO: Mini Library Management System ===")

print(add_book("001", "Python Basics", "John Doe", "Fiction", 5))
print(add_book("002", "Data Science 101", "Jane Smith", "Non-Fiction", 3))

print(add_member("M001", "Alice", "alice@email.com"))
print(add_member("M002", "Bob", "bob@email.com"))

print(borrow_book("M001", "001"))
print(borrow_book("M001", "002"))
print(return_book("M001", "001"))

print("Searching for 'Python':", search_books("Python"))
print(delete_book("002"))
print(delete_book("001"))
