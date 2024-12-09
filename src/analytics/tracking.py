from typing import Dict
from datetime import datetime

class AnalyticsTracker:
    def __init__(self, user_id: str):
        self.user_id = user_id
    
    def track_post_performance(self, post_id: str, platform: str, metrics: Dict) -> Dict:
        return {
            'post_id': post_id,
            'platform': platform,
            'likes': metrics.get('likes', 0),
            'shares': metrics.get('shares', 0),
            'comments': metrics.get('comments', 0),
            'reach': metrics.get('reach', 0),
            'timestamp': datetime.now()
        }
    
    def get_engagement_rate(self, metrics: Dict) -> float:
        total_engagement = (
            metrics.get('likes', 0) + 
            metrics.get('shares', 0) + 
            metrics.get('comments', 0)
        )
        return (total_engagement / metrics['reach']) * 100 if metrics.get('reach', 0) > 0 else 0