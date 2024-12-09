import React, { useState } from 'react';

export function Register({ onRegister }) {
  const [userData, setUserData] = useState({
    email: '',
    password: '',
    confirmPassword: '',
    companyName: ''
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    if (userData.password === userData.confirmPassword) {
      onRegister(userData);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="max-w-md w-full space-y-8 p-8 bg-white rounded-lg shadow">
        <div>
          <h2 className="text-3xl font-bold text-center">Create Account</h2>
          <p className="mt-2 text-center text-gray-600">Start automating your social media</p>
        </div>

        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700">Email</label>
              <input
                type="email"
                value={userData.email}
                onChange={(e) => setUserData({...userData, email: e.target.value})}
                className="mt-1 w-full p-3 border rounded"
                required
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">Company Name</label>
              <input
                type="text"
                value={userData.companyName}
                onChange={(e) => setUserData({...userData, companyName: e.target.value})}
                className="mt-1 w-full p-3 border rounded"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">Password</label>
              <input
                type="password"
                value={userData.password}
                onChange={(e) => setUserData({...userData, password: e.target.value})}
                className="mt-1 w-full p-3 border rounded"
                required
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">Confirm Password</label>
              <input
                type="password"
                value={userData.confirmPassword}
                onChange={(e) => setUserData({...userData, confirmPassword: e.target.value})}
                className="mt-1 w-full p-3 border rounded"
                required
              />
            </div>
          </div>

          <button
            type="submit"
            className="w-full py-3 px-4 bg-blue-600 text-white rounded hover:bg-blue-700"
          >
            Create Account
          </button>

          <p className="text-center text-sm text-gray-600">
            Already have an account?{' '}
            <a href="#" className="text-blue-600 hover:underline">Sign in</a>
          </p>
        </form>
      </div>
    </div>
  );
}