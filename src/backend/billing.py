from fastapi import APIRouter, HTTPException
from typing import Optional
import stripe
from datetime import datetime

router = APIRouter()
stripe.api_key = 'your_stripe_secret_key'

class BillingManager:
    ANNUAL_DISCOUNT_PERCENT = 20
    
    PLANS = {
        'free': {
            'monthly': None,  # Free plan has no price IDs
            'annual': None
        },
        'pro': {
            'monthly': 'price_pro_monthly',
            'annual': 'price_pro_annual'
        },
        'enterprise': {
            'monthly': 'price_enterprise_monthly',
            'annual': 'price_enterprise_annual'
        }
    }
    
    @staticmethod
    async def create_subscription(user_id: str, plan: str, billing_cycle: str = 'monthly'):
        try:
            # Get or create customer
            customer = stripe.Customer.retrieve(user_id)
            
            # Get price ID based on plan and billing cycle
            price_id = BillingManager.PLANS[plan][billing_cycle]
            
            # Create subscription
            subscription = stripe.Subscription.create(
                customer=customer.id,
                items=[{'price': price_id}],
                payment_behavior='default_incomplete',
                expand=['latest_invoice.payment_intent']
            )
            
            return {
                'subscription_id': subscription.id,
                'client_secret': subscription.latest_invoice.payment_intent.client_secret
            }
            
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    @staticmethod
    def calculate_annual_price(monthly_price: float) -> float:
        annual_price = monthly_price * 12
        discount = annual_price * (BillingManager.ANNUAL_DISCOUNT_PERCENT / 100)
        return annual_price - discount
    
    @staticmethod
    async def handle_subscription_change(user_id: str, new_plan: str):
        try:
            # Get current subscription
            subscriptions = stripe.Subscription.list(customer=user_id, limit=1)
            
            if not subscriptions.data:
                return await BillingManager.create_subscription(user_id, new_plan)
            
            current_subscription = subscriptions.data[0]
            
            # Update subscription
            updated_subscription = stripe.Subscription.modify(
                current_subscription.id,
                items=[{
                    'id': current_subscription['items']['data'][0].id,
                    'price': BillingManager.PLANS[new_plan]['monthly']
                }]
            )
            
            return {
                'subscription_id': updated_subscription.id,
                'status': 'updated'
            }
            
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))