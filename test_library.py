import unittest
from library import Library, Book

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        library = Library()
        book = Book("12345", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book(book)
        self.assertIn(book, library.books_available)

    def test_borrow_book(self):
        library = Library()
        book = Book("12345", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book(book)
        result = library.borrow_book(book.isbn)
        self.assertTrue(result)
        self.assertNotIn(book, library.books_available)
        
    def test_return_book(self):
        library = Library()
        book = Book("12345", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book(book)
        library.borrow_book(book.isbn)
        library.return_book(book.isbn)
        self.assertIn(book, library.books_available)
        
    def test_view_available_books(self):
        library = Library()
        book1 = Book("12345", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        book2 = Book("67890", "1984", "George Orwell", 1949)
        library.add_book(book1)
        library.add_book(book2)
        available_books = library.view_available_books()
        self.assertIn(book1, available_books)
        self.assertIn(book2, available_books)

if __name__ == '__main__':
    unittest.main()
