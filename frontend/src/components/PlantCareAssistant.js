import React, { useState } from "react";

const PlantCareAssistant = ({ currentPlant, currentCondition }) => {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [conversation, setConversation] = useState([
    {
      sender: "assistant",
      text: "Hello! I am your AI Plant Science Consultant, powered by PLLaMa (arXiv:2401.01600v1) and agricultural intelligence. Ask me anything about watering schedules, lighting, N-P-K fertilizers, or disease cures!",
      category: "Welcome"
    }
  ]);

  const quickPrompts = [
    "💧 How often should I water?",
    "☀️ Sunlight & temperature preferences",
    "🧪 N-P-K fertilizer recommendations",
    "🩺 How do I cure Early Blight?",
    "🧬 About PLLaMa (arXiv:2401.01600v1)"
  ];

  const handleAsk = async (textToSend) => {
    const q = textToSend || query;
    if (!q.trim()) return;

    // Add user message
    const newConv = [...conversation, { sender: "user", text: q }];
    setConversation(newConv);
    setQuery("");
    setLoading(true);

    try {
      const res = await fetch("http://localhost:4000/api/knowledge/ask-assistant", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          query: q,
          current_plant: currentPlant,
          current_condition: currentCondition
        })
      });

      const data = await res.json();
      setConversation([
        ...newConv,
        {
          sender: "assistant",
          text: data.answer,
          category: data.category,
          source: data.source || "PLLaMa Research Corpus"
        }
      ]);
    } catch (err) {
      console.error("Assistant error:", err);
      setConversation([
        ...newConv,
        {
          sender: "assistant",
          text: "Could not reach the scientific consultation service. Please check your network connection.",
          category: "System Notification"
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="plant-care-assistant-card" style={{
      background: "var(--dark-card)",
      border: "1px solid rgba(255, 255, 255, 0.08)",
      borderRadius: "16px",
      padding: "24px",
      marginTop: "28px",
      boxShadow: "0 10px 30px rgba(0, 0, 0, 0.25)",
      color: "#f8fafc"
    }}>
      {/* Header */}
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", flexWrap: "wrap", gap: "10px", marginBottom: "16px" }}>
        <div>
          <div style={{ display: "flex", alignItems: "center", gap: "8px" }}>
            <span style={{ fontSize: "1.3rem" }}>🤖</span>
            <h3 style={{ fontSize: "1.2rem", fontWeight: 700, color: "#ffffff", margin: 0 }}>
              AI Plant Science Consultant (PLLaMa)
            </h3>
          </div>
          <p style={{ color: "#94a3b8", fontSize: "0.85rem", margin: "4px 0 0 0" }}>
            Scientific plant care Q&A grounded in <strong>PLLaMa (arXiv:2401.01600v1)</strong> & 1.67M academic papers.
          </p>
        </div>
        <span style={{ background: "rgba(45, 106, 79, 0.15)", color: "var(--primary-light)", padding: "4px 10px", borderRadius: "6px", fontSize: "0.78rem", fontWeight: 600, border: "1px solid rgba(82, 183, 136, 0.25)" }}>
          Active Model: PLLaMa-13B / TinyLlama
        </span>
      </div>

      {/* Quick Prompts */}
      <div style={{ display: "flex", gap: "8px", flexWrap: "wrap", marginBottom: "16px" }}>
        {quickPrompts.map((p, idx) => (
          <button
            key={idx}
            onClick={() => handleAsk(p)}
            disabled={loading}
            style={{
              background: "rgba(255, 255, 255, 0.05)",
              border: "1px solid rgba(255, 255, 255, 0.1)",
              color: "#cbd5e1",
              padding: "6px 12px",
              borderRadius: "8px",
              fontSize: "0.8rem",
              fontWeight: 500,
              cursor: "pointer",
              transition: "all 0.2s ease"
            }}
            onMouseOver={(e) => {
              e.target.style.background = "rgba(45, 106, 79, 0.2)";
              e.target.style.borderColor = "var(--primary-light)";
              e.target.style.color = "#ffffff";
            }}
            onMouseOut={(e) => {
              e.target.style.background = "rgba(255, 255, 255, 0.05)";
              e.target.style.borderColor = "rgba(255, 255, 255, 0.1)";
              e.target.style.color = "#cbd5e1";
            }}
          >
            {p}
          </button>
        ))}
      </div>

      {/* Dialogue Stream */}
      <div style={{
        maxHeight: "260px",
        overflowY: "auto",
        display: "flex",
        flexDirection: "column",
        gap: "12px",
        padding: "12px",
        background: "rgba(0, 0, 0, 0.25)",
        borderRadius: "10px",
        marginBottom: "16px",
        border: "1px solid rgba(255, 255, 255, 0.06)"
      }}>
        {conversation.map((msg, idx) => (
          <div
            key={idx}
            style={{
              alignSelf: msg.sender === "user" ? "flex-end" : "flex-start",
              maxWidth: "85%",
              background: msg.sender === "user" ? "var(--primary)" : "rgba(255, 255, 255, 0.04)",
              color: msg.sender === "user" ? "#ffffff" : "#e2e8f0",
              padding: "10px 14px",
              borderRadius: msg.sender === "user" ? "12px 12px 2px 12px" : "12px 12px 12px 2px",
              fontSize: "0.88rem",
              lineHeight: 1.5,
              border: msg.sender === "user" ? "1px solid rgba(255, 255, 255, 0.12)" : "1px solid rgba(255, 255, 255, 0.08)"
            }}
          >
            {msg.sender === "assistant" && msg.category && (
              <div style={{ fontSize: "0.75rem", color: "var(--primary-light)", fontWeight: 700, marginBottom: "4px", textTransform: "uppercase" }}>
                🔬 {msg.category}
              </div>
            )}
            <div>{msg.text}</div>
          </div>
        ))}
        {loading && (
          <div style={{ alignSelf: "flex-start", color: "var(--primary-light)", fontSize: "0.85rem", fontStyle: "italic" }}>
            🤖 Consulting PLLaMa 1.67M plant science paper database...
          </div>
        )}
      </div>

      {/* Input Field */}
      <form
        onSubmit={(e) => {
          e.preventDefault();
          handleAsk(query);
        }}
        style={{ display: "flex", gap: "10px" }}
      >
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask a plant care or disease question (e.g., 'How often to water?', 'NPK ratio?')"
          style={{
            flex: 1,
            background: "rgba(0, 0, 0, 0.25)",
            border: "1px solid rgba(255, 255, 255, 0.12)",
            borderRadius: "8px",
            padding: "10px 14px",
            color: "#ffffff",
            fontSize: "0.9rem",
            outline: "none"
          }}
        />
        <button
          type="submit"
          disabled={loading || !query.trim()}
          style={{
            background: "var(--primary)",
            color: "#ffffff",
            border: "1px solid rgba(255, 255, 255, 0.12)",
            borderRadius: "8px",
            padding: "10px 20px",
            fontWeight: 700,
            fontSize: "0.9rem",
            cursor: loading || !query.trim() ? "not-allowed" : "pointer",
            opacity: loading || !query.trim() ? 0.6 : 1,
            transition: "all 0.2s ease"
          }}
        >
          Ask AI
        </button>
      </form>
    </div>
  );
};

export default PlantCareAssistant;
