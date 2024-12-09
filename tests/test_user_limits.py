import pytest
from src.backend.pricing import get_plan_limits
from src.social_media.manager import SocialMediaManager

def test_free_tier_limits():
    limits = get_plan_limits('free')
    assert limits['posts_per_day'] == 5
    assert limits['social_accounts'] == 2

def test_pro_tier_limits():
    limits = get_plan_limits('pro')
    assert limits['posts_per_day'] == 50
    assert limits['social_accounts'] == 10

def test_enterprise_tier_limits():
    limits = get_plan_limits('enterprise')
    assert limits['posts_per_day'] == float('inf')  # Unlimited
    assert limits['social_accounts'] == float('inf')  # Unlimited