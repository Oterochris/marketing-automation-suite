import pytest
from src.payments.stripe_integration import process_payment, create_subscription
from src.payments.billing import BillingManager

@pytest.fixture
def test_payment_data():
    return {
        'user_id': 'test_user',
        'plan': 'pro',
        'amount': 4900,  # $49.00
        'currency': 'usd',
        'payment_method': 'test_card'
    }

def test_subscription_creation(test_payment_data):
    result = create_subscription(
        user_id=test_payment_data['user_id'],
        plan=test_payment_data['plan']
    )
    
    assert result['status'] == 'success'
    assert 'subscription_id' in result

def test_payment_processing(test_payment_data):
    result = process_payment(test_payment_data)
    
    assert result['status'] == 'success'
    assert result['amount'] == test_payment_data['amount']

def test_failed_payment():
    bad_payment = {
        'user_id': 'test_user',
        'plan': 'pro',
        'amount': 4900,
        'payment_method': 'invalid_card'
    }
    
    result = process_payment(bad_payment)
    assert result['status'] == 'error'
    assert 'payment failed' in result['error'].lower()