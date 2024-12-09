from instagram_private_api import Client
from .base import SocialPlatform

class InstagramPlatform(SocialPlatform):
    def __init__(self, username: str, password: str):
        self.api = Client(username, password)
    
    def post(self, content: str, media_url: str = None, **kwargs):
        if media_url:
            return self.api.post_photo(media_url, caption=content)
        return self.api.post_comment('self', content)