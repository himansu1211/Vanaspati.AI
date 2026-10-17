import React, { useState } from "react";
import "../css/DragDrop.css";

const DragDrop = ({ onFileChange, onRemoveClicked }) => {
  const [image, setImage] = useState(null);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];

    if (!file) return;

    if (!file.type.startsWith("image/")) {
      setError("You can only upload image files");
      return;
    }

    setImage({
      file,
      preview: URL.createObjectURL(file),
    });
    setError(null);
    onFileChange(file);
  };

  const handleRemoveImage = () => {
    setImage(null);
    document.getElementById("fileInput").value = "";
  };
  

  return (
    <div className="upload-container">
      <div className="dropzone">
        <input
          type="file"
          accept="image/*"
          onChange={handleFileChange}
          className="input-file"
          id="fileInput"
        />
        {!image && (
          <React.Fragment>
            <span className="message">Drag and Drop to Upload Image</span>
            <span className="browse">or Click to Browse</span>
          </React.Fragment>
        )}
        {image && (
          <div className="image-container">
            <img src={image.preview} alt="Uploaded file" className="image" />
            <button
              type="button"
              className="remove-button"
              onClick={() => {handleRemoveImage(); onRemoveClicked()}}
            >
              &times;
            </button>
          </div>
        )}
      </div>
      {error && <span className="error">{error}</span>}
    </div>
  );
};

export default DragDrop;
