from src.social_media.manager import SocialMediaManager

# Example configuration
config = {
    'twitter': {
        'api_key': 'your_api_key',
        'api_secret': 'your_api_secret',
        'access_token': 'your_access_token',
        'access_token_secret': 'your_access_token_secret'
    }
}

# Initialize the manager
manager = SocialMediaManager(config)

# Post immediately to Twitter
result = manager.post(
    content='Hello from Marketing Automation Suite! 🚀',
    platforms=['twitter']
)
print('Immediate post result:', result)

# Schedule a post for later
scheduled = manager.schedule_post(
    content='This is a scheduled post from Marketing Automation Suite! 📅',
    schedule_time='2024-12-10 15:00:00',
    platforms=['twitter']
)
print('Scheduled post result:', scheduled)