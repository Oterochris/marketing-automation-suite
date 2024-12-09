from typing import Dict, List
from datetime import datetime

class ContentManager:
    def __init__(self):
        self.scheduled_posts = []
    
    def schedule_content(self, content_data: Dict) -> Dict:
        post_id = f'post_{len(self.scheduled_posts) + 1}'
        self.scheduled_posts.append({
            'id': post_id,
            **content_data
        })
        return {
            'status': 'scheduled',
            'post_id': post_id,
            'schedule_time': content_data['schedule']
        }
    
    def bulk_upload(self, posts: List[Dict]) -> Dict:
        for post in posts:
            self.schedule_content(post)
        return {
            'status': 'success',
            'total_scheduled': len(posts)
        }