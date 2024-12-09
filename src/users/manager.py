from typing import Dict
import uuid

class UserManager:
    def __init__(self):
        self.users = {}
    
    def register_user(self, user_data: Dict) -> Dict:
        user_id = str(uuid.uuid4())
        self.users[user_id] = user_data
        return {
            'status': 'success',
            'user_id': user_id
        }
    
    def generate_api_keys(self, user_id: str) -> Dict:
        return {
            'api_key': f'key_{uuid.uuid4().hex[:12]}',
            'api_secret': f'secret_{uuid.uuid4().hex}'
        }