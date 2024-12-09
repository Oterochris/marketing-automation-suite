from abc import ABC, abstractmethod
from typing import Dict, Any

class SocialPlatform(ABC):
    """Base class for all social media platforms."""
    
    @abstractmethod
    def post(self, content: str, **kwargs) -> Dict[str, Any]:
        """Post content to the platform."""
        pass
    
    @abstractmethod
    def schedule_post(self, content: str, schedule_time: str, **kwargs) -> Dict[str, Any]:
        """Schedule a post for later."""
        pass
    
    @abstractmethod
    def delete_post(self, post_id: str) -> bool:
        """Delete a post."""
        pass