import stripe
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()
stripe.api_key = 'your_stripe_secret_key'

@router.post('/create-subscription')
async def create_subscription(price_id: str, db: Session = Depends(get_db)):
    try:
        # Create a customer and subscription in Stripe
        subscription = stripe.Subscription.create(
            customer='customer_id',
            items=[{'price': price_id}],
            payment_behavior='default_incomplete',
            expand=['latest_invoice.payment_intent'],
        )
        
        return {
            'subscriptionId': subscription.id,
            'clientSecret': subscription.latest_invoice.payment_intent.client_secret
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))