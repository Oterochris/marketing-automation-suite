import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

export function Dashboard() {
  const [stats, setStats] = useState({
    scheduled: 5,
    published: 12,
    engagement: 3250,
    reachTotal: 15000
  });

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Dashboard</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-gray-500 text-sm">Scheduled Posts</h3>
          <p className="text-2xl font-bold">{stats.scheduled}</p>
        </div>
        
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-gray-500 text-sm">Published Posts</h3>
          <p className="text-2xl font-bold">{stats.published}</p>
        </div>
        
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-gray-500 text-sm">Total Engagement</h3>
          <p className="text-2xl font-bold">{stats.engagement}</p>
        </div>
        
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-gray-500 text-sm">Total Reach</h3>
          <p className="text-2xl font-bold">{stats.reachTotal}</p>
        </div>
      </div>

      <div className="bg-white p-6 rounded-lg shadow">
        <h2 className="text-lg font-bold mb-4">Engagement Over Time</h2>
        <LineChart width={800} height={300} data={[
          { date: '2024-01-01', engagement: 1200 },
          { date: '2024-01-02', engagement: 1300 },
          { date: '2024-01-03', engagement: 1400 },
        ]}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="engagement" stroke="#8884d8" />
        </LineChart>
      </div>
    </div>
  );
}