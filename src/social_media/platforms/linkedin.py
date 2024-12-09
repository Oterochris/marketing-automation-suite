from linkedin_api import Linkedin
from .base import SocialPlatform

class LinkedInPlatform(SocialPlatform):
    def __init__(self, client_id: str, client_secret: str):
        self.api = Linkedin(client_id, client_secret)
    
    def post(self, content: str, **kwargs):
        return self.api.post_share(
            text=content,
            visibility='PUBLIC'
        )