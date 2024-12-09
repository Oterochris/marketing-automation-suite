import React, { useState } from 'react';
import { BarChart2, Users, Calendar } from 'lucide-react';

export function Campaigns() {
  const [campaigns, setCampaigns] = useState([
    {
      id: 1,
      name: 'Holiday Sale 2024',
      status: 'active',
      posts: 12,
      engagement: 3500,
      startDate: '2024-12-01',
      endDate: '2024-12-31'
    }
  ]);

  return (
    <div className="p-6">
      <div className="bg-white rounded-lg shadow-lg p-6">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold">Campaigns</h2>
          <button className="bg-blue-500 text-white px-4 py-2 rounded-lg">
            Create Campaign
          </button>
        </div>

        <div className="grid gap-6">
          {campaigns.map(campaign => (
            <div key={campaign.id} className="border rounded-lg p-4">
              <div className="flex justify-between items-start">
                <div>
                  <h3 className="text-xl font-bold mb-2">{campaign.name}</h3>
                  <div className="flex space-x-4 text-sm text-gray-600">
                    <span className="flex items-center">
                      <Calendar size={16} className="mr-1" />
                      {campaign.startDate} - {campaign.endDate}
                    </span>
                    <span className="flex items-center">
                      <Users size={16} className="mr-1" />
                      {campaign.engagement} engagements
                    </span>
                  </div>
                </div>
                <span className={`px-2 py-1 rounded-full text-sm ${campaign.status === 'active' ? 'bg-green-100 text-green-800' : 'bg-gray-100'}`}>
                  {campaign.status}
                </span>
              </div>
              
              <div className="mt-4 grid grid-cols-3 gap-4">
                <div className="bg-gray-50 p-4 rounded">
                  <h4 className="text-sm text-gray-600">Posts</h4>
                  <p className="text-2xl font-bold">{campaign.posts}</p>
                </div>
                <div className="bg-gray-50 p-4 rounded">
                  <h4 className="text-sm text-gray-600">Engagement Rate</h4>
                  <p className="text-2xl font-bold">3.5%</p>
                </div>
                <div className="bg-gray-50 p-4 rounded">
                  <h4 className="text-sm text-gray-600">Reach</h4>
                  <p className="text-2xl font-bold">12.5K</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}