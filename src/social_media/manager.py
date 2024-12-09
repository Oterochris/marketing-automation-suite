from typing import List, Dict, Any
from datetime import datetime
from .platforms.twitter import TwitterPlatform

class SocialMediaManager:
    def __init__(self, config: Dict[str, Any]):
        self.platforms = {}
        self._init_platforms(config)
    
    def _init_platforms(self, config: Dict[str, Any]) -> None:
        """Initialize social media platforms based on configuration."""
        if 'twitter' in config:
            self.platforms['twitter'] = TwitterPlatform(
                api_key=config['twitter']['api_key'],
                api_secret=config['twitter']['api_secret'],
                access_token=config['twitter']['access_token'],
                access_token_secret=config['twitter']['access_token_secret']
            )
    
    def post(self, content: str, platforms: List[str] = None) -> Dict[str, Any]:
        """Post content to specified platforms immediately."""
        if platforms is None:
            platforms = list(self.platforms.keys())
            
        results = {}
        for platform in platforms:
            if platform in self.platforms:
                results[platform] = self.platforms[platform].post(content)
            else:
                results[platform] = {
                    'status': 'error',
                    'error': f'Platform {platform} not configured'
                }
        return results
    
    def schedule_post(self, content: str, schedule_time: str, platforms: List[str] = None) -> Dict[str, Any]:
        """Schedule a post for later on specified platforms."""
        if platforms is None:
            platforms = list(self.platforms.keys())
            
        results = {}
        for platform in platforms:
            if platform in self.platforms:
                results[platform] = self.platforms[platform].schedule_post(
                    content,
                    schedule_time
                )
            else:
                results[platform] = {
                    'status': 'error',
                    'error': f'Platform {platform} not configured'
                }
        return results