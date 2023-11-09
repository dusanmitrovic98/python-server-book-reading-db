import unittest
from flask import Flask
from app import config
from app.routes.book_routes import book_routes

class BookRoutesTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(book_routes, url_prefix='/api/books')
        self.app.config.from_object(config)

        self.client = self.app.test_client()

    def test_get_book_details(self):
        # Send a GET request with a valid book ID
        book_id = "your_valid_book_id_here"
        response = self.client.get(f'/api/books/{book_id}')

        # Assert the response for success (status code 200 and expected book details)
        self.assertEqual(response.status_code, 200)
        # Assert other attributes in the book details response

    def test_search_books(self):
        # Send a GET request with a search query
        query = "your_search_query_here"
        response = self.client.get(f'/api/books/search?query={query}')

        # Assert the response for success (status code 200 and a list of matching books)
        self.assertEqual(response.status_code, 200)
        # Assert the structure and content of the list of matching books
