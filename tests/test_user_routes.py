import unittest
from flask import Flask
from app import config
from app.routes.user_routes import user_routes

class UserRoutesTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(user_routes, url_prefix='/api/users')
        self.app.config.from_object(config)

        self.client = self.app.test_client()

    def test_user_registration(self):
        # Send a POST request with registration data (e.g., username, email, and password)
        registration_data = {
            "username": "test_user",
            "email": "test@example.com",
            "password": "testpassword"
        }
        response = self.client.post('/api/users/register', json=registration_data)

        # Assert the response for success (status code 200 and expected success message)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'User registered successfully')

    def test_user_login(self):
        # Send a POST request with login data (e.g., username and password)
        login_data = {
            "username": "test_user",
            "password": "testpassword"
        }
        response = self.client.post('/api/users/login', json=login_data)

        # Assert the response for success (status code 200 and expected success message)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access_token' in response.json)  # Check for the presence of an access token

    def test_user_profile_access(self):
        # Send a GET request with a valid access token
        access_token = "your_valid_access_token_here"
        response = self.client.get('/api/users/profile', headers={'Authorization': access_token})

        # Assert the response for success (status code 200 and expected user profile data)
        self.assertEqual(response.status_code, 200)
        # Assert the structure and content of the user profile data response
