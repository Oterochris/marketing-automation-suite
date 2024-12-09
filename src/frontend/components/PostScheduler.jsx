import React, { useState } from 'react';

export function PostScheduler() {
  const [post, setPost] = useState({
    content: '',
    platforms: [],
    scheduledTime: '',
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    // Submit post to backend
    console.log('Scheduling post:', post);
  };

  return (
    <div className="max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">Schedule Post</h1>
      
      <form onSubmit={handleSubmit} className="space-y-6 bg-white p-6 rounded-lg shadow">
        <div>
          <label className="block text-sm font-medium mb-2">Content</label>
          <textarea
            value={post.content}
            onChange={(e) => setPost({...post, content: e.target.value})}
            className="w-full p-2 border rounded h-32"
            placeholder="What would you like to post?"
          />
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">Platforms</label>
          <div className="space-x-4">
            {['Twitter', 'LinkedIn', 'Facebook'].map(platform => (
              <label key={platform} className="inline-flex items-center">
                <input
                  type="checkbox"
                  value={platform}
                  onChange={(e) => {
                    const platforms = e.target.checked
                      ? [...post.platforms, platform]
                      : post.platforms.filter(p => p !== platform);
                    setPost({...post, platforms});
                  }}
                  className="mr-2"
                />
                {platform}
              </label>
            ))}
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">Schedule Time</label>
          <input
            type="datetime-local"
            value={post.scheduledTime}
            onChange={(e) => setPost({...post, scheduledTime: e.target.value})}
            className="w-full p-2 border rounded"
          />
        </div>

        <button
          type="submit"
          className="w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600"
        >
          Schedule Post
        </button>
      </form>
    </div>
  );
}