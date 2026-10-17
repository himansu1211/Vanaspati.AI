import { Link } from "react-router-dom";
import { useLogout } from "../hooks/useLogout";
import { useAuthContext } from "../hooks/useAuthContext";

const Navbar = (props) => {
  const { logout } = useLogout();
  const { user } = useAuthContext();

  const handleClick = () => {
    logout();
  };

  return (
    <header className="navbar">
      <div className="nav-title">
        <Link to="/" className="brand-link">
          <h1 className="title">Vanaspati<span>.AI</span></h1>
          <h3>From Diagnosis To Solution</h3>
        </Link>
      </div>
      <nav>
        {user && (
          <div className="nav-links">
            <li>
              <span className="user-badge">
                <span className="greetingsText">Welcome, </span>
                <span className="userIdText">{user.email}</span>
              </span>
            </li>
            <li>
              <Link to="/plant-identification-software">AI Guide</Link>
            </li>
            {props.onPrediction && (
              <li>
                <Link to="/">Home</Link>
              </li>
            )}
            {!props.onPrediction && (
              <li>
                <Link to="/predict">Predict</Link>
              </li>
            )}
            <li>
              <button className="logout-button" onClick={handleClick}>
                Log Out
              </button>
            </li>
          </div>
        )}
        {!user && (
          <div className="nav-links">
            <li>
              <Link to="/plant-identification-software">AI Guide</Link>
            </li>
            {props.onLogin && (
              <li>
                <Link to="/">Home</Link>
              </li>
            )}
            {!props.onLogin && (
              <li>
                <Link to="/authenticate">Login / Sign Up</Link>
              </li>
            )}
          </div>
        )}
      </nav>
    </header>
  );
};

export default Navbar;
