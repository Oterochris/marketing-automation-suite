from typing import Dict

class PaymentManager:
    def __init__(self, config: Dict):
        self.config = config
    
    def create_subscription(self, user_id: str, plan: str) -> Dict:
        # Simulate subscription creation
        return {
            'status': 'success',
            'user_id': user_id,
            'plan': plan,
            'subscription_id': f'sub_{user_id}_{plan}'
        }
    
    def process_payment(self, payment_data: Dict) -> Dict:
        if payment_data.get('card') == 'invalid_card':
            return {
                'status': 'error',
                'error': 'Payment failed: Invalid card'
            }
        return {
            'status': 'success',
            'transaction_id': 'tx_123',
            'amount': payment_data['amount']
        }