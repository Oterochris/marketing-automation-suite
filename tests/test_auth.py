import pytest
from src.auth.user_manager import UserManager
from src.auth.authentication import authenticate_user, create_access_token

@pytest.fixture
def test_user_data():
    return {
        'email': 'test@example.com',
        'password': 'test_password123',
        'company_name': 'Test Company'
    }

def test_user_registration(test_user_data):
    user_manager = UserManager()
    result = user_manager.register_user(test_user_data)
    
    assert result['status'] == 'success'
    assert 'user_id' in result

def test_user_login(test_user_data):
    result = authenticate_user(
        email=test_user_data['email'],
        password=test_user_data['password']
    )
    
    assert result['authenticated'] is True
    assert 'access_token' in result

def test_invalid_login():
    result = authenticate_user(
        email='wrong@example.com',
        password='wrong_password'
    )
    
    assert result['authenticated'] is False
    assert 'Invalid credentials' in result['error']