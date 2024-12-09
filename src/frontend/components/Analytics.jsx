import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

export function Analytics() {
  const [data, setData] = useState({
    engagement: [],
    bestTimes: [],
    platformStats: {}
  });

  useEffect(() => {
    // Fetch analytics data
    fetch('/api/analytics/dashboard')
      .then(res => res.json())
      .then(setData);
  }, []);

  return (
    <div className="space-y-8">
      <div className="bg-white p-6 rounded-lg shadow">
        <h2 className="text-xl font-bold mb-4">Engagement Over Time</h2>
        <LineChart width={800} height={400} data={data.engagement}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="likes" stroke="#8884d8" />
          <Line type="monotone" dataKey="shares" stroke="#82ca9d" />
          <Line type="monotone" dataKey="comments" stroke="#ffc658" />
        </LineChart>
      </div>

      <div className="grid grid-cols-2 gap-6">
        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-xl font-bold mb-4">Best Posting Times</h2>
          <ul className="space-y-2">
            {data.bestTimes.map((time, index) => (
              <li key={index} className="flex justify-between">
                <span>{time.hour}:00</span>
                <span>{time.engagementRate.toFixed(2)}% engagement</span>
              </li>
            ))}
          </ul>
        </div>

        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-xl font-bold mb-4">Platform Performance</h2>
          <div className="space-y-4">
            {Object.entries(data.platformStats).map(([platform, stats]) => (
              <div key={platform} className="border-b pb-4">
                <h3 className="font-semibold mb-2">{platform}</h3>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <p className="text-sm text-gray-600">Avg. Engagement</p>
                    <p className="text-lg font-bold">{stats.avgEngagement}%</p>
                  </div>
                  <div>
                    <p className="text-sm text-gray-600">Total Reach</p>
                    <p className="text-lg font-bold">{stats.totalReach.toLocaleString()}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}