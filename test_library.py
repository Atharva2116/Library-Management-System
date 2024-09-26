import unittest
from library import Library, Book

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        library = Library()
        book = Book("12345", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book(book)
        self.assertIn(book, library.books_available)

if __name__ == '__main__':
    unittest.main()
