from typing import Dict, List
from datetime import datetime
import uuid

class ReferralProgram:
    def __init__(self):
        self.rewards = {
            'referrer': {
                'free_months': 1,  # 1 month free for referrer
                'bonus_features': ['extra_accounts', 'api_calls']
            },
            'referee': {
                'discount_percent': 20,  # 20% off first 3 months
                'trial_days': 30  # 30-day trial of Enterprise features
            }
        }
    
    def create_referral_code(self, user_id: str) -> str:
        """Generate unique referral code"""
        code = f"{user_id[:6]}-{uuid.uuid4().hex[:6]}".upper()
        # Store in database
        return code
    
    def track_referral(self, referral_code: str, new_user_id: str) -> Dict:
        """Track successful referral"""
        referral = {
            'referral_code': referral_code,
            'referrer_id': self._get_referrer_id(referral_code),
            'referee_id': new_user_id,
            'timestamp': datetime.now(),
            'status': 'pending'
        }
        # Store in database
        return referral
    
    def process_referral_reward(self, referral_id: str) -> Dict:
        """Process rewards for both referrer and referee"""
        # Apply rewards
        return {
            'referrer_reward': self.rewards['referrer'],
            'referee_reward': self.rewards['referee']
        }
    
    def get_referral_stats(self, user_id: str) -> Dict:
        """Get user's referral statistics"""
        return {
            'total_referrals': 10,  # Example
            'successful_referrals': 8,
            'pending_referrals': 2,
            'rewards_earned': {
                'free_months': 8,
                'bonus_features': ['extra_accounts', 'api_calls']
            }
        }
    
    def _get_referrer_id(self, code: str) -> str:
        # Get referrer ID from code
        return code.split('-')[0]