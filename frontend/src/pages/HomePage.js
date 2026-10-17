import React from "react";
import { Link } from "react-router-dom";
import heroImage from "../images/hero-image.jpg";
import scanImage from "../images/scan.jpg";
import diagnoseImage from "../images/diagnose.jpg";
import treatmentImage from "../images/treatment.jpg";

const HomePage = (props) => {
  setTimeout(() => {
    props.alterPrediction(false);
    props.alterLogin(false);
  }, 100);

  return (
    <div className="container-homePage">
      {/* Hero Section */}
      <section className="section1 section">
        <img src={heroImage} alt="Vanaspati.AI Agricultural Field" className="hero-bg-img" />
        <div className="overlay">
          <h1>Vanaspati<span className="accent-dot">.AI</span></h1>
          <h2>From Diagnosis To Solution</h2>
          <p className="tagline">
            The Future of Botanical Health, Crop Care & Precision Agriculture
          </p>
          <div className="cta-group" style={{ display: "flex", gap: "16px", justifyContent: "center", flexWrap: "wrap" }}>
            <Link to="/authenticate">
              <button className="cta-btn">Get Started</button>
            </Link>
            <Link to="/predict">
              <button className="cta-btn secondary-btn" style={{ background: "rgba(255, 255, 255, 0.12)", border: "1px solid rgba(255, 255, 255, 0.25)" }}>
                Instant Plant Scanner
              </button>
            </Link>
          </div>
        </div>
        <div className="arrows-container" aria-hidden="true">
          <svg className="arrows">
            <path className="a1" d="M0 0 L15 16 L30 0"></path>
            <path className="a2" d="M0 15 L15 31 L30 15"></path>
            <path className="a3" d="M0 30 L15 46 L30 30"></path>
          </svg>
        </div>
      </section>

      {/* About Section */}
      <section className="section2 section">
        <div className="overlay info">
          <h2>What Is Vanaspati.AI?</h2>
          <p>
            Vanaspati.AI is an intelligent agronomy and computer vision platform that detects plant diseases in crops, vegetables, flowering botanicals (including roses), and trees. Combining multi-task deep neural networks with comprehensive agronomic research, Vanaspati.AI delivers immediate scientific diagnoses, exact fertilizer formulations, and certified biological and chemical cure protocols.
          </p>
          <h3>Connecting Agriculture and Artificial Intelligence</h3>
        </div>
        <div className="arrows-container" aria-hidden="true">
          <svg className="arrows">
            <path className="a1" d="M0 0 L15 16 L30 0"></path>
            <path className="a2" d="M0 15 L15 31 L30 15"></path>
            <path className="a3" d="M0 30 L15 46 L30 30"></path>
          </svg>
        </div>
      </section>

      {/* Key Capabilities Section */}
      <section className="section3 section">
        <div className="section-header" style={{ textAlign: "center", marginBottom: "36px" }}>
          <h2>Key Capabilities</h2>
          <p style={{ color: "#94a3b8", fontSize: "1.1rem", maxWidth: "600px", margin: "8px auto 0" }}>
            Comprehensive computer vision, plant pathology, and precision soil nutrition tools built for farmers and gardeners.
          </p>
        </div>

        <ul className="features-grid">
          <li className="feature-card">
            <img src={scanImage} alt="Scan Plants" />
            <h3>1. Multi-Plant Visual Scanner</h3>
            <p>
              Upload or photograph any leaf specimen. <span>Vanaspati.AI</span> evaluates foliage morphology across tomatoes, potatoes, apples, corn, grapes, peppers, and roses in under 2 seconds.
            </p>
            <Link to="/predict" style={{ marginTop: "14px", textDecoration: "none" }}>
              <span className="card-link" style={{ color: "var(--primary-light)", fontWeight: 700, fontSize: "0.9rem" }}>
                Launch Scanner →
              </span>
            </Link>
          </li>

          <li className="feature-card">
            <img src={diagnoseImage} alt="Diagnose Diseases" />
            <h3>2. Fine-Grained Pathology AI</h3>
            <p>
              Identifies fungal infections, bacterial blights, viral mottles, and mite infestations with high accuracy and scientific pathogen names (e.g. <i>Alternaria solani</i>, <i>Diplocarpon rosae</i>).
            </p>
            <Link to="/predict" style={{ marginTop: "14px", textDecoration: "none" }}>
              <span className="card-link" style={{ color: "var(--primary-light)", fontWeight: 700, fontSize: "0.9rem" }}>
                View Conditions →
              </span>
            </Link>
          </li>

          <li className="feature-card">
            <img src={treatmentImage} alt="Treat and Prevent" />
            <h3>3. Complete Cure & Treatment</h3>
            <p>
              Provides 7-part comprehensive prescription reports covering cultural sanitation, organic remedies (Neem oil, Bacillus), approved fungicides/insecticides, and exact N-P-K fertilizer schedules.
            </p>
            <Link to="/predict" style={{ marginTop: "14px", textDecoration: "none" }}>
              <span className="card-link" style={{ color: "var(--primary-light)", fontWeight: 700, fontSize: "0.9rem" }}>
                Download Reports →
              </span>
            </Link>
          </li>
        </ul>
      </section>

      {/* Farmlyt AI Plant Identification Pipeline Section */}
      <section className="section" style={{ background: "var(--dark-bg)", borderTop: "1px solid rgba(255, 255, 255, 0.08)", padding: "70px 24px" }}>
        <div style={{ maxWidth: "1140px", margin: "0 auto" }}>
          <div style={{ textAlign: "center", marginBottom: "40px" }}>
            <span style={{ background: "rgba(45, 106, 79, 0.15)", color: "var(--primary-light)", border: "1px solid rgba(82, 183, 136, 0.25)", padding: "4px 12px", borderRadius: "6px", fontSize: "0.8rem", fontWeight: 700, textTransform: "uppercase", letterSpacing: "0.5px" }}>
              Farmlyt AI Knowledge Base
            </span>
            <h2 style={{ fontSize: "clamp(1.8rem, 3vw, 2.4rem)", fontWeight: 800, color: "#ffffff", marginTop: "12px" }}>
              How AI-Powered Plant Identification Works
            </h2>
            <p style={{ color: "#94a3b8", fontSize: "1.05rem", maxWidth: "650px", margin: "10px auto 0" }}>
              The 6-stage deep learning and computer vision pipeline that transforms field leaf photographs into accurate botanical diagnoses.
            </p>
          </div>

          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))", gap: "20px", marginBottom: "36px" }}>
            <div style={{ background: "var(--dark-card)", border: "1px solid rgba(255, 255, 255, 0.08)", borderRadius: "12px", padding: "22px" }}>
              <div style={{ fontSize: "1.8rem", marginBottom: "8px" }}>📷</div>
              <h4 style={{ color: "#ffffff", fontSize: "1.1rem", fontWeight: 700, marginBottom: "6px" }}>1. Image Capture</h4>
              <p style={{ color: "#cbd5e1", fontSize: "0.9rem", lineHeight: 1.6, margin: 0 }}>
                High-resolution field photography of leaves, flowers, fruit, or stems under natural diffuse lighting.
              </p>
            </div>

            <div style={{ background: "var(--dark-card)", border: "1px solid rgba(255, 255, 255, 0.08)", borderRadius: "12px", padding: "22px" }}>
              <div style={{ fontSize: "1.8rem", marginBottom: "8px" }}>📤</div>
              <h4 style={{ color: "#ffffff", fontSize: "1.1rem", fontWeight: 700, marginBottom: "6px" }}>2. Upload & Validation</h4>
              <p style={{ color: "#cbd5e1", fontSize: "0.9rem", lineHeight: 1.6, margin: 0 }}>
                Automatic background verification rejects non-foliar uploads, documents, and corrupt image files.
              </p>
            </div>

            <div style={{ background: "var(--dark-card)", border: "1px solid rgba(255, 255, 255, 0.08)", borderRadius: "12px", padding: "22px" }}>
              <div style={{ fontSize: "1.8rem", marginBottom: "8px" }}>⚙️</div>
              <h4 style={{ color: "#ffffff", fontSize: "1.1rem", fontWeight: 700, marginBottom: "6px" }}>3. Image Preprocessing</h4>
              <p style={{ color: "#cbd5e1", fontSize: "0.9rem", lineHeight: 1.6, margin: 0 }}>
                Adaptive resizing, center-cropping, and tensor normalization prepare pixel matrices for deep inference.
              </p>
            </div>

            <div style={{ background: "var(--dark-card)", border: "1px solid rgba(255, 255, 255, 0.08)", borderRadius: "12px", padding: "22px" }}>
              <div style={{ fontSize: "1.8rem", marginBottom: "8px" }}>🔬</div>
              <h4 style={{ color: "#ffffff", fontSize: "1.1rem", fontWeight: 700, marginBottom: "6px" }}>4. Feature Extraction</h4>
              <p style={{ color: "#cbd5e1", fontSize: "0.9rem", lineHeight: 1.6, margin: 0 }}>
                Convolutional filters extract leaf margins, venation geometry, necrotic halos, and color gradients.
              </p>
            </div>

            <div style={{ background: "var(--dark-card)", border: "1px solid rgba(255, 255, 255, 0.08)", borderRadius: "12px", padding: "22px" }}>
              <div style={{ fontSize: "1.8rem", marginBottom: "8px" }}>🧠</div>
              <h4 style={{ color: "#ffffff", fontSize: "1.1rem", fontWeight: 700, marginBottom: "6px" }}>5. AI Classification</h4>
              <p style={{ color: "#cbd5e1", fontSize: "0.9rem", lineHeight: 1.6, margin: 0 }}>
                Multi-modal Vision Transformers (ViT) and ResNet-9 neural networks cross-examine thousands of crop patterns.
              </p>
            </div>

            <div style={{ background: "var(--dark-card)", border: "1px solid rgba(255, 255, 255, 0.08)", borderRadius: "12px", padding: "22px" }}>
              <div style={{ fontSize: "1.8rem", marginBottom: "8px" }}>📊</div>
              <h4 style={{ color: "#ffffff", fontSize: "1.1rem", fontWeight: 700, marginBottom: "6px" }}>6. 100% Verified Decision</h4>
              <p style={{ color: "#cbd5e1", fontSize: "0.9rem", lineHeight: 1.6, margin: 0 }}>
                Strict 100% accuracy rule displays verified plant species while concealing unverified names to avoid error.
              </p>
            </div>
          </div>

          <div style={{ textAlign: "center" }}>
            <Link to="/plant-identification-software">
              <button className="cta-btn" style={{ padding: "12px 28px", borderRadius: "8px", fontWeight: 700, background: "var(--primary)", border: "1px solid rgba(255, 255, 255, 0.15)", color: "#ffffff", cursor: "pointer" }}>
                Read the Complete Plant Identification Guide →
              </button>
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
};

export default HomePage;
