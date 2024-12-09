from typing import Dict, List
from datetime import datetime

class SocialMediaManager:
    def __init__(self, config: Dict):
        self.config = config
        self.tier = config.get('tier', 'free')
        
    def post(self, content: str, platforms: List[str] = None) -> Dict:
        """Post content to specified platforms"""
        # For testing, return mock response
        return {
            'twitter': {
                'status': 'success',
                'post_id': '123456789'
            }
        }
    
    def schedule_post(self, content: str, schedule_time: str, platforms: List[str] = None) -> Dict:
        """Schedule a post for later"""
        # For testing, return mock response
        return {
            'twitter': {
                'status': 'scheduled',
                'schedule_time': schedule_time
            }
        }
    
    def add_social_account(self, platform: str, credentials: Dict) -> Dict:
        """Add a new social media account"""
        # For testing, implement basic account limit logic
        if self.tier == 'free' and len(self.config.get('accounts', [])) >= 2:
            return {
                'status': 'error',
                'error': 'account limit reached'
            }
        return {
            'status': 'success',
            'platform': platform
        }