from flask import Blueprint, request, jsonify
import jwt
from app.models.user import User
from app.utils.authentication import generate_access_token, authenticate_user

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/register', methods=['POST'])
def register_user():
    # Get user data from the request
    data = request.get_json()

    # Validate user input (you can use the validation functions from utils/validation.py)
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Username, email, and password are required'}), 400

    # Check if the username or email already exists
    if User.objects(username=data['username']).first() or User.objects(email=data['email']).first():
        return jsonify({'message': 'Username or email is already in use'}), 400

    # Create a new user
    user = User(
        username=data['username'],
        email=data['email'],
        password=data['password'],  # You should hash the password
    )
    user.save()

    # Generate an access token and return it in the response
    access_token = generate_access_token(user)

    return jsonify({'message': 'User registered successfully', 'access_token': access_token})

@user_routes.route('/login', methods=['POST'])
def login_user():
    # Get user credentials from the request
    data = request.get_json()

    # Validate user input (you can use the validation functions from utils/validation.py)
    if 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Username and password are required'}), 400

    # Authenticate the user
    user = authenticate_user(data['username'], data['password'])

    if not user:
        return jsonify({'message': 'Invalid credentials'}), 401

    # Generate an access token and return it in the response
    access_token = generate_access_token(user)

    return jsonify({'message': 'User logged in successfully', 'access_token': access_token})

@user_routes.route('/profile', methods=['GET', 'PUT'])
def user_profile():
    # Use authentication to verify the user's identity
    access_token = request.headers.get('Authorization')
    if not access_token:
        return jsonify({'message': 'Access token is missing'}), 401

    try:
        payload = jwt.decode(access_token, app.config['JWT_SECRET_KEY'], algorithms=["HS256"])
        user_id = payload['user_id']
        user = User.objects(id=user_id).first()

        if not user:
            return jsonify({'message': 'User not found'}), 404

        if request.method == 'GET':
            # Return the user's profile data
            return jsonify({
                'username': user.username,
                'email': user.email,
                'name': user.profile['name'],
                'bio': user.profile['bio']
            })

        if request.method == 'PUT':
            # Update the user's profile (example: update name and bio)
            data = request.get_json()
            user.profile['name'] = data.get('name', user.profile['name'])
            user.profile['bio'] = data.get('bio', user.profile['bio'])
            user.save()
            return jsonify({'message': 'Profile updated successfully'})

    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401
