import pytest
from src.payments.manager import PaymentManager

@pytest.fixture
def payment_config():
    return {
        'stripe_key': 'test_key',
        'plans': {
            'free': {'price': 0},
            'pro': {'price': 4900},
            'enterprise': {'price': 10000}
        }
    }

def test_subscription_creation(payment_config):
    payment_mgr = PaymentManager(payment_config)
    result = payment_mgr.create_subscription(
        user_id='test_user',
        plan='pro'
    )
    assert result['status'] == 'success'
    assert result['plan'] == 'pro'

def test_failed_payment(payment_config):
    payment_mgr = PaymentManager(payment_config)
    result = payment_mgr.process_payment({
        'amount': 4900,
        'card': 'invalid_card'
    })
    assert result['status'] == 'error'
    assert 'payment failed' in result['error'].lower()