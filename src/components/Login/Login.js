import React, { useState, useEffect  } from 'react';
import axios from 'axios';
import './Login.css';



const Login = ({ onSuccess }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  
  useEffect(() => {
    document.title = 'Login Page';
  }, []);
  
  const login = async () => {
    try {
      await axios.post('http://localhost:5000/login', { username, password });
      onSuccess();
    } catch {
      setError('Invalid username or password');
    }
  };

  return (
    <div className="login-container">
      <div className="login-card">
        <h2>Login</h2>
        {error && <div className="error">{error}</div>}

        <input
          type="text"
          placeholder="Username"
          value={username}
          id="username"
          onChange={e => setUsername(e.target.value)}
          className="login-input"
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          id="password"
          onChange={e => setPassword(e.target.value)}
          className="login-input"
        />

        <button onClick={login} className="login-button">
          Login
        </button>
      </div>
    </div>
  );
};

export default Login;
