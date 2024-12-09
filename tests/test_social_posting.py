import pytest
from datetime import datetime, timedelta
from src.social_media.manager import SocialMediaManager

# Test configuration
@pytest.fixture
def test_config():
    return {
        'tier': 'free',
        'twitter': {
            'api_key': 'test_key',
            'api_secret': 'test_secret',
            'access_token': 'test_token',
            'access_token_secret': 'test_token_secret'
        }
    }

def test_post_creation(test_config):
    manager = SocialMediaManager(test_config)
    result = manager.post(
        content='Test post from automation suite!',
        platforms=['twitter']
    )
    assert result['twitter']['status'] == 'success'

def test_schedule_post(test_config):
    manager = SocialMediaManager(test_config)
    tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
    
    result = manager.schedule_post(
        content='Scheduled test post',
        schedule_time=tomorrow,
        platforms=['twitter']
    )
    assert result['twitter']['status'] == 'scheduled'