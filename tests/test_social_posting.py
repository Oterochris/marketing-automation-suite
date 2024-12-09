from src.social_media.manager import SocialMediaManager

def test_post_creation():
    config = {
        'tier': 'free',
        'twitter': {
            'api_key': 'test_key',
            'api_secret': 'test_secret'
        }
    }
    manager = SocialMediaManager(config)
    result = manager.post('Test post')
    assert result['twitter']['status'] == 'success'