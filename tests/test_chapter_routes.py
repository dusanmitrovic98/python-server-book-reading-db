import unittest
from flask import Flask
from app import config
from app.routes.chapter_routes import chapter_routes

class ChapterRoutesTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(chapter_routes, url_prefix='/api/chapters')
        self.app.config.from_object(config)

        self.client = self.app.test_client()

    def test_get_chapter_content(self):
        # Send a GET request with a valid chapter ID
        chapter_id = "your_valid_chapter_id_here"
        response = self.client.get(f'/api/chapters/{chapter_id}')

        # Assert the response for success (status code 200 and expected chapter content)
        self.assertEqual(response.status_code, 200)
        # Assert other attributes in the chapter content response
