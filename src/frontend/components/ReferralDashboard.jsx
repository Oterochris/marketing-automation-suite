import React, { useState, useEffect } from 'react';

export function ReferralDashboard() {
  const [referralStats, setReferralStats] = useState(null);
  const [referralCode, setReferralCode] = useState('');

  useEffect(() => {
    // Fetch referral stats
    fetch('/api/referrals/stats')
      .then(res => res.json())
      .then(setReferralStats);
    
    // Get user's referral code
    fetch('/api/referrals/code')
      .then(res => res.json())
      .then(data => setReferralCode(data.code));
  }, []);

  const copyToClipboard = () => {
    navigator.clipboard.writeText(
      `Join Marketing Automation Suite using my code: ${referralCode} and get 20% off!`
    );
  };

  if (!referralStats) return <div>Loading...</div>;

  return (
    <div className="container mx-auto p-8">
      <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
        <h2 className="text-2xl font-bold mb-4">Your Referral Dashboard</h2>
        
        <div className="bg-blue-50 p-4 rounded-lg mb-6">
          <h3 className="font-semibold mb-2">Your Referral Code</h3>
          <div className="flex items-center space-x-4">
            <code className="bg-white px-4 py-2 rounded">{referralCode}</code>
            <button
              onClick={copyToClipboard}
              className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
            >
              Copy Invite Message
            </button>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div className="bg-gray-50 p-4 rounded-lg">
            <h4 className="text-gray-600">Total Referrals</h4>
            <p className="text-3xl font-bold">{referralStats.total_referrals}</p>
          </div>
          
          <div className="bg-gray-50 p-4 rounded-lg">
            <h4 className="text-gray-600">Successful Referrals</h4>
            <p className="text-3xl font-bold">{referralStats.successful_referrals}</p>
          </div>
          
          <div className="bg-gray-50 p-4 rounded-lg">
            <h4 className="text-gray-600">Pending Referrals</h4>
            <p className="text-3xl font-bold">{referralStats.pending_referrals}</p>
          </div>
          
          <div className="bg-gray-50 p-4 rounded-lg">
            <h4 className="text-gray-600">Free Months Earned</h4>
            <p className="text-3xl font-bold">{referralStats.rewards_earned.free_months}</p>
          </div>
        </div>
      </div>

      <div className="bg-white rounded-lg shadow-lg p-6">
        <h3 className="text-xl font-bold mb-4">Referral Rewards</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h4 className="font-semibold mb-2">For You (Referrer)</h4>
            <ul className="list-disc pl-5 space-y-2">
              <li>1 month free for each successful referral</li>
              <li>Extra social media accounts</li>
              <li>Bonus API calls</li>
            </ul>
          </div>
          <div>
            <h4 className="font-semibold mb-2">For Your Friends (Referee)</h4>
            <ul className="list-disc pl-5 space-y-2">
              <li>20% off first 3 months</li>
              <li>30-day trial of Enterprise features</li>
              <li>Priority onboarding support</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}