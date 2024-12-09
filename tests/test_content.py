import pytest
from src.content.manager import ContentManager

@pytest.fixture
def content_data():
    return {
        'text': 'Test post content',
        'media': None,
        'schedule': '2024-12-31 12:00:00',
        'platforms': ['twitter', 'linkedin']
    }

def test_content_scheduling(content_data):
    content_mgr = ContentManager()
    result = content_mgr.schedule_content(content_data)
    assert result['status'] == 'scheduled'
    assert result['schedule_time'] == content_data['schedule']

def test_bulk_upload():
    content_mgr = ContentManager()
    posts = [
        {'text': f'Bulk post {i}'} for i in range(5)
    ]
    result = content_mgr.bulk_upload(posts)
    assert result['total_scheduled'] == 5