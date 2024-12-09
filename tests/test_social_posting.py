import pytest
from datetime import datetime, timedelta
from src.social_media.manager import SocialMediaManager

# Mock configuration for testing
test_config = {
    'twitter': {
        'api_key': 'test_key',
        'api_secret': 'test_secret',
        'access_token': 'test_token',
        'access_token_secret': 'test_token_secret'
    }
}

def test_post_creation():
    manager = SocialMediaManager(test_config)
    
    # Test immediate post
    result = manager.post(
        content='Test post from automation suite!',
        platforms=['twitter']
    )
    assert result['twitter']['status'] == 'success'

def test_schedule_post():
    manager = SocialMediaManager(test_config)
    
    # Schedule post for tomorrow
    tomorrow = datetime.now() + timedelta(days=1)
    result = manager.schedule_post(
        content='Scheduled test post',
        schedule_time=tomorrow.strftime('%Y-%m-%d %H:%M:%S'),
        platforms=['twitter']
    )
    assert result['twitter']['status'] == 'scheduled'

def test_post_limits():
    # Test with Free tier limits
    free_config = {'tier': 'free', **test_config}
    manager = SocialMediaManager(free_config)
    
    # Try to exceed daily post limit
    posts = []
    for i in range(6):  # Free tier limit is 5
        result = manager.post(
            content=f'Test post {i}',
            platforms=['twitter']
        )
        posts.append(result)
    
    # Verify last post was rejected
    assert posts[-1]['twitter']['status'] == 'error'
    assert 'daily limit exceeded' in posts[-1]['twitter']['error']

def test_platform_integration():
    manager = SocialMediaManager(test_config)
    
    # Test with invalid credentials
    bad_config = {
        'twitter': {
            'api_key': 'invalid',
            'api_secret': 'invalid',
            'access_token': 'invalid',
            'access_token_secret': 'invalid'
        }
    }
    manager_bad = SocialMediaManager(bad_config)
    
    result = manager_bad.post(
        content='This should fail',
        platforms=['twitter']
    )
    assert result['twitter']['status'] == 'error'
    assert 'authentication' in result['twitter']['error'].lower()