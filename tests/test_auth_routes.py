import unittest
from flask import Flask
from app import config
from app.routes.auth_routes import auth_routes

class AuthRoutesTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_routes, url_prefix='/api/auth')
        self.app.config.from_object(config)

        self.client = self.app.test_client()

    def test_user_logout(self):
        # Send a POST request with a valid access token
        access_token = "your_valid_access_token_here"
        response = self.client.post('/api/auth/logout', headers={'Authorization': access_token})

        # Assert the response for success (status code 200 and expected message)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'User has been logged out successfully')

    def test_validate_token(self):
        # Send a POST request with a valid access token
        access_token = "your_valid_access_token_here"
        response = self.client.post('/api/auth/validate_token', headers={'Authorization': access_token})

        # Assert the response for success (status code 200 and expected message)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Token is valid')
