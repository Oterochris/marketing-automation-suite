import React from 'react';

export function Sidebar({ onNavigate, currentView }) {
  const menuItems = [
    { id: 'dashboard', label: 'Dashboard' },
    { id: 'schedule', label: 'Schedule Posts' },
    { id: 'analytics', label: 'Analytics' },
    { id: 'settings', label: 'Settings' }
  ];

  return (
    <aside className="w-64 bg-white shadow-lg">
      <div className="p-6">
        <h1 className="text-xl font-bold">Marketing Suite</h1>
      </div>
      
      <nav className="mt-6">
        {menuItems.map(item => (
          <button
            key={item.id}
            onClick={() => onNavigate(item.id)}
            className={`w-full flex items-center px-6 py-3 ${currentView === item.id ? 'bg-blue-50 text-blue-500' : ''}`}
          >
            {item.label}
          </button>
        ))}
      </nav>
    </aside>
  );
}