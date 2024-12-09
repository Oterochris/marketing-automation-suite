import React, { useState } from 'react';

export function APIKeyForm({ userEmail }) {
  const [keys, setKeys] = useState({
    twitter_api_key: '',
    twitter_api_secret: '',
    linkedin_client_id: '',
    linkedin_client_secret: ''
  });

  const [status, setStatus] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('/api/store-keys', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          ...keys,
          user_email: userEmail
        })
      });

      if (response.ok) {
        setStatus('Keys stored successfully!');
      } else {
        setStatus('Failed to store keys. Please try again.');
      }
    } catch (error) {
      setStatus('Error saving keys. Please try again.');
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-6 bg-white rounded-lg shadow-lg">
      <h2 className="text-2xl font-bold mb-6">Connect Your Social Media Accounts</h2>
      
      <form onSubmit={handleSubmit} className="space-y-6">
        <div className="border-b pb-6">
          <h3 className="text-xl font-semibold mb-4">Twitter</h3>
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-1">API Key</label>
              <input
                type="text"
                value={keys.twitter_api_key}
                onChange={(e) => setKeys({...keys, twitter_api_key: e.target.value})}
                className="w-full p-2 border rounded"
                placeholder="Enter your Twitter API Key"
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">API Secret</label>
              <input
                type="password"
                value={keys.twitter_api_secret}
                onChange={(e) => setKeys({...keys, twitter_api_secret: e.target.value})}
                className="w-full p-2 border rounded"
                placeholder="Enter your Twitter API Secret"
              />
            </div>
          </div>
        </div>

        <div className="border-b pb-6">
          <h3 className="text-xl font-semibold mb-4">LinkedIn</h3>
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-1">Client ID</label>
              <input
                type="text"
                value={keys.linkedin_client_id}
                onChange={(e) => setKeys({...keys, linkedin_client_id: e.target.value})}
                className="w-full p-2 border rounded"
                placeholder="Enter your LinkedIn Client ID"
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Client Secret</label>
              <input
                type="password"
                value={keys.linkedin_client_secret}
                onChange={(e) => setKeys({...keys, linkedin_client_secret: e.target.value})}
                className="w-full p-2 border rounded"
                placeholder="Enter your LinkedIn Client Secret"
              />
            </div>
          </div>
        </div>

        {status && (
          <div className={`p-3 rounded ${status.includes('success') ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'}`}>
            {status}
          </div>
        )}

        <button
          type="submit"
          className="w-full bg-blue-500 text-white px-6 py-3 rounded-lg hover:bg-blue-600 transition-colors"
        >
          Save API Keys
        </button>
      </form>

      <div className="mt-6 text-sm text-gray-600">
        <h4 className="font-medium mb-2">How to get your API keys:</h4>
        <ul className="list-disc pl-5 space-y-2">
          <li>
            <a href="https://developer.twitter.com/en/portal/dashboard" target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline">
              Twitter Developer Portal
            </a>
            {" "}- Create a new app to get your API keys
          </li>
          <li>
            <a href="https://www.linkedin.com/developers/apps" target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline">
              LinkedIn Developer Portal
            </a>
            {" "}- Create a new application to get your Client ID and Secret
          </li>
        </ul>
      </div>
    </div>
  );
}