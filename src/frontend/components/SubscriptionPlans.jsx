import React from 'react';
import { loadStripe } from '@stripe/stripe-js';

const stripePromise = loadStripe('your_publishable_key');

export function SubscriptionPlans() {
  const handleSubscribe = async (priceId) => {
    const stripe = await stripePromise;
    const response = await fetch('/api/create-subscription', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ priceId })
    });
    
    const data = await response.json();
    
    // Redirect to Stripe checkout
    const result = await stripe.redirectToCheckout({
      sessionId: data.sessionId
    });
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-8 p-8">
      <div className="border rounded-lg p-6">
        <h2 className="text-xl font-bold">Free Plan</h2>
        <p className="text-3xl font-bold mt-4">$0</p>
        <ul className="mt-4 space-y-2">
          <li>5 posts per day</li>
          <li>2 social accounts</li>
          <li>Basic analytics</li>
        </ul>
        <button
          onClick={() => handleSubscribe('free_plan_price_id')}
          className="w-full mt-6 bg-blue-500 text-white px-4 py-2 rounded"
        >
          Start Free
        </button>
      </div>

      <div className="border rounded-lg p-6 bg-blue-50">
        <h2 className="text-xl font-bold">Pro Plan</h2>
        <p className="text-3xl font-bold mt-4">$49/month</p>
        <ul className="mt-4 space-y-2">
          <li>50 posts per day</li>
          <li>10 social accounts</li>
          <li>Advanced analytics</li>
          <li>Priority support</li>
        </ul>
        <button
          onClick={() => handleSubscribe('pro_plan_price_id')}
          className="w-full mt-6 bg-blue-500 text-white px-4 py-2 rounded"
        >
          Subscribe to Pro
        </button>
      </div>

      <div className="border rounded-lg p-6">
        <h2 className="text-xl font-bold">Enterprise</h2>
        <p className="text-3xl font-bold mt-4">Custom</p>
        <ul className="mt-4 space-y-2">
          <li>Unlimited posts</li>
          <li>Unlimited accounts</li>
          <li>Custom analytics</li>
          <li>Dedicated support</li>
        </ul>
        <button
          onClick={() => window.location.href = '/contact-sales'}
          className="w-full mt-6 bg-blue-500 text-white px-4 py-2 rounded"
        >
          Contact Sales
        </button>
      </div>
    </div>
  );
}