from typing import Dict, List
from datetime import datetime

class SocialMediaManager:
    MAX_POST_LENGTH = 280  # Twitter's limit
    TIER_LIMITS = {
        'free': {'posts_per_day': 5},
        'pro': {'posts_per_day': 50},
        'enterprise': {'posts_per_day': float('inf')}
    }

    def __init__(self, config: Dict):
        self.config = config
        self.tier = config.get('tier', 'free')
        self.posts_today = 0
    
    def post(self, content: str, platforms: List[str] = None) -> Dict:
        # Validate content
        if not content:
            return {
                'status': 'error',
                'error': 'Content cannot be empty'
            }
        
        if len(content) > self.MAX_POST_LENGTH:
            return {
                'status': 'error',
                'error': f'Content too long. Maximum length is {self.MAX_POST_LENGTH} characters'
            }
        
        # Check daily limit
        if self.posts_today >= self.TIER_LIMITS[self.tier]['posts_per_day']:
            return {
                'status': 'error',
                'error': f"Daily post limit reached for {self.tier} tier"
            }
        
        # Default to all configured platforms if none specified
        if platforms is None:
            platforms = [p for p in ['twitter', 'linkedin'] if p in self.config]
        
        # Post to each platform
        result = {}
        for platform in platforms:
            if platform in self.config:
                result[platform] = {
                    'status': 'success',
                    'post_id': f'{platform}_123456789'
                }
            else:
                result[platform] = {
                    'status': 'error',
                    'error': f'Platform {platform} not configured'
                }
        
        if any(r['status'] == 'success' for r in result.values()):
            self.posts_today += 1
        
        return result if len(platforms) > 1 else result.get(platforms[0], {'status': 'error', 'error': 'Invalid platform'})
    
    def schedule_post(self, content: str, schedule_time: str, platforms: List[str] = None) -> Dict:
        try:
            schedule_dt = datetime.strptime(schedule_time, '%Y-%m-%d %H:%M:%S')
            if schedule_dt <= datetime.now():
                return {
                    'status': 'error',
                    'error': 'Cannot schedule posts in the past'
                }
                
            if platforms is None:
                platforms = [p for p in ['twitter', 'linkedin'] if p in self.config]
            
            result = {}
            for platform in platforms:
                if platform in self.config:
                    result[platform] = {
                        'status': 'scheduled',
                        'schedule_time': schedule_time,
                        'post_id': f'{platform}_scheduled_123456789'
                    }
            
            return result if len(platforms) > 1 else result.get(platforms[0], {'status': 'error', 'error': 'Invalid platform'})
                
        except ValueError:
            return {
                'status': 'error',
                'error': 'Invalid datetime format. Use YYYY-MM-DD HH:MM:SS'
            }