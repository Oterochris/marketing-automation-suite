import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

export function Analytics() {
  const platformData = [
    { platform: 'Twitter', posts: 15, engagement: 1200, reach: 5000 },
    { platform: 'LinkedIn', posts: 10, engagement: 800, reach: 3000 },
    { platform: 'Facebook', posts: 12, engagement: 1000, reach: 4000 }
  ];

  const timeData = [
    { time: '9 AM', engagement: 120 },
    { time: '12 PM', engagement: 300 },
    { time: '3 PM', engagement: 200 },
    { time: '6 PM', engagement: 450 },
    { time: '9 PM', engagement: 180 }
  ];

  return (
    <div className="space-y-8">
      <h1 className="text-2xl font-bold">Analytics</h1>

      {/* Platform Performance */}
      <div className="bg-white p-6 rounded-lg shadow">
        <h2 className="text-lg font-bold mb-4">Platform Performance</h2>
        <BarChart width={800} height={300} data={platformData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="platform" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="posts" fill="#8884d8" name="Posts" />
          <Bar dataKey="engagement" fill="#82ca9d" name="Engagement" />
          <Bar dataKey="reach" fill="#ffc658" name="Reach" />
        </BarChart>
      </div>

      {/* Best Posting Times */}
      <div className="bg-white p-6 rounded-lg shadow">
        <h2 className="text-lg font-bold mb-4">Best Posting Times</h2>
        <BarChart width={800} height={300} data={timeData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="time" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="engagement" fill="#8884d8" name="Engagement" />
        </BarChart>
      </div>

      {/* Detailed Stats */}
      <div className="grid grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-lg font-bold mb-4">Top Performing Post</h3>
          <div className="border-l-4 border-blue-500 pl-4">
            <p className="text-gray-600">"Excited to announce our new feature launch! #tech #innovation"</p>
            <div className="mt-2 text-sm text-gray-500">
              <p>Platform: Twitter</p>
              <p>Engagement: 1,234</p>
              <p>Reach: 5,678</p>
            </div>
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-lg font-bold mb-4">Best Hashtags</h3>
          <div className="flex flex-wrap gap-2">
            {['#tech', '#innovation', '#startup', '#growth', '#marketing'].map(tag => (
              <span key={tag} className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm">
                {tag}
              </span>
            ))}
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-lg font-bold mb-4">Audience Growth</h3>
          <div className="space-y-4">
            <div>
              <p className="text-sm text-gray-500">Last 7 Days</p>
              <p className="text-xl font-bold">+234</p>
            </div>
            <div>
              <p className="text-sm text-gray-500">Last 30 Days</p>
              <p className="text-xl font-bold">+1,234</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}