from enum import Enum
from typing import Dict

class PlanTier(Enum):
    FREE = 'free'
    PRO = 'pro'
    ENTERPRISE = 'enterprise'

class PricingConfig:
    PLANS = {
        PlanTier.FREE: {
            'price': 0,
            'limits': {
                'posts_per_day': 5,
                'social_accounts': 2,
                'analytics': 'basic',
            }
        },
        PlanTier.PRO: {
            'price': 49,
            'limits': {
                'posts_per_day': 50,
                'social_accounts': 10,
                'analytics': 'advanced',
            }
        },
        PlanTier.ENTERPRISE: {
            'price': 100,
            'limits': {
                'posts_per_day': float('inf'),  # unlimited
                'social_accounts': float('inf'),  # unlimited
                'analytics': 'full',
            }
        }
    }
    
    @staticmethod
    def get_plan_limits(plan: PlanTier) -> Dict:
        return PricingConfig.PLANS[plan]['limits']
    
    @staticmethod
    def get_plan_price(plan: PlanTier) -> float:
        return PricingConfig.PLANS[plan]['price']