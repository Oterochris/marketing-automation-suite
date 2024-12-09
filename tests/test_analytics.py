import pytest
from datetime import datetime
from src.analytics.tracking import AnalyticsTracker

@pytest.fixture
def test_post_data():
    return {
        'post_id': '123',
        'likes': 100,
        'shares': 50,
        'comments': 25,
        'reach': 1000,
        'engagement_rate': 17.5
    }

def test_engagement_tracking(test_post_data):
    tracker = AnalyticsTracker('test_user')
    result = tracker.track_post_performance(
        post_id=test_post_data['post_id'],
        platform='twitter',
        metrics=test_post_data
    )
    
    assert result['post_id'] == test_post_data['post_id']
    assert result['platform'] == 'twitter'
    assert 'timestamp' in result

def test_engagement_rate_calculation(test_post_data):
    tracker = AnalyticsTracker('test_user')
    rate = tracker.get_engagement_rate(test_post_data)
    expected_rate = ((test_post_data['likes'] + 
                     test_post_data['shares'] + 
                     test_post_data['comments']) / 
                    test_post_data['reach']) * 100
    
    assert rate == expected_rate