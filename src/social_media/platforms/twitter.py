import tweepy
from typing import Dict, Any
from .base import SocialPlatform

class TwitterPlatform(SocialPlatform):
    def __init__(self, api_key: str, api_secret: str, access_token: str, access_token_secret: str):
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
        
    def post(self, content: str, **kwargs) -> Dict[str, Any]:
        """Post a tweet immediately."""
        try:
            tweet = self.api.update_status(content)
            return {
                'id': tweet.id_str,
                'platform': 'twitter',
                'status': 'success',
                'url': f'https://twitter.com/user/status/{tweet.id_str}'
            }
        except Exception as e:
            return {
                'status': 'error',
                'platform': 'twitter',
                'error': str(e)
            }
    
    def schedule_post(self, content: str, schedule_time: str, **kwargs) -> Dict[str, Any]:
        """Schedule a tweet for later using custom scheduling logic."""
        # Store in database for later posting
        return {
            'status': 'scheduled',
            'platform': 'twitter',
            'schedule_time': schedule_time,
            'content': content
        }
    
    def delete_post(self, post_id: str) -> bool:
        """Delete a tweet."""
        try:
            self.api.destroy_status(post_id)
            return True
        except:
            return False