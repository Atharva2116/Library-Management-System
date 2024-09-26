class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books_available = []
        self.borrowed_books = []

    def add_book(self, book):
        self.books_available.append(book)

    def borrow_book(self, isbn):
        for book in self.books_available:
            if book.isbn == isbn:
                self.books_available.remove(book)
                self.borrowed_books.append(book)
                return True
        return False