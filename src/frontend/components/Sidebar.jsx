import React from 'react';
import { LayoutDashboard, Calendar, BarChart2, Settings, Users } from 'lucide-react';

export function Sidebar({ onNavigate, currentView }) {
  const menuItems = [
    { id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard },
    { id: 'schedule', label: 'Schedule Posts', icon: Calendar },
    { id: 'analytics', label: 'Analytics', icon: BarChart2 },
    { id: 'team', label: 'Team', icon: Users },
    { id: 'settings', label: 'Settings', icon: Settings },
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
            className={`w-full flex items-center space-x-2 px-6 py-3 text-gray-600 hover:bg-gray-50 ${currentView === item.id ? 'bg-gray-50 text-blue-500' : ''}`}
          >
            <item.icon size={20} />
            <span>{item.label}</span>
          </button>
        ))}
      </nav>
    </aside>
  );
}