from flask import Blueprint, request, jsonify
import jwt
from app.models.user import User
from app.utils.authentication import generate_access_token

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/logout', methods=['POST'])
def logout_user():
    # Get the user's access token from the request
    access_token = request.headers.get('Authorization')
    
    if not access_token:
        return jsonify({'message': 'Access token is missing'}), 401

    try:
        # Decode the access token to get user_id
        payload = jwt.decode(access_token, app.config['JWT_SECRET_KEY'], algorithms=["HS256"])
        user_id = payload['user_id']

        # Implement user logout logic (if needed)
        # Invalidation of the token is optional because JWTs are stateless

        return jsonify({'message': 'User has been logged out successfully'})
    
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401

@auth_routes.route('/validate_token', methods=['POST'])
def validate_token():
    # Get the user's access token from the request
    access_token = request.headers.get('Authorization')

    if not access_token:
        return jsonify({'message': 'Access token is missing'}), 401

    try:
        # Decode the access token to get user_id
        payload = jwt.decode(access_token, app.config['JWT_SECRET_KEY'], algorithms=["HS256"])
        user_id = payload['user_id']

        # Check if the user exists (optional, you can add more validation)
        user = User.objects(id=user_id).first()
        if user:
            return jsonify({'message': 'Token is valid'})

        return jsonify({'message': 'User does not exist'}), 401
    
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401

