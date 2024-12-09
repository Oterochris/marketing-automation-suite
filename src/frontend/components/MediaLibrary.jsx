import React, { useState } from 'react';
import { Upload, Image, Folder, Search } from 'lucide-react';

export function MediaLibrary() {
  const [media, setMedia] = useState([
    {
      id: 1,
      type: 'image',
      url: '/placeholder/400/300',
      name: 'product-image-1.jpg',
      folder: 'Products'
    }
  ]);

  const [currentFolder, setCurrentFolder] = useState('All');
  const [view, setView] = useState('grid');

  return (
    <div className="p-6">
      <div className="bg-white rounded-lg shadow-lg p-6">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold">Media Library</h2>
          <button className="bg-blue-500 text-white px-4 py-2 rounded-lg flex items-center">
            <Upload className="mr-2" size={20} />
            Upload Files
          </button>
        </div>

        <div className="flex space-x-4 mb-6">
          <div className="w-64 bg-gray-50 p-4 rounded-lg">
            <h3 className="font-bold mb-4">Folders</h3>
            <ul className="space-y-2">
              {['All', 'Products', 'Blog', 'Social'].map(folder => (
                <li
                  key={folder}
                  className={`flex items-center p-2 rounded cursor-pointer ${currentFolder === folder ? 'bg-blue-50' : ''}`}
                  onClick={() => setCurrentFolder(folder)}
                >
                  <Folder size={16} className="mr-2" />
                  {folder}
                </li>
              ))}
            </ul>
          </div>

          <div className="flex-1">
            <div className="grid grid-cols-4 gap-4">
              {media.map(item => (
                <div key={item.id} className="border rounded-lg p-2">
                  <img src={item.url} alt={item.name} className="rounded mb-2" />
                  <p className="text-sm truncate">{item.name}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}