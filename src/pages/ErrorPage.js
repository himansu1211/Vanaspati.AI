import React from "react";
import { Link } from "react-router-dom";

const ErrorPage = () => {
  return (
    <main className="error-page-container">
      <div className="error-code">404</div>
      <h1 className="error-title">You have reached uncharted territory</h1>
      <p className="error-description">
        The botanical specimen or page you were looking for doesn't exist or may have been relocated.
      </p>
      <Link to="/" className="error-btn-link">
        <button type="button" className="error-button">Return to Vanaspati.AI Home</button>
      </Link>
    </main>
  );
};

export default ErrorPage;
