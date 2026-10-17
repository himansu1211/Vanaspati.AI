import "./App.css";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useAuthContext } from "./hooks/useAuthContext";

import Navbar from "./components/Navbar";
import HomePage from "./pages/HomePage";
import PredictionPage from "./pages/PredictionPage";
import ErrorPage from "./pages/ErrorPage";
import Authentication from "./pages/Authentication";
import PlantIdentificationGuide from "./pages/PlantIdentificationGuide";
import Footer from "./components/Footer";
import { useState } from "react";

function App() {
  const { user } = useAuthContext();
  const [onPrediction, setOnPrediction] = useState(false);
  const [onLogin, setOnLogin] = useState(false);

  const alterPrediction = (arg) => {
    setOnPrediction(arg);
  };

  const alterLogin = (arg) => {
    setOnLogin(arg);
  };
  return (
    <div className="App">
      <div className="App">
        <BrowserRouter>
          <Navbar onPrediction={onPrediction} onLogin={onLogin} />
          <div className="pages">
            <Routes>
              <Route
                path="/"
                element={
                  <HomePage
                  alterPrediction={alterPrediction}
                    alterLogin={alterLogin}
                  />
                }
              />
              <Route
                path="/authenticate"
                element={
                  user ? (
                    <PredictionPage alterPrediction={alterPrediction} />
                  ) : (
                    <Authentication alterLogin={alterLogin} />
                  )
                }
              />
              <Route
                path="/predict"
                element={
                  user ? (
                    <PredictionPage alterPrediction={alterPrediction} />
                  ) : (
                    <Authentication alterLogin={alterLogin} />
                  )
                }
              />
              <Route
                path="/plant-identification-software"
                element={<PlantIdentificationGuide />}
              />
              <Route
                path="/technology"
                element={<PlantIdentificationGuide />}
              />
              <Route
                path="/guide"
                element={<PlantIdentificationGuide />}
              />
              <Route
                path="/404"
                element={
                  user ? (
                    <ErrorPage />
                  ) : (
                    <Authentication alterLogin={alterLogin} />
                  )
                }
              />
              <Route
                path="*"
                element={
                  user ? (
                    <Navigate to="/404" />
                  ) : (
                    <Authentication alterLogin={alterLogin} />
                  )
                }
              />
            </Routes>
          </div>
          <Footer />
        </BrowserRouter>
      </div>
    </div>
  );
}

export default App;
