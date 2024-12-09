import React, { useState } from 'react';

export function Settings() {
  const [settings, setSettings] = useState({
    notifications: {
      email: true,
      desktop: false,
      reports: true
    },
    platforms: {
      twitter: {
        enabled: true,
        apiKey: '****',
        apiSecret: '****'
      },
      linkedin: {
        enabled: true,
        clientId: '****',
        clientSecret: '****'
      }
    },
    timezone: 'UTC'
  });

  const [activeTab, setActiveTab] = useState('general');

  return (
    <div className="max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">Settings</h1>

      <div className="bg-white rounded-lg shadow">
        <div className="border-b">
          <nav className="flex">
            {[
              { id: 'general', label: 'General' },
              { id: 'platforms', label: 'Platforms' },
              { id: 'notifications', label: 'Notifications' },
              { id: 'team', label: 'Team Members' },
              { id: 'billing', label: 'Billing' }
            ].map(tab => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`px-4 py-2 ${activeTab === tab.id ? 'border-b-2 border-blue-500' : ''}`}
              >
                {tab.label}
              </button>
            ))}
          </nav>
        </div>

        <div className="p-6">
          {activeTab === 'general' && (
            <div className="space-y-6">
              <div>
                <h3 className="text-lg font-medium mb-2">Time Zone</h3>
                <select
                  value={settings.timezone}
                  onChange={(e) => setSettings({...settings, timezone: e.target.value})}
                  className="w-full p-2 border rounded"
                >
                  <option value="UTC">UTC</option>
                  <option value="EST">Eastern Time</option>
                  <option value="PST">Pacific Time</option>
                </select>
              </div>
            </div>
          )}

          {activeTab === 'platforms' && (
            <div className="space-y-6">
              {Object.entries(settings.platforms).map(([platform, config]) => (
                <div key={platform} className="border-b pb-6">
                  <div className="flex items-center justify-between mb-4">
                    <h3 className="text-lg font-medium capitalize">{platform}</h3>
                    <label className="flex items-center">
                      <input
                        type="checkbox"
                        checked={config.enabled}
                        onChange={(e) => setSettings({
                          ...settings,
                          platforms: {
                            ...settings.platforms,
                            [platform]: {
                              ...config,
                              enabled: e.target.checked
                            }
                          }
                        })}
                        className="mr-2"
                      />
                      Enabled
                    </label>
                  </div>

                  <div className="grid grid-cols-2 gap-4">
                    {Object.entries(config)
                      .filter(([key]) => key !== 'enabled')
                      .map(([key, value]) => (
                        <div key={key}>
                          <label className="block text-sm font-medium mb-1 capitalize">
                            {key.replace(/([A-Z])/g, ' $1').trim()}
                          </label>
                          <input
                            type="password"
                            value={value}
                            onChange={(e) => setSettings({
                              ...settings,
                              platforms: {
                                ...settings.platforms,
                                [platform]: {
                                  ...config,
                                  [key]: e.target.value
                                }
                              }
                            })}
                            className="w-full p-2 border rounded"
                          />
                        </div>
                      ))}
                  </div>
                </div>
              ))}
            </div>
          )}

          {activeTab === 'notifications' && (
            <div className="space-y-4">
              {Object.entries(settings.notifications).map(([type, enabled]) => (
                <label key={type} className="flex items-center">
                  <input
                    type="checkbox"
                    checked={enabled}
                    onChange={(e) => setSettings({
                      ...settings,
                      notifications: {
                        ...settings.notifications,
                        [type]: e.target.checked
                      }
                    })}
                    className="mr-2"
                  />
                  <span className="capitalize">{type.replace(/([A-Z])/g, ' $1').trim()}</span>
                </label>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}