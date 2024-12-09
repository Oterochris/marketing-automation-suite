import pytest
from src.social_media.manager import SocialMediaManager
from src.auth.authentication import authenticate_user
from src.backend.error_handler import handle_error

def test_rate_limit_handling():
    manager = SocialMediaManager({'tier': 'free'})
    
    # Simulate rate limit exceeded
    results = []
    for _ in range(6):  # Free tier limit is 5
        results.append(manager.post(content='Test post'))
    
    assert results[-1]['twitter']['status'] == 'error'
    assert 'rate limit' in results[-1]['twitter']['error'].lower()

def test_api_error_handling():
    manager = SocialMediaManager({
        'twitter': {
            'api_key': 'invalid_key'
        }
    })
    
    result = manager.post(content='Test post')
    assert result['twitter']['status'] == 'error'
    assert 'authentication failed' in result['twitter']['error'].lower()

def test_invalid_input_handling():
    # Test empty content
    manager = SocialMediaManager({'tier': 'free'})
    result = manager.post(content='')
    
    assert result['status'] == 'error'
    assert 'content cannot be empty' in result['error'].lower()

def test_database_error_handling():
    result = handle_error({
        'type': 'database',
        'message': 'Connection failed'
    })
    
    assert result['status'] == 'error'
    assert 'please try again later' in result['message'].lower()