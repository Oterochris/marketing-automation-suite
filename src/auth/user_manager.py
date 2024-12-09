from typing import Dict, Any

class UserManager:
    def __init__(self):
        self.users = {}
    
    def add_user(self, user_id: str, api_keys: Dict[str, Any]) -> None:
        """Store a user's API keys securely"""
        # In production, these would be encrypted and stored in a secure database
        self.users[user_id] = api_keys
    
    def get_user_keys(self, user_id: str) -> Dict[str, Any]:
        """Retrieve a user's API keys"""
        return self.users.get(user_id, {})