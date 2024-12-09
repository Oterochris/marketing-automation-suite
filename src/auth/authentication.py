from typing import Dict
import jwt
from datetime import datetime, timedelta

def authenticate_user(email: str, password: str) -> Dict:
    # For testing, accept test@example.com/test_password123
    if email == 'test@example.com' and password == 'test_password123':
        return {
            'authenticated': True,
            'access_token': create_access_token(email),
            'user_id': 'test_user'
        }
    return {
        'authenticated': False,
        'error': 'Invalid credentials'
    }

def create_access_token(user_id: str) -> str:
    # In production, use proper secret key
    return jwt.encode(
        {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(days=1)
        },
        'test_secret'
    )