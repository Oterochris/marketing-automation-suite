import React from 'react';

export function PricingTable() {
  const annualDiscount = 20; // 20% off for annual plans

  const calculateAnnualPrice = (monthlyPrice) => {
    const annualPrice = monthlyPrice * 12;
    const discountedPrice = annualPrice * (1 - annualDiscount/100);
    return discountedPrice.toFixed(2);
  };

  return (
    <div className="container mx-auto p-8">
      <div className="flex justify-end mb-4">
        <div className="bg-blue-100 p-2 rounded">
          <span className="text-blue-800">
            Save {annualDiscount}% with annual billing
          </span>
        </div>
      </div>

      <table className="w-full border-collapse">
        <thead>
          <tr className="bg-gray-50">
            <th className="p-4 border">Features</th>
            <th className="p-4 border">Free</th>
            <th className="p-4 border">Pro</th>
            <th className="p-4 border bg-blue-50">Enterprise</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td className="p-4 border font-bold" colSpan="4">Pricing</td>
          </tr>
          <tr>
            <td className="p-4 border">Monthly Billing</td>
            <td className="p-4 border">$0</td>
            <td className="p-4 border">$49</td>
            <td className="p-4 border">$100</td>
          </tr>
          <tr>
            <td className="p-4 border">Annual Billing</td>
            <td className="p-4 border">$0</td>
            <td className="p-4 border">${calculateAnnualPrice(49)}/year</td>
            <td className="p-4 border">${calculateAnnualPrice(100)}/year</td>
          </tr>
          <tr>
            <td className="p-4 border font-bold" colSpan="4">Core Features</td>
          </tr>
          <tr>
            <td className="p-4 border">Social Accounts</td>
            <td className="p-4 border">2</td>
            <td className="p-4 border">10</td>
            <td className="p-4 border">Unlimited</td>
          </tr>
          <tr>
            <td className="p-4 border">Posts per Day</td>
            <td className="p-4 border">5</td>
            <td className="p-4 border">50</td>
            <td className="p-4 border">Unlimited</td>
          </tr>
          <tr>
            <td className="p-4 border">Analytics</td>
            <td className="p-4 border">Basic</td>
            <td className="p-4 border">Advanced</td>
            <td className="p-4 border">Custom</td>
          </tr>
          <tr>
            <td className="p-4 border font-bold" colSpan="4">Enterprise Features</td>
          </tr>
          <tr>
            <td className="p-4 border">Bulk Post Scheduler</td>
            <td className="p-4 border">❌</td>
            <td className="p-4 border">❌</td>
            <td className="p-4 border">✓</td>
          </tr>
          <tr>
            <td className="p-4 border">Team Collaboration</td>
            <td className="p-4 border">❌</td>
            <td className="p-4 border">❌</td>
            <td className="p-4 border">✓</td>
          </tr>
          <tr>
            <td className="p-4 border">White Labeling</td>
            <td className="p-4 border">❌</td>
            <td className="p-4 border">❌</td>
            <td className="p-4 border">✓</td>
          </tr>
          <tr>
            <td className="p-4 border">Crisis Detection</td>
            <td className="p-4 border">❌</td>
            <td className="p-4 border">❌</td>
            <td className="p-4 border">✓</td>
          </tr>
          <tr>
            <td className="p-4 border">Unified Social Inbox</td>
            <td className="p-4 border">❌</td>
            <td className="p-4 border">❌</td>
            <td className="p-4 border">✓</td>
          </tr>
          <tr>
            <td className="p-4 border">API Access</td>
            <td className="p-4 border">❌</td>
            <td className="p-4 border">Basic</td>
            <td className="p-4 border">Full</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}