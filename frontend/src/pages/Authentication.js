import React, { useState } from "react";
import LoginComponent from "../components/LoginComponent";
import SignupComponent from "../components/SignupComponent";
import "../css/Login.css";

const Authentication = (props) => {
  const [showLogin, setShowLogin] = useState(true);

  setTimeout(() => {
    props.alterLogin(true);
  }, 100);

  return (
    <div className="auth-container">
      <div className="auth-button">
        <button
          className={showLogin ? "active" : "deactive"}
          onClick={() => setShowLogin(true)}
        >
          Login
        </button>
        <button
          className={showLogin ? "deactive" : "active"}
          onClick={() => setShowLogin(false)}
        >
          Sign Up
        </button>
      </div>
      <div className="auth-form">
        {showLogin ? <LoginComponent /> : <SignupComponent />}
      </div>
    </div>
  );
};

export default Authentication;
