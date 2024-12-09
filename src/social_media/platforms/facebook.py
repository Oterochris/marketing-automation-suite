from facebook_sdk import GraphAPI
from .base import SocialPlatform

class FacebookPlatform(SocialPlatform):
    def __init__(self, access_token: str):
        self.api = GraphAPI(access_token)
    
    def post(self, content: str, **kwargs):
        return self.api.put_object('me', 'feed', message=content)

    def schedule_post(self, content: str, schedule_time: str, **kwargs):
        return self.api.put_object(
            'me', 'feed',
            message=content,
            scheduled_publish_time=schedule_time
        )