import os

# MongoDB Configuration
MONGODB_SETTINGS = {
    'db': os.environ.get('DATABASE_NAME', 'book_reading_db'),
    'host': os.environ.get('MONGODB_HOST', 'mongodb://localhost:27017/book_reading_db'),
    'connect': True,  # Set to True for production
}

# Flask Configuration
SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
DEBUG = os.environ.get('DEBUG', True)  # Set to False for production

# JWT Configuration (for user authentication)
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'your_jwt_secret_key')
JWT_ACCESS_TOKEN_EXPIRES = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 60 * 60 * 24))  # 24 hours in seconds

# Other Configurations
# Add other configuration settings as needed

# Environment-specific configurations
if os.environ.get('FLASK_ENV') == 'production':
    DEBUG = False
    # Set other production-specific configurations here

# You can add more configuration settings as your application grows

# Use environment variables to override default settings
# You can set these environment variables in a .env file or your deployment environment
