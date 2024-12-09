import React, { useState, useEffect } from 'react';
import { SchedulePost } from './SchedulePost';
import { PostsList } from './PostsList';
import { Analytics } from './Analytics';

export function Dashboard() {
  const [posts, setPosts] = useState([]);
  const [selectedTab, setSelectedTab] = useState('schedule');

  useEffect(() => {
    // Fetch scheduled posts
    fetch('/api/posts/scheduled')
      .then(res => res.json())
      .then(data => setPosts(data));
  }, []);

  return (
    <div className="container mx-auto px-4 py-8">
      <nav className="flex mb-8 space-x-4">
        <button
          onClick={() => setSelectedTab('schedule')}
          className={`px-4 py-2 rounded ${selectedTab === 'schedule' ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
        >
          Schedule Post
        </button>
        <button
          onClick={() => setSelectedTab('posts')}
          className={`px-4 py-2 rounded ${selectedTab === 'posts' ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
        >
          Scheduled Posts
        </button>
        <button
          onClick={() => setSelectedTab('analytics')}
          className={`px-4 py-2 rounded ${selectedTab === 'analytics' ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
        >
          Analytics
        </button>
      </nav>

      {selectedTab === 'schedule' && <SchedulePost />}
      {selectedTab === 'posts' && <PostsList posts={posts} />}
      {selectedTab === 'analytics' && <Analytics />}
    </div>
  );
}