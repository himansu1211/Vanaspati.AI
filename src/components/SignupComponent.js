import React, { useState } from "react";
import "../css/Login.css";
import { useSignup } from "../hooks/useSignup";

const SignupComponent = () => {
  // const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const {signup, error, isLoading } = useSignup();

  const handleSignup =  async (e) => {
    e.preventDefault()

    await signup(email, password)
  };

  return (
    <div className="signup-container">
      <h5>New User? Signup to Continue.</h5>
      <div>
        {/* <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="input-field"
        /> */}
        <input
          type="email"
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
      <button onClick={handleSignup} className="btn-primary" disabled={isLoading}>
        Sign Up
      </button>

      {error && <div className="error">{error}</div>}
    </div>
  );
};

export default SignupComponent;
