import React from "react";
import { Link } from "react-router-dom";

const Footer = () => {
  return (
    <footer className="site-footer" style={{
      background: "#080c0a",
      borderTop: "1px solid rgba(255, 255, 255, 0.08)",
      color: "#94a3b8",
      padding: "48px 24px 32px",
      marginTop: "auto",
      width: "100%",
      position: "relative",
      zIndex: 10
    }}>
      <div style={{
        maxWidth: "1200px",
        margin: "0 auto",
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))",
        gap: "36px",
        marginBottom: "36px"
      }}>
        {/* Brand & Mission */}
        <div>
          <div style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "12px" }}>
            <span style={{ fontSize: "1.4rem" }}>🌿</span>
            <h3 style={{
              fontFamily: "'Outfit', sans-serif",
              fontSize: "1.35rem",
              fontWeight: 800,
              color: "#ffffff",
              margin: 0
            }}>
              Vanaspati<span style={{ color: "var(--primary-light)" }}>.AI</span>
            </h3>
          </div>
          <p style={{ fontSize: "0.9rem", lineHeight: 1.6, color: "#94a3b8", margin: 0, maxWidth: "340px" }}>
            Next-generation autonomous plant pathology, multi-modal botanical vision, and precision agricultural diagnosis powered by Deep Learning, ViT, and PLLaMa scientific research.
          </p>
        </div>

        {/* Quick Navigation */}
        <div>
          <h4 style={{ color: "#ffffff", fontSize: "0.95rem", fontWeight: 700, marginBottom: "14px", textTransform: "uppercase", letterSpacing: "0.5px" }}>
            Navigation & Tools
          </h4>
          <ul style={{ listStyle: "none", padding: 0, margin: 0, display: "flex", flexDirection: "column", gap: "10px", fontSize: "0.9rem" }}>
            <li>
              <Link to="/" style={{ color: "#cbd5e1", textDecoration: "none", transition: "color 0.2s" }} onMouseOver={(e) => e.target.style.color = "var(--primary-light)"} onMouseOut={(e) => e.target.style.color = "#cbd5e1"}>
                🏠 Home
              </Link>
            </li>
            <li>
              <Link to="/predict" style={{ color: "#cbd5e1", textDecoration: "none", transition: "color 0.2s" }} onMouseOver={(e) => e.target.style.color = "var(--primary-light)"} onMouseOut={(e) => e.target.style.color = "#cbd5e1"}>
                📷 Plant & Pathology Scanner
              </Link>
            </li>
            <li>
              <Link to="/plant-identification-software" style={{ color: "#cbd5e1", textDecoration: "none", transition: "color 0.2s" }} onMouseOver={(e) => e.target.style.color = "var(--primary-light)"} onMouseOut={(e) => e.target.style.color = "#cbd5e1"}>
                🔬 AI Plant Identification Guide
              </Link>
            </li>
            <li>
              <Link to="/authenticate" style={{ color: "#cbd5e1", textDecoration: "none", transition: "color 0.2s" }} onMouseOver={(e) => e.target.style.color = "var(--primary-light)"} onMouseOut={(e) => e.target.style.color = "#cbd5e1"}>
                🔐 Account Portal
              </Link>
            </li>
          </ul>
        </div>

        {/* Scientific Foundations */}
        <div>
          <h4 style={{ color: "#ffffff", fontSize: "0.95rem", fontWeight: 700, marginBottom: "14px", textTransform: "uppercase", letterSpacing: "0.5px" }}>
            Research Foundations
          </h4>
          <ul style={{ listStyle: "none", padding: 0, margin: 0, display: "flex", flexDirection: "column", gap: "10px", fontSize: "0.88rem", color: "#94a3b8" }}>
            <li>• <strong>PLLaMa</strong> (arXiv:2401.01600v1) - 1.67M plant science papers from 750 journals</li>
            <li>• <strong>Vision Transformers</strong> - Produce & fruit classification</li>
            <li>• <strong>PlantVillage & Koppert</strong> - Certified pathology & biological control protocols</li>
            <li>• <strong>Pl@ntNet</strong> - Global botanical taxonomy benchmarks</li>
          </ul>
        </div>

        {/* Developer Info & Social Links */}
        <div>
          <h4 style={{ color: "#ffffff", fontSize: "0.95rem", fontWeight: 700, marginBottom: "14px", textTransform: "uppercase", letterSpacing: "0.5px" }}>
            Developer
          </h4>
          <div style={{ background: "rgba(255, 255, 255, 0.03)", border: "1px solid rgba(255, 255, 255, 0.08)", borderRadius: "10px", padding: "16px" }}>
            <p style={{ color: "#ffffff", fontWeight: 700, fontSize: "0.95rem", margin: "0 0 10px 0" }}>
              Built by Himansu Kumar Sahu
            </p>
            <div style={{ display: "flex", flexDirection: "column", gap: "8px" }}>
              <a
                href="https://github.com/himansu1211"
                target="_blank"
                rel="noopener noreferrer"
                style={{
                  display: "inline-flex",
                  alignItems: "center",
                  gap: "8px",
                  color: "var(--primary-light)",
                  textDecoration: "none",
                  fontWeight: 600,
                  fontSize: "0.88rem",
                  transition: "opacity 0.2s"
                }}
                onMouseOver={(e) => e.target.style.opacity = "0.75"}
                onMouseOut={(e) => e.target.style.opacity = "1"}
              >
                <span>💻</span> GitHub: himansu1211
              </a>

              <a
                href="https://www.linkedin.com/in/himansu-kumar-sahu-377916334"
                target="_blank"
                rel="noopener noreferrer"
                style={{
                  display: "inline-flex",
                  alignItems: "center",
                  gap: "8px",
                  color: "#93c5fd",
                  textDecoration: "none",
                  fontWeight: 600,
                  fontSize: "0.88rem",
                  transition: "opacity 0.2s"
                }}
                onMouseOver={(e) => e.target.style.opacity = "0.75"}
                onMouseOut={(e) => e.target.style.opacity = "1"}
              >
                <span>🔗</span> LinkedIn Profile
              </a>
            </div>
          </div>
        </div>
      </div>

      {/* Bottom Sub-footer */}
      <div style={{
        maxWidth: "1200px",
        margin: "0 auto",
        paddingTop: "24px",
        borderTop: "1px solid rgba(255, 255, 255, 0.08)",
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "space-between",
        alignItems: "center",
        gap: "12px",
        fontSize: "0.85rem",
        color: "#64748b"
      }}>
        <div>
          © {new Date().getFullYear()} Vanaspati.AI (CropcareAI). All rights reserved. Built by <strong>Himansu Kumar Sahu</strong>.
        </div>
        <div style={{ display: "flex", gap: "20px" }}>
          <a
            href="https://github.com/himansu1211"
            target="_blank"
            rel="noopener noreferrer"
            style={{ color: "#94a3b8", textDecoration: "none" }}
          >
            GitHub
          </a>
          <a
            href="https://www.linkedin.com/in/himansu-kumar-sahu-377916334"
            target="_blank"
            rel="noopener noreferrer"
            style={{ color: "#94a3b8", textDecoration: "none" }}
          >
            LinkedIn
          </a>
          <Link to="/plant-identification-software" style={{ color: "#94a3b8", textDecoration: "none" }}>
            AI Guide
          </Link>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
