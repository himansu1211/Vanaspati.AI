import React, { useState } from "react";
import "../css/Login.css";

import { useLogin } from "../hooks/useLogin";

const LoginComponent = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const {login, error, isLoading } = useLogin();

  const handleLogin = async (e) => {
    e.preventDefault();

    await login(email, password);
  };

  return (
    <div className="login-container">
      <h5>Already a User? Login to Continue.</h5>
      <div>
        <input
          type="text"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="input-field"
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="input-field"
        />
      </div>
      <button onClick={handleLogin} className="btn-primary" disabled={isLoading}>
        Login
      </button>

      {error && <div className="error">{error}</div>}
    </div>
  );
};

export default LoginComponent;
