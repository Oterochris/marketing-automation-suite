import pytest
from src.backend.pricing import PricingConfig
from src.social_media.manager import SocialMediaManager

def test_free_tier_limits():
    config = PricingConfig.get_plan_limits('free')
    assert config['posts_per_day'] == 5
    assert config['social_accounts'] == 2

def test_pro_tier_limits():
    config = PricingConfig.get_plan_limits('pro')
    assert config['posts_per_day'] == 50
    assert config['social_accounts'] == 10

def test_enterprise_tier_limits():
    config = PricingConfig.get_plan_limits('enterprise')
    assert config['posts_per_day'] == float('inf')  # Unlimited
    assert config['social_accounts'] == float('inf')  # Unlimited

def test_account_limits():
    # Test Free tier account limits
    free_config = {'tier': 'free', 'accounts': []}
    manager = SocialMediaManager(free_config)
    
    # Try to add accounts
    for i in range(3):  # Free tier limit is 2
        result = manager.add_social_account(
            platform='twitter',
            credentials={'api_key': f'key_{i}'}
        )
        if i < 2:
            assert result['status'] == 'success'
        else:
            assert result['status'] == 'error'
            assert 'account limit reached' in result['error']