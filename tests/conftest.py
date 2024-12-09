import pytest

@pytest.fixture
def test_config():
    return {
        'twitter': {
            'api_key': 'test_key',
            'api_secret': 'test_secret',
            'access_token': 'test_token',
            'access_token_secret': 'test_token_secret'
        }
    }