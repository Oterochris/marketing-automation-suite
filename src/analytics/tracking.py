from datetime import datetime, timedelta
from typing import Dict, List
import pandas as pd

class AnalyticsTracker:
    def __init__(self, user_id: str):
        self.user_id = user_id
        
    def track_post_performance(self, post_id: str, platform: str, metrics: Dict):
        """Track engagement metrics for a post"""
        # In production, store in database
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
        """Calculate engagement rate"""
        total_engagement = metrics['likes'] + metrics['shares'] + metrics['comments']
        return (total_engagement / metrics['reach']) * 100 if metrics['reach'] > 0 else 0
    
    def analyze_best_times(self, posts: List[Dict]) -> Dict:
        """Analyze best posting times based on engagement"""
        df = pd.DataFrame(posts)
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        
        engagement_by_hour = df.groupby('hour')['engagement_rate'].mean()
        return {
            'best_times': engagement_by_hour.nlargest(3).index.tolist(),
            'avg_engagement': engagement_by_hour.to_dict()
        }