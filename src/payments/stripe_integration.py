from typing import Dict

def process_payment(payment_data: Dict) -> Dict:
    # Simulate payment processing
    if payment_data.get('payment_method') == 'invalid_card':
        return {
            'status': 'error',
            'error': 'Payment failed: Invalid card'
        }
    
    return {
        'status': 'success',
        'amount': payment_data['amount'],
        'transaction_id': 'test_transaction'
    }

def create_subscription(user_id: str, plan: str) -> Dict:
    # Simulate subscription creation
    return {
        'status': 'success',
        'subscription_id': f'sub_{user_id}_{plan}',
        'plan': plan,
        'start_date': '2024-01-01'
    }