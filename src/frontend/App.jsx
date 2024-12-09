import React from 'react';
import { Sidebar } from './components/Sidebar';
import { Dashboard } from './components/Dashboard';
import { PostScheduler } from './components/PostScheduler';
import { Analytics } from './components/Analytics';

export default function App() {
  const [currentView, setCurrentView] = React.useState('dashboard');

  const renderView = () => {
    switch(currentView) {
      case 'dashboard':
        return <Dashboard />;
      case 'schedule':
        return <PostScheduler />;
      case 'analytics':
        return <Analytics />;
      default:
        return <Dashboard />;
    }
  };

  return (
    <div className="flex h-screen bg-gray-100">
      <Sidebar onNavigate={setCurrentView} currentView={currentView} />
      <main className="flex-1 overflow-y-auto p-8">
        {renderView()}
      </main>
    </div>
  );
}