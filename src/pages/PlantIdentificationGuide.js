import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import PlantCareAssistant from "../components/PlantCareAssistant";

const PlantIdentificationGuide = () => {
  const [guideData, setGuideData] = useState(null);

  useEffect(() => {
    window.scrollTo(0, 0);
    fetch("http://localhost:4000/api/knowledge/plant-identification-software")
      .then((res) => res.json())
      .then((data) => {
        setGuideData(data);
      })
      .catch((err) => {
        console.error("Error fetching guide data:", err);
      });
  }, []);

  return (
    <div className="plant-guide-container" style={{ padding: "90px 20px 60px", maxWidth: "1200px", margin: "0 auto", color: "#f8fafc" }}>
      {/* Header Banner */}
      <div className="guide-hero" style={{ textAlign: "center", marginBottom: "48px", background: "var(--dark-card)", padding: "40px 24px", borderRadius: "16px", border: "1px solid rgba(255, 255, 255, 0.08)" }}>
        <span style={{ background: "rgba(45, 106, 79, 0.15)", color: "var(--primary-light)", border: "1px solid rgba(82, 183, 136, 0.25)", padding: "4px 12px", borderRadius: "6px", fontSize: "0.8rem", fontWeight: 700, textTransform: "uppercase", letterSpacing: "0.5px" }}>
          Vanaspati.AI × Farmlyt AI Knowledge Base
        </span>
        <h1 style={{ fontSize: "clamp(2rem, 4vw, 2.8rem)", fontWeight: 800, marginTop: "16px", color: "#ffffff", letterSpacing: "-0.5px" }}>
          Plant Identification Software Using AI
        </h1>
        <p style={{ maxWidth: "800px", margin: "14px auto 0", fontSize: "1.05rem", color: "#94a3b8", lineHeight: 1.6 }}>
          Discover how state-of-the-art Computer Vision, Vision Transformers (ViT), and Deep Convolutional Neural Networks identify plant species, distinguish weeds, and power precision agriculture.
        </p>
        <div style={{ display: "flex", gap: "12px", justifyContent: "center", marginTop: "24px", flexWrap: "wrap" }}>
          <Link to="/predict">
            <button className="cta-btn" style={{ padding: "12px 28px", borderRadius: "8px", fontWeight: 700, cursor: "pointer", background: "var(--primary)", border: "1px solid rgba(255, 255, 255, 0.15)", color: "#ffffff" }}>
              Launch Plant & Pathology Scanner →
            </button>
          </Link>
          <a href="#pipeline" style={{ textDecoration: "none" }}>
            <button className="cta-btn" style={{ padding: "12px 24px", borderRadius: "8px", fontWeight: 600, cursor: "pointer", background: "rgba(255, 255, 255, 0.05)", border: "1px solid rgba(255, 255, 255, 0.1)", color: "#e2e8f0" }}>
              Explore 6-Step Pipeline ↓
            </button>
          </a>
        </div>
      </div>

      {/* Section 1: Introduction & Botanical Science */}
      <section style={{ marginBottom: "50px", background: "var(--dark-card)", padding: "32px", borderRadius: "14px", border: "1px solid rgba(255, 255, 255, 0.08)" }}>
        <h2 style={{ fontSize: "1.65rem", fontWeight: 700, color: "#ffffff", marginBottom: "16px" }}>
          1. Introduction to Digital Plant Identification
        </h2>
        <p style={{ fontSize: "1rem", lineHeight: 1.8, color: "#cbd5e1", marginBottom: "16px" }}>
          Plant identification software is a digital solution designed to recognize plant species from photographs using Artificial Intelligence (AI), machine learning, and computer vision. It analyzes visible morphological markers—including <strong>leaf shape</strong>, <strong>venation structure</strong>, <strong>flower anatomy</strong>, <strong>fruit appearance</strong>, <strong>stem patterns</strong>, and <strong>epidermal texture</strong>—to determine the species of a specimen in real time.
        </p>
        <p style={{ fontSize: "1rem", lineHeight: 1.8, color: "#94a3b8" }}>
          Traditional botanical identification often required heavy encyclopedias, manual dichotomous keys, or expert taxonomists. AI-powered vision bridges this gap, allowing farmers, students, agronomists, and gardeners to photograph an unfamiliar crop or weed and instantly receive scientific binomial taxonomy and cultivation guidance.
        </p>
      </section>

      {/* Section 2: Interactive 6-Step Vision Pipeline */}
      <section id="pipeline" style={{ marginBottom: "50px" }}>
        <div style={{ textAlign: "center", marginBottom: "32px" }}>
          <h2 style={{ fontSize: "1.75rem", fontWeight: 800, color: "#ffffff" }}>
            2. How AI-Powered Plant Identification Works
          </h2>
          <p style={{ color: "#94a3b8", fontSize: "0.95rem", marginTop: "8px" }}>
            The 6-stage deep learning and computer vision pipeline executed during every scan:
          </p>
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(320px, 1fr))", gap: "20px" }}>
          {guideData && guideData.pipeline_steps ? (
            guideData.pipeline_steps.map((st) => (
              <div key={st.step} style={{ background: "var(--dark-card)", border: "1px solid rgba(255, 255, 255, 0.08)", borderRadius: "12px", padding: "24px", position: "relative", transition: "transform 0.2s ease" }}>
                <div style={{ display: "flex", alignItems: "center", gap: "12px", marginBottom: "12px" }}>
                  <span style={{ fontSize: "1.8rem" }}>{st.icon}</span>
                  <div>
                    <span style={{ fontSize: "0.75rem", color: "var(--primary-light)", fontWeight: 700, textTransform: "uppercase" }}>Stage 0{st.step}</span>
                    <h3 style={{ fontSize: "1.15rem", color: "#ffffff", fontWeight: 700, margin: 0 }}>{st.title}</h3>
                  </div>
                </div>
                <p style={{ color: "#cbd5e1", fontSize: "0.92rem", lineHeight: 1.6, margin: 0 }}>
                  {st.summary}
                </p>
              </div>
            ))
          ) : (
            <p>Loading pipeline architecture...</p>
          )}
        </div>
      </section>

      {/* Section 3: Critical Distinction: Plant ID vs Disease Detection */}
      <section style={{ marginBottom: "50px", background: "var(--dark-surface)", padding: "32px", borderRadius: "16px", border: "1px solid rgba(255, 255, 255, 0.08)" }}>
        <h2 style={{ fontSize: "1.65rem", fontWeight: 700, color: "#ffffff", marginBottom: "12px" }}>
          3. Crucial Distinction: Plant Identification vs. Disease Detection
        </h2>
        <p style={{ color: "#cbd5e1", fontSize: "1rem", lineHeight: 1.7, marginBottom: "24px" }}>
          Farmlyt AI highlights an essential architectural rule that our platform adheres to: <strong>Species identification</strong> and <strong>pathology detection</strong> represent two distinct computer vision disciplines requiring specialized multi-modal models.
        </p>

        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))", gap: "20px" }}>
          <div style={{ background: "rgba(45, 106, 79, 0.08)", border: "1px solid rgba(82, 183, 136, 0.25)", borderRadius: "10px", padding: "22px" }}>
            <h3 style={{ color: "var(--primary-light)", fontSize: "1.15rem", fontWeight: 700, marginBottom: "8px" }}>
              🌱 Plant Identification
            </h3>
            <p style={{ color: "#e2e8f0", fontSize: "0.92rem", lineHeight: 1.6, marginBottom: "12px" }}>
              Predicts which plant, crop, flower, or tree species appears in a photograph based on structural morphology.
            </p>
            <ul style={{ paddingLeft: "20px", color: "#94a3b8", fontSize: "0.88rem", lineHeight: 1.8 }}>
              <li>Leaf outline & serrated margins</li>
              <li>Petiole & stem venation geometry</li>
              <li>Floral petal count & reproductive structures</li>
              <li>Produce color, sizing & epidermis texture</li>
            </ul>
          </div>

          <div style={{ background: "rgba(185, 28, 28, 0.08)", border: "1px solid rgba(185, 28, 28, 0.25)", borderRadius: "10px", padding: "22px" }}>
            <h3 style={{ color: "#fca5a5", fontSize: "1.15rem", fontWeight: 700, marginBottom: "8px" }}>
              🔬 Disease & Pathology Detection
            </h3>
            <p style={{ color: "#e2e8f0", fontSize: "0.92rem", lineHeight: 1.6, marginBottom: "12px" }}>
              Diagnoses visible pathogenic lesions, fungal mycelium, bacterial wilts, or viral mosaic discoloration.
            </p>
            <ul style={{ paddingLeft: "20px", color: "#94a3b8", fontSize: "0.88rem", lineHeight: 1.8 }}>
              <li>Concentric necrotic rings (Early Blight)</li>
              <li>Orange/brown spore pustules (Rust)</li>
              <li>Olive-dark velvety crusts (Apple Scab)</li>
              <li>White superficial powdery patches (Mildews)</li>
            </ul>
          </div>
        </div>

        <div style={{ marginTop: "24px", padding: "16px", borderRadius: "8px", background: "rgba(217, 119, 6, 0.1)", border: "1px solid #d97706" }}>
          <strong style={{ color: "#b45309" }}>🔒 The 100% Accuracy Verification Rule:</strong> <span style={{ color: "#cbd5e1" }}>If the host crop species cannot be verified with 100% certainty from a single close-up lesion, our engine conceals the plant name while displaying the verified condition and full treatment protocols to avoid false identifications.</span>
        </div>
      </section>

      {/* Section 4: Smart Agriculture Matrix */}
      <section style={{ marginBottom: "50px" }}>
        <h2 style={{ fontSize: "1.65rem", fontWeight: 700, color: "#ffffff", marginBottom: "20px" }}>
          4. Smart Agriculture Applications
        </h2>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: "16px" }}>
          {guideData && guideData.smart_agriculture_applications ? (
            guideData.smart_agriculture_applications.map((app, idx) => (
              <div key={idx} style={{ background: "var(--dark-card)", border: "1px solid rgba(255, 255, 255, 0.08)", padding: "20px", borderRadius: "10px" }}>
                <h4 style={{ color: "var(--primary-light)", fontSize: "1.05rem", fontWeight: 700, marginBottom: "8px" }}>
                  🌾 {app.domain}
                </h4>
                <p style={{ color: "#cbd5e1", fontSize: "0.9rem", lineHeight: 1.6, margin: 0 }}>
                  {app.description}
                </p>
              </div>
            ))
          ) : null}
        </div>
      </section>

      {/* Section 5: Best Practices for Photography */}
      <section style={{ marginBottom: "50px", background: "var(--dark-card)", padding: "30px", borderRadius: "14px", border: "1px solid rgba(255, 255, 255, 0.08)" }}>
        <h2 style={{ fontSize: "1.65rem", fontWeight: 700, color: "#ffffff", marginBottom: "16px" }}>
          5. Best Practices for 100% Accurate AI Identification
        </h2>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))", gap: "16px" }}>
          <div style={{ padding: "16px", background: "rgba(0, 0, 0, 0.2)", borderRadius: "8px", border: "1px solid rgba(255, 255, 255, 0.05)" }}>
            <h4 style={{ color: "#ffffff", marginBottom: "6px", fontSize: "0.95rem" }}>☀️ Natural Diffuse Lighting</h4>
            <p style={{ color: "#94a3b8", fontSize: "0.88rem", lineHeight: 1.5, margin: 0 }}>
              Photograph in bright morning daylight or open shade. Direct midday glare washes out subtle vein patterns.
            </p>
          </div>
          <div style={{ padding: "16px", background: "rgba(0, 0, 0, 0.2)", borderRadius: "8px", border: "1px solid rgba(255, 255, 255, 0.05)" }}>
            <h4 style={{ color: "#ffffff", marginBottom: "6px", fontSize: "0.95rem" }}>🎯 Crisp Macro Focus</h4>
            <p style={{ color: "#94a3b8", fontSize: "0.88rem", lineHeight: 1.5, margin: 0 }}>
              Hold the camera steady 15–30 cm from the leaf blade or flower petals to ensure fine leaf serrations are sharp.
            </p>
          </div>
          <div style={{ padding: "16px", background: "rgba(0, 0, 0, 0.2)", borderRadius: "8px", border: "1px solid rgba(255, 255, 255, 0.05)" }}>
            <h4 style={{ color: "#ffffff", marginBottom: "6px", fontSize: "0.95rem" }}>🍃 Isolate the Target Specimen</h4>
            <p style={{ color: "#94a3b8", fontSize: "0.88rem", lineHeight: 1.5, margin: 0 }}>
              Avoid cluttered backgrounds. Position a single leaf or flower in center frame to minimize non-leaf visual noise.
            </p>
          </div>
          <div style={{ padding: "16px", background: "rgba(0, 0, 0, 0.2)", borderRadius: "8px", border: "1px solid rgba(255, 255, 255, 0.05)" }}>
            <h4 style={{ color: "#ffffff", marginBottom: "6px", fontSize: "0.95rem" }}>🩺 Capture Lesion Margins</h4>
            <p style={{ color: "#94a3b8", fontSize: "0.88rem", lineHeight: 1.5, margin: 0 }}>
              For diseased foliage, capture the transition zone between healthy green tissue and necrotic spots to diagnose accurately.
            </p>
          </div>
        </div>
      </section>

      {/* Section 6: PLLaMa Plant Science LLM (arXiv:2401.01600v1) & Local AI Assistant */}
      <section style={{ marginBottom: "50px", background: "var(--dark-surface)", padding: "32px", borderRadius: "16px", border: "1px solid rgba(255, 255, 255, 0.08)" }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", flexWrap: "wrap", gap: "12px", marginBottom: "16px" }}>
          <div>
            <span style={{ background: "rgba(255, 255, 255, 0.05)", color: "#94a3b8", padding: "4px 10px", borderRadius: "6px", fontSize: "0.78rem", fontWeight: 600, textTransform: "uppercase", border: "1px solid rgba(255, 255, 255, 0.1)" }}>
              Scientific Paper Integration • arXiv:2401.01600v1
            </span>
            <h2 style={{ fontSize: "1.65rem", fontWeight: 700, color: "#ffffff", marginTop: "8px" }}>
              6. PLLaMa: Large Language Models for Plant Science
            </h2>
          </div>
          <a
            href="https://arxiv.org/html/2401.01600v1"
            target="_blank"
            rel="noopener noreferrer"
            style={{ color: "var(--primary-light)", fontSize: "0.85rem", fontWeight: 600, textDecoration: "none", border: "1px solid rgba(82, 183, 136, 0.3)", padding: "6px 14px", borderRadius: "8px" }}
          >
            Read arXiv Paper ↗
          </a>
        </div>

        <p style={{ color: "#cbd5e1", fontSize: "1rem", lineHeight: 1.7, marginBottom: "20px" }}>
          General foundational models often lack specialized domain expertise in botanical science. <strong>PLLaMa</strong> bridges this void by pretraining on <strong>1,676,389 scientific articles</strong> sourced from <strong>750 peer-reviewed plant science journals</strong> (including <i>The Plant Cell</i>, <i>Plant Physiology</i>, <i>Phytopathology</i>, and <i>Trends in Plant Science</i>). Combined with local edge models (like TinyLlama for offline IoT/Raspberry Pi plant care), it delivers rigorous, scientific agronomic answers.
        </p>

        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: "16px", marginBottom: "28px" }}>
          <div style={{ background: "var(--dark-card)", padding: "16px", borderRadius: "8px", border: "1px solid rgba(255, 255, 255, 0.08)" }}>
            <div style={{ fontSize: "1.4rem", color: "#ffffff", fontWeight: 800 }}>1.67M+</div>
            <div style={{ color: "#94a3b8", fontSize: "0.82rem", marginTop: "4px" }}>Peer-Reviewed Academic Articles</div>
          </div>
          <div style={{ background: "var(--dark-card)", padding: "16px", borderRadius: "8px", border: "1px solid rgba(255, 255, 255, 0.08)" }}>
            <div style={{ fontSize: "1.4rem", color: "#ffffff", fontWeight: 800 }}>750</div>
            <div style={{ color: "#94a3b8", fontSize: "0.82rem", marginTop: "4px" }}>Indexed Plant Science Journals</div>
          </div>
          <div style={{ background: "var(--dark-card)", padding: "16px", borderRadius: "8px", border: "1px solid rgba(255, 255, 255, 0.08)" }}>
            <div style={{ fontSize: "1.4rem", color: "#ffffff", fontWeight: 800 }}>FlashAttention</div>
            <div style={{ color: "#94a3b8", fontSize: "0.82rem", marginTop: "4px" }}>Zero-Shot Botanical QA & Evaluation</div>
          </div>
          <div style={{ background: "var(--dark-card)", padding: "16px", borderRadius: "8px", border: "1px solid rgba(255, 255, 255, 0.08)" }}>
            <div style={{ fontSize: "1.4rem", color: "#ffffff", fontWeight: 800 }}>Local Edge AI</div>
            <div style={{ color: "#94a3b8", fontSize: "0.82rem", marginTop: "4px" }}>Edge Computing on SBC / Raspberry Pi</div>
          </div>
        </div>

        {/* Embedded Interactive Assistant */}
        <PlantCareAssistant />
      </section>

      {/* Bottom CTA & Attribution */}
      <div style={{ textAlign: "center", padding: "36px 20px", background: "var(--dark-card)", borderRadius: "14px", border: "1px solid rgba(255, 255, 255, 0.08)" }}>
        <h3 style={{ fontSize: "1.4rem", fontWeight: 700, color: "#ffffff", marginBottom: "8px" }}>
          Ready to Test the AI Vision Scanner?
        </h3>
        <p style={{ color: "#94a3b8", maxWidth: "600px", margin: "0 auto 20px", fontSize: "0.95rem" }}>
          Experience real-time botanical classification and 7-part curative prescription reports.
        </p>
        <Link to="/predict">
          <button className="cta-btn" style={{ padding: "12px 32px", fontSize: "0.95rem", borderRadius: "8px", background: "var(--primary)", border: "1px solid rgba(255, 255, 255, 0.15)", color: "#ffffff", fontWeight: 700, cursor: "pointer" }}>
            Start Scanning Now →
          </button>
        </Link>
        <p style={{ fontSize: "0.8rem", color: "#64748b", marginTop: "24px" }}>
          Knowledge extracted & integrated from Farmlyt AI (Aislyn Technologies, Bengaluru) with Vanaspati.AI Vision Engine.
        </p>
      </div>
    </div>
  );
};

export default PlantIdentificationGuide;
