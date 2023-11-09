from flask import Flask
from app import config
from dotenv import load_dotenv
from app.routes.user_routes import user_routes
from app.routes.book_routes import book_routes
from app.routes.chapter_routes import chapter_routes
from app.routes.auth_routes import auth_routes
from app.routes.payment_routes import payment_routes
from mongoengine import connect

# Load the environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Load application configurations from the config module
app.config.from_object(config)

# MongoDB Configuration
connection = connect(
    db="book_reading_db",
    host="mongodb://localhost:27017/book_reading_db",
)

# Function to check MongoDB connection
def is_mongodb_connected():
    try:
        connection # Try to get the connection
        return True
    except Exception as e:
        return False

# Check the MongoDB connection
if is_mongodb_connected():
    print("MongoDB connection is active.")
else:
    print("MongoDB connection is not active.")

# Register the route blueprints
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(book_routes, url_prefix='/api/books')
app.register_blueprint(chapter_routes, url_prefix='/api/chapters')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(payment_routes, url_prefix='/api/payments')


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])

