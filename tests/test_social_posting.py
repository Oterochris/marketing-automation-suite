import pytest
from datetime import datetime, timedelta
from src.social_media.manager import SocialMediaManager

@pytest.fixture
def test_config():
    return {
        'tier': 'free',
        'twitter': {
            'api_key': 'test_key',
            'api_secret': 'test_secret'
        }
    }

def test_post_creation(test_config):
    manager = SocialMediaManager(test_config)
    result = manager.post('Test post')
    assert result['twitter']['status'] == 'success'

def test_empty_post(test_config):
    manager = SocialMediaManager(test_config)
    result = manager.post('')
    assert result['status'] == 'error'
    assert 'empty' in result['error'].lower()

def test_long_post(test_config):
    manager = SocialMediaManager(test_config)
    long_post = 'x' * 281  # Twitter's limit is 280
    result = manager.post(long_post)
    assert result['status'] == 'error'
    assert 'too long' in result['error'].lower()

def test_free_tier_limits(test_config):
    manager = SocialMediaManager(test_config)
    
    # Should allow 5 posts
    results = []
    for i in range(6):
        results.append(manager.post(f'Test post {i}'))
    
    # First 5 should succeed
    for i in range(5):
        assert results[i]['twitter']['status'] == 'success'
    
    # 6th should fail
    assert results[5]['status'] == 'error'
    assert 'limit' in results[5]['error'].lower()

def test_schedule_post(test_config):
    manager = SocialMediaManager(test_config)
    tomorrow = datetime.now() + timedelta(days=1)
    schedule_time = tomorrow.strftime('%Y-%m-%d %H:%M:%S')
    
    result = manager.schedule_post('Scheduled post', schedule_time)
    assert result['twitter']['status'] == 'scheduled'
    assert result['twitter']['schedule_time'] == schedule_time

def test_past_schedule_time(test_config):
    manager = SocialMediaManager(test_config)
    yesterday = datetime.now() - timedelta(days=1)
    schedule_time = yesterday.strftime('%Y-%m-%d %H:%M:%S')
    
    result = manager.schedule_post('Past post', schedule_time)
    assert result['status'] == 'error'
    assert 'past' in result['error'].lower()

def test_multiple_platforms(test_config):
    # Add LinkedIn to config
    test_config['linkedin'] = {
        'client_id': 'test_id',
        'client_secret': 'test_secret'
    }
    
    manager = SocialMediaManager(test_config)
    result = manager.post('Multi-platform post', platforms=['twitter', 'linkedin'])
    
    assert result['twitter']['status'] == 'success'
    assert result['linkedin']['status'] == 'success'
