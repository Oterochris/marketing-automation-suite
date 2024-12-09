from src.social_media.manager import SocialMediaManager
from src.auth.user_manager import UserManager

# This is your customer management system
user_manager = UserManager()

# When a customer signs up, they provide their own API keys
user_manager.add_user('customer123', {
    'twitter': {
        'api_key': 'CUSTOMER_PROVIDED_KEY',
        'api_secret': 'CUSTOMER_PROVIDED_SECRET',
        'access_token': 'CUSTOMER_PROVIDED_TOKEN',
        'access_token_secret': 'CUSTOMER_PROVIDED_TOKEN_SECRET'
    }
})

# Your system then uses their keys to post on their behalf
user_keys = user_manager.get_user_keys('customer123')
manager = SocialMediaManager(user_keys)

# Now posts will go to the customer's social media accounts
manager.schedule_post(
    content='Post from customer account!',
    schedule_time='2024-12-10 15:00:00',
    platforms=['twitter']
)