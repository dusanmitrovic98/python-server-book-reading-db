import jwt
from datetime import datetime, timedelta
from app.config import JWT_SECRET_KEY, JWT_ACCESS_TOKEN_EXPIRES
from app.models.user import User

def generate_access_token(user):
    payload = {
        "user_id": str(user.id),
        "exp": datetime.utcnow() + timedelta(seconds=JWT_ACCESS_TOKEN_EXPIRES)
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")
    return token

def authenticate_user(username, password):
    user = User.objects(username=username).first()
    if user and user.password == password:  # You should hash and compare the password
        return user
    return None
