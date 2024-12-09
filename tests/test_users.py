import pytest
from src.users.manager import UserManager

@pytest.fixture
def user_data():
    return {
        'email': 'test@example.com',
        'password': 'secure_password123',
        'company': 'Test Corp'
    }

def test_user_registration(user_data):
    user_mgr = UserManager()
    result = user_mgr.register_user(user_data)
    assert result['status'] == 'success'
    assert 'user_id' in result

def test_api_key_management(user_data):
    user_mgr = UserManager()
    keys = user_mgr.generate_api_keys('test_user')
    assert 'api_key' in keys
    assert 'api_secret' in keys