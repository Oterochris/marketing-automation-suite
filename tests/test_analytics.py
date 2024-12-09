import pytest
from datetime import datetime
from src.analytics.tracker import AnalyticsTracker

@pytest.fixture
def analytics_data():
    return {
        'post_id': 'test_123',
        'likes': 100,
        'shares': 50,
        'comments': 25,
        'reach': 1000
    }

def test_engagement_tracking(analytics_data):
    tracker = AnalyticsTracker('test_user')
    result = tracker.track_engagement(analytics_data)
    assert result['engagement_rate'] == 17.5  # (100+50+25)/1000 * 100

def test_performance_report(analytics_data):
    tracker = AnalyticsTracker('test_user')
    report = tracker.generate_report()
    assert 'total_engagement' in report
    assert 'best_performing_post' in report