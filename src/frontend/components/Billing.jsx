import React, { useState } from 'react';

export function Billing() {
  const [currentPlan, setCurrentPlan] = useState('pro');
  const [billingCycle, setBillingCycle] = useState('monthly');

  const plans = {
    free: {
      name: 'Free',
      price: { monthly: 0, annual: 0 },
      features: [
        '5 posts per day',
        '2 social accounts',
        'Basic analytics'
      ]
    },
    pro: {
      name: 'Pro',
      price: { monthly: 49, annual: 470 },
      features: [
        '50 posts per day',
        '10 social accounts',
        'Advanced analytics',
        'Priority support'
      ]
    },
    enterprise: {
      name: 'Enterprise',
      price: { monthly: 100, annual: 960 },
      features: [
        'Unlimited posts',
        'Unlimited accounts',
        'Custom analytics',
        'Dedicated support',
        'White labeling'
      ]
    }
  };

  const handleUpgrade = (planId) => {
    // Handle plan upgrade logic
    console.log('Upgrading to:', planId);
  };

  return (
    <div className="max-w-4xl mx-auto p-6">
      <h1 className="text-2xl font-bold mb-6">Billing & Subscription</h1>

      <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
        <div className="flex justify-between items-center mb-6">
          <div>
            <h2 className="text-lg font-medium">Current Plan: {plans[currentPlan].name}</h2>
            <p className="text-gray-600">Billing Cycle: {billingCycle}</p>
          </div>
          <div className="text-right">
            <p className="text-sm text-gray-600">Next billing date</p>
            <p className="font-medium">January 1, 2025</p>
          </div>
        </div>

        <div className="flex justify-center mb-8">
          <div className="inline-flex rounded-lg border p-1">
            <button
              onClick={() => setBillingCycle('monthly')}
              className={`px-4 py-2 rounded-lg ${billingCycle === 'monthly' ? 'bg-blue-500 text-white' : ''}`}
            >
              Monthly
            </button>
            <button
              onClick={() => setBillingCycle('annual')}
              className={`px-4 py-2 rounded-lg ${billingCycle === 'annual' ? 'bg-blue-500 text-white' : ''}`}
            >
              Annual (20% off)
            </button>
          </div>
        </div>

        <div className="grid grid-cols-3 gap-6">
          {Object.entries(plans).map(([id, plan]) => (
            <div key={id} className="border rounded-lg p-6">
              <h3 className="text-xl font-bold mb-2">{plan.name}</h3>
              <p className="text-3xl font-bold mb-4">
                ${plan.price[billingCycle]}
                <span className="text-sm font-normal text-gray-600">/{billingCycle}</span>
              </p>
              <ul className="space-y-2 mb-6">
                {plan.features.map((feature, index) => (
                  <li key={index} className="flex items-center">
                    <svg className="w-4 h-4 mr-2 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                    {feature}
                  </li>
                ))}
              </ul>
              {id !== currentPlan ? (
                <button
                  onClick={() => handleUpgrade(id)}
                  className="w-full py-2 px-4 bg-blue-500 text-white rounded hover:bg-blue-600"
                >
                  Upgrade
                </button>
              ) : (
                <button
                  disabled
                  className="w-full py-2 px-4 bg-gray-100 text-gray-500 rounded"
                >
                  Current Plan
                </button>
              )}
            </div>
          ))}
        </div>
      </div>

      <div className="bg-white rounded-lg shadow-lg p-6">
        <h2 className="text-lg font-bold mb-4">Payment Method</h2>
        <div className="border p-4 rounded-lg flex items-center justify-between">
          <div className="flex items-center">
            <div className="w-12 h-8 bg-gray-200 rounded mr-4"></div>
            <div>
              <p className="font-medium">•••• •••• •••• 4242</p>
              <p className="text-sm text-gray-600">Expires 12/25</p>
            </div>
          </div>
          <button className="text-blue-500 hover:underline">Update</button>
        </div>
      </div>
    </div>
  );
}