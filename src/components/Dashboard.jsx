import React from 'react';

export function Dashboard() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-gray-500 text-sm">Scheduled Posts</h3>
          <p className="text-2xl font-bold">5</p>
        </div>
        
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-gray-500 text-sm">Published Posts</h3>
          <p className="text-2xl font-bold">12</p>
        </div>
        
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-gray-500 text-sm">Total Engagement</h3>
          <p className="text-2xl font-bold">3,250</p>
        </div>
        
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-gray-500 text-sm">Total Reach</h3>
          <p className="text-2xl font-bold">15,000</p>
        </div>
      </div>
    </div>
  );
}