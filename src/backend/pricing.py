from typing import Dict

def get_plan_limits(tier: str) -> Dict:
    """Get limits for a specific pricing tier"""
    limits = {
        'free': {
            'posts_per_day': 5,
            'social_accounts': 2
        },
        'pro': {
            'posts_per_day': 50,
            'social_accounts': 10
        },
        'enterprise': {
            'posts_per_day': float('inf'),
            'social_accounts': float('inf')
        }
    }
    return limits.get(tier, limits['free'])