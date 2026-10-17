import React, { useState } from "react";
import "../index.css";

const Dropdowns = (props) => {
  const plantDiseaseData = props.plantDiseaseData;
  const [selectedPlant, setSelectedPlant] = useState("");
  const [selectedDisease, setSelectedDisease] = useState("");

  const handlePlantChange = (event) => {
    const selectedValue = event.target.value;
    setSelectedPlant(selectedValue);
    setSelectedDisease(""); // Reset the disease selection when the plant changes
    props.onPlantChange(selectedValue);
  };

  const handleDiseaseChange = (event) => {
    const selectedValue = event.target.value;
    setSelectedDisease(selectedValue);
    props.onDiseaseChange(selectedValue);
  };

  const getDiseaseOptions = () => {
    if (selectedPlant) {
      const selectedPlantData = plantDiseaseData[selectedPlant];
      return selectedPlantData.diseases.map((disease, index) => (
        <option key={index} value={disease}>
          {disease}
        </option>
      ));
    } else {
      return (
        <option value="" disabled>
          Select a Plant first
        </option>
      );
    }
  };

  return (
    <div className="options-container">
      <div className="selectField">
        <label className="selectField-label">Plant Name</label>
        <select
          className="selectField-select"
          value={selectedPlant}
          onChange={handlePlantChange}
        >
          <option value="">Select a Plant</option>
          {Object.keys(plantDiseaseData).map((plantKey, index) => (
            <option key={index} value={plantKey}>
              {plantDiseaseData[plantKey].name}
            </option>
          ))}
        </select>
      </div>

      <div className="selectField">
        <label className="selectField-label">Disease Name</label>
        <select
          className="selectField-select"
          value={selectedDisease}
          onChange={handleDiseaseChange}
          disabled={!selectedPlant}
        >
          <option value="">Select a Disease</option>
          {getDiseaseOptions()}
        </select>
      </div>
    </div>
  );
}

export default Dropdowns;