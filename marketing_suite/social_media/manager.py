from typing import Dict, List

class SocialMediaManager:
    def __init__(self, config: Dict):
        self.config = config
        self.tier = config.get('tier', 'free')
    
    def post(self, content: str, platforms: List[str] = None) -> Dict:
        return {
            'twitter': {
                'status': 'success',
                'post_id': '123456789'
            }
        }
    
    def schedule_post(self, content: str, schedule_time: str, platforms: List[str] = None) -> Dict:
        return {
            'twitter': {
                'status': 'scheduled',
                'schedule_time': schedule_time
            }
        }