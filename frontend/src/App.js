import React, { useEffect, useState } from 'react';
import './App.css'

function App() {
  const [serverTime, setServerTime] = useState(null);
  const [userTime, setUserTime] = useState(null);

  useEffect(() => {
    const fetchServerTime = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api');
        const data = await response.json();
        setServerTime(data.serverTime);
      } catch (error) {
        console.error('Error fetching server time:', error);
      }
    };

    const interval = setInterval(fetchServerTime, 1000);

    const updateUserTime = () => {
      setUserTime(new Date().toLocaleString());
    };
    updateUserTime();
    const userTimeInterval = setInterval(updateUserTime, 1000);

    return () => {
      clearInterval(interval);
      clearInterval(userTimeInterval);
    };
  }, []);

  return (
    <div className='info'>
      <h2>Server Time (JST):</h2>
      <div id="server-time">{serverTime ? serverTime.toLocaleString() : 'Loading...'}</div>
      <h2>User Time:</h2>
      <div id="user-time">{userTime}</div>
    </div>
  );
}

export default App;