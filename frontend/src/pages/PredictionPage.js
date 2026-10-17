import React, { useState } from "react";
import axios from "axios";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

import DragDrop from "../components/DragDrop";
import DiseaseDetails from "../components/DiseaseDetails";
import { useAuthContext } from "../hooks/useAuthContext";
import Dropdowns from "../components/Dropdowns";
import PlantCareAssistant from "../components/PlantCareAssistant";

const plantDiseaseData = {
  plant1: {
    name: "Apple",
    diseases: ["Apple Scab", "Apple Black Rot", "Apple Cedar/Apple Rust"],
  },
  plant2: {
    name: "Cherry",
    diseases: ["Cherry Powdery Mildew"],
  },
  plant3: {
    name: "Corn",
    diseases: [
      "Corn Cercospora Leaf Spot",
      "Corn Common Rust",
      "Corn Northern Leaf Blight",
    ],
  },
  plant4: {
    name: "Grapes",
    diseases: [
      "Grape Black Rot",
      "Grape Esca (Black Measles)",
      "Grape Leaf Blight",
    ],
  },
  plant5: {
    name: "Orange",
    diseases: ["Orange Haunglongbing (Citrus Greening)"],
  },
  plant6: {
    name: "Peach",
    diseases: ["Peach Bacterial Spot"],
  },
  plant7: {
    name: "Pepper Bell",
    diseases: ["Pepper Bell Bacterial Spot"],
  },
  plant8: {
    name: "Potato",
    diseases: ["Potato Early Blight", "Potato Late Blight"],
  },
  plant9: {
    name: "Squash",
    diseases: ["Squash Powdery Mildew"],
  },
  plant10: {
    name: "Strawberry",
    diseases: ["Strawberry Leaf Scorch"],
  },
  plant11: {
    name: "Tomato",
    diseases: [
      "Tomato Bacterial Spot",
      "Tomato Early Blight",
      "Tomato Late Blight",
      "Tomato Leaf Mold",
      "Tomato Septoria Leaf Spot",
      "Tomato Spider Mites",
      "Tomato Target Spot",
      "Tomato Yellow Leaf Curl",
      "Tomato Mosaic Virus",
    ],
  },
  plant12: {
    name: "Rose",
    diseases: [
      "Rose Black Spot",
      "Rose Powdery Mildew",
      "Rose Rust",
      "Rose Healthy"
    ],
  },
  plant13: {
    name: "Lady's Finger (Okra)",
    diseases: ["Yellow Vein Mosaic of Bhendi", "Lady's Finger Cercospora Leaf Spot"],
  },
  plant14: {
    name: "Brinjal (Eggplant)",
    diseases: ["Little Leaf of Brinjal", "Brinjal Bacterial Wilt"],
  },
  plant15: {
    name: "Carrot",
    diseases: ["Black Rot of Carrots", "Root Rot of Carrot", "Aster Yellows"],
  },
  plant16: {
    name: "Wheat & Cereals",
    diseases: ["Loose Smut of Wheat", "Wheat Bunt", "Fusarium Head Blight"],
  },
  plant17: {
    name: "Groundnut (Peanut)",
    diseases: ["Tikka Disease of Groundnut"],
  },
  plant18: {
    name: "Cucumber & Cucurbits",
    diseases: ["Downy Mildew of Cucurbits", "Powdery Mildew", "Gummy Stem Blight"],
  },
  plant19: {
    name: "Pomegranate",
    diseases: ["Pomegranate Bacterial Blight", "Pomegranate Wilt Complex"],
  },
  plant20: {
    name: "Tea",
    diseases: ["Red Rust of Tea"],
  },
};

const plantDiseaseNamesMapping = {
  "Apple Scab": "Apple___Apple_scab",
  "Apple Black Rot": "Apple___Black_rot",
  "Apple Cedar/Apple Rust": "Apple___Cedar_apple_rust",
  "Cherry Powdery Mildew": "Cherry___Powdery_mildew",
  "Corn Cercospora Leaf Spot": "Corn___Cercospora_leaf_spot Gray_leaf_spot",
  "Corn Common Rust": "Corn___Common_rust",
  "Corn Northern Leaf Blight": "Corn___Northern_Leaf_Blight",
  "Grape Black Rot": "Grape___Black_rot",
  "Grape Esca (Black Measles)": "Grape___Esca_(Black_Measles)",
  "Grape Leaf Blight": "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
  "Orange Haunglongbing (Citrus Greening)":
    "Orange___Haunglongbing_(Citrus_greening)",
  "Peach Bacterial Spot": "Peach___Bacterial_spot",
  "Pepper Bell Bacterial Spot": "Pepper,_bell___Bacterial_spot",
  "Potato Early Blight": "Potato___Early_blight",
  "Potato Late Blight": "Potato___Late_blight",
  "Squash Powdery Mildew": "Squash___Powdery_mildew",
  "Strawberry Leaf Scorch": "Strawberry___Leaf_scorch",
  "Tomato Bacterial Spot": "Tomato___Bacterial_spot",
  "Tomato Early Blight": "Tomato___Early_blight",
  "Tomato Late Blight": "Tomato___Late_blight",
  "Tomato Leaf Mold": "Tomato___Leaf_Mold",
  "Tomato Septoria Leaf Spot": "Tomato___Septoria_leaf_spot",
  "Tomato Spider Mites": "Tomato___Spider_mites Two-spotted_spider_mite",
  "Tomato Target Spot": "Tomato___Target_Spot",
  "Tomato Yellow Leaf Curl": "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
  "Tomato Mosaic Virus": "Tomato___Tomato_mosaic_virus",
  "Rose Black Spot": "Rose___Black_spot",
  "Rose Powdery Mildew": "Rose___Powdery_mildew",
  "Rose Rust": "Rose___Rust",
  "Rose Healthy": "Rose___healthy",
  "Yellow Vein Mosaic of Bhendi": "Yellow Vein Mosaic of Bhendi (Okra)",
  "Lady's Finger Cercospora Leaf Spot": "Cercospora leaf spot",
  "Little Leaf of Brinjal": "Little Leaf of Brinjal",
  "Brinjal Bacterial Wilt": "Bacterial Wilt (Brown Rot / Stewart's Wilt / Southern Wilt)",
  "Black Rot of Carrots": "Black rot of carrots",
  "Root Rot of Carrot": "Root rot of carrot",
  "Aster Yellows": "Aster Yellows",
  "Loose Smut of Wheat": "Loose smut of wheat",
  "Wheat Bunt": "Wheat bunt",
  "Fusarium Head Blight": "Fusarium head blight or scab",
  "Tikka Disease of Groundnut": "Tikka Disease of Groundnut (Early and Late Leaf Spot)",
  "Downy Mildew of Cucurbits": "Downy mildew of Cucurbits",
  "Powdery Mildew": "Powdery mildew",
  "Gummy Stem Blight": "Gummy stem blight",
  "Pomegranate Bacterial Blight": "Pomegranate bacterial blight",
  "Pomegranate Wilt Complex": "Pomegranate wilt complex",
  "Red Rust of Tea": "Red Rust of Tea",
};

const PredictionPage = (props) => {
  const alterPrediction = props.alterPrediction;

  setTimeout(() => {
    alterPrediction(true);
  }, 100);

  const [file, setFile] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [predictedDiseaseData, setPredictedDiseaseData] = useState(null);
  const [healthy, setHealthy] = useState(null);

  const [dragDrop, setDragDrop] = useState(true);

  const [selectedPlant, setSelectedPlant] = useState("");
  const [selectedDisease, setSelectedDisease] = useState("");

  const { user } = useAuthContext();

  const alterDragDrop = (arg) => {
    setDragDrop(arg);
    setFile(null);
    setPrediction(null);
    setPredictedDiseaseData(null);
    setHealthy(null);
    setSelectedPlant(null);
    setSelectedDisease(null);
  };

  const handleFileChange = (file) => {
    setFile(file);
    setPrediction(null);
  };

  const handleRemoveClicked = () => {
    setFile(null);
    setPrediction(null);
    setPredictedDiseaseData(null);
    setHealthy(null);
  };

  const handlePlantChange = (selectedValue) => {
    setSelectedPlant(selectedValue);
    setSelectedDisease(null);
  };

  const handleDiseaseChange = (selectedValue) => {
    setSelectedDisease(selectedValue);
  };

  const handleFormSubmit = async (e) => {
    e.preventDefault();

    if (!file) {
      notifyImageSelectError();
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const headers = {
      "Content-Type": "multipart/form-data",
    };
    if (user && user.token) {
      headers["Authorization"] = `Bearer ${user.token}`;
    }

    try {
      const response = await axios.post(
        "http://localhost:10000/predict",
        formData,
        { headers }
      );
      const data = response.data;
      setPrediction(data);

      // Handling non-leaf background cases
      if (data.class_name === "Background_without_leaves") {
        notifyImageContentError();
        return;
      }

      // Check if healthy specimen
      if (data.class_name && data.class_name.includes("healthy")) {
        setHealthy(data.plant_name || data.class_name.split("___")[0].replace(/_/g, ' '));
      } else {
        setHealthy(null);
      }

      // Fetch full rich disease details
      try {
        const diseaseDetailsResponse = await fetch(
          `http://localhost:4000/api/diseases/details?name=${encodeURIComponent(data.class_name)}&plant_identified=true&confidence=${encodeURIComponent(data.confidence || 0)}`
        );
        if (diseaseDetailsResponse.ok) {
          const diseaseDetailsData = await diseaseDetailsResponse.json();
          setPredictedDiseaseData(diseaseDetailsData);
        } else {
          throw new Error("Backend response not ok");
        }
      } catch (fetchErr) {
        console.warn("Backend fetch failed, generating resilient local diagnosis details:", fetchErr);
        const derivedPlant = data.plant_name || data.class_name.split("___")[0].replace(/_/g, ' ');
        const derivedCondition = data.class_name.includes("___") ? data.class_name.split("___")[1].replace(/_/g, ' ') : data.class_name;
        const isHealthy = data.class_name.includes("healthy");
        
        setPredictedDiseaseData({
          idName: data.class_name,
          plant_name: derivedPlant,
          plant_identified: true,
          disease_name: isHealthy ? `Healthy ${derivedPlant} Specimen` : `${derivedPlant} - ${derivedCondition}`,
          scientific_name: `${derivedPlant} spp.`,
          pathogen_type: isHealthy ? "None (Optimum Foliar Health)" : "Pathological Plant Condition",
          severity: isHealthy ? "Optimal Health (Zero Pathology)" : "Moderate",
          disease_symptoms: [isHealthy ? "Vigorous, unblemished photosynthetic foliage with clean cellular structure." : `Observed foliar lesions and symptoms characteristic of ${derivedCondition}.`],
          disease_causes: ["Environmental conditions, moisture, and ambient temperature thresholds."],
          disease_prevention: ["Maintain drip root irrigation and ensure adequate canopy airflow."],
          fertilizer_recommendation: ["Apply balanced N-P-K nutrition with supplemental potassium for cell wall immunity."],
          pesticides_and_fungicides: [isHealthy ? "No chemical intervention needed for healthy specimens." : "Apply protective organic bio-fungicide or copper spray."],
          organic_remedies: ["Cold-pressed neem oil spray or potassium bicarbonate solution."],
          disease_control: ["Inspect crops weekly and remove any heavily discolored outer foliage."]
        });
      }
    } catch (error) {
      console.error(error);
      notifyPredictError();
    }
  };

  const handleChoiceFormSubmit = async (e) => {
    e.preventDefault();

    if (!selectedPlant || !selectedDisease) {
      notifyChoiceSelectError();
      setPrediction(null);
      setPredictedDiseaseData(null);
      setHealthy(null);
      return;
    }

    let name = plantDiseaseNamesMapping[selectedDisease] || selectedDisease;

    const diseaseDetailsResponse = await fetch(
      `http://localhost:4000/api/diseases/details?name=${encodeURIComponent(name)}`
    );


    const diseaseDetailsData = await diseaseDetailsResponse.json();

    if (diseaseDetailsResponse.ok) {
      setPredictedDiseaseData(diseaseDetailsData);
      setHealthy(name.includes("healthy") ? selectedPlant : null);
      setPrediction({ class_name: name, confidence: 1.0 });
    } else {
      console.log("Error fetching the data.");
      notifyFetchError();
    }
  };

  const notifyChoiceSelectError = () =>
    toast.warn("Please select the disease name!", {
      position: "top-right",
      autoClose: 3000,
      theme: "light",
    });

  const notifyImageSelectError = () =>
    toast.warn("Please select an image to upload!", {
      position: "top-right",
      autoClose: 3000,
      theme: "light",
    });

  const notifyImageContentError = () =>
    toast.warn(
      "Please upload an image that contains leaves or flowers of the plant!",
      {
        position: "top-right",
        autoClose: 3000,
        theme: "light",
      }
    );

  const notifyPredictError = () =>
    toast.error("Error communicating with AI Vision model!", {
      position: "top-right",
      autoClose: 3000,
      theme: "light",
    });

  const notifyFetchError = () =>
    toast.error("Could not fetch diagnosis details!", {
      position: "top-right",
      autoClose: 3000,
      theme: "light",
    });


  return (
    <>
      <ToastContainer
        position="top-right"
        autoClose={3000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
        theme="light"
      />
      <div className="predictionpage-container">
        <div className="predict-container">
          <div className="predict-options">
            <button
              className={
                dragDrop ? "active predict-btn" : "deactive predict-btn"
              }
              id="predict-btn-1"
              onClick={() => alterDragDrop(true)}
            >
              Upload Image
            </button>
            <button
              className={
                !dragDrop ? "active predict-btn" : "deactive predict-btn"
              }
              id="predict-btn-2"
              onClick={() => alterDragDrop(false)}
            >
              Disease Name
            </button>
          </div>
          <div className="predict-choice">
            {dragDrop && (
              <div className="photo-tips-card" style={{ background: "rgba(0, 0, 0, 0.2)", border: "1px solid rgba(255, 255, 255, 0.08)", borderRadius: "8px", padding: "12px 14px", marginBottom: "14px", fontSize: "0.85rem", color: "#cbd5e1", textAlign: "left" }}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                  <strong style={{ color: "var(--primary-light)" }}>📸 Photography Tips for 100% Accuracy:</strong>
                  <a href="/plant-identification-software" style={{ color: "#93c5fd", textDecoration: "none", fontSize: "0.8rem", fontWeight: 600 }}>AI Guide →</a>
                </div>
                <ul style={{ margin: "6px 0 0 16px", padding: 0, lineHeight: 1.5, color: "#94a3b8" }}>
                  <li>Use bright natural daylight; keep the leaf blade or flower in close focus.</li>
                  <li>Ensure distinctive leaf margins, serrations, and vein patterns are sharp.</li>
                  <li>For lesions, capture both the disease spot boundary and adjacent green tissue.</li>
                </ul>
              </div>
            )}
            {dragDrop && (
              <form onSubmit={handleFormSubmit}>
                <DragDrop
                  onFileChange={handleFileChange}
                  onRemoveClicked={handleRemoveClicked}
                />
                <button type="submit" className="submit">
                  Predict Pathology
                </button>
              </form>
            )}
            {!dragDrop && (
              <form onSubmit={handleChoiceFormSubmit}>
                <Dropdowns
                  plantDiseaseData={plantDiseaseData}
                  onPlantChange={handlePlantChange}
                  onDiseaseChange={handleDiseaseChange}
                />
                <button type="submit" className="submit">
                  View Cure & Details
                </button>
              </form>
            )}
          </div>
        </div>

        {healthy && (
          <div className="prediction-result" style={{ marginBottom: "20px", maxWidth: "840px" }}>
            <h4 style={{ color: "var(--primary-light)", fontSize: "1.2rem", fontWeight: 700 }}>
              🌿 Specimen Diagnosis: The uploaded {healthy} specimen appears healthy and vigorous!
            </h4>
            <p style={{ color: "#cbd5e1", marginTop: "6px" }}>
              Below is the comprehensive maintenance guide, fertilizer recommendations, and preventive protocol for your {healthy} specimen:
            </p>
          </div>
        )}

        {prediction && predictedDiseaseData && (
          <div className="disease-result">
            <DiseaseDetails
              key={predictedDiseaseData._id || predictedDiseaseData.idName}
              predictedDiseaseData={predictedDiseaseData}
            />
          </div>
        )}

        {/* Interactive PLLaMa Plant Science Consultant */}
        <div style={{ maxWidth: "840px", width: "100%", margin: "24px auto 40px" }}>
          <PlantCareAssistant
            currentPlant={prediction?.plant_name || healthy}
            currentCondition={predictedDiseaseData?.disease_name}
          />
        </div>
      </div>
    </>
  );
};

export default PredictionPage;
