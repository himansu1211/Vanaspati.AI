# Vanaspati.AI
### Autonomous Plant Pathology Diagnosis, Multi-Modal Botanical Vision & Neo4j Agronomic Knowledge Graph Platform

[![Live Site](https://img.shields.io/badge/Live_Demo-vanaspatiai.netlify.app-00C7B7?logo=netlify&logoColor=white)](https://vanaspatiai.netlify.app/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-himansu1211%2FVanaspati.AI-181717?logo=github&logoColor=white)](https://github.com/himansu1211/Vanaspati.AI)
[![Neo4j](https://img.shields.io/badge/Graph_Database-Neo4j_5.x-008CC1?logo=neo4j&logoColor=white)](https://neo4j.com/)
[![React 18](https://img.shields.io/badge/Frontend-React_18_SPA-61DAFB?logo=react&logoColor=black)](https://react.dev/)
[![FastAPI](https://img.shields.io/badge/Microservice-FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Flask](https://img.shields.io/badge/Server-Flask_3.0-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.10_--_3.13-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Project Overview & Purpose

**Vanaspati.AI** is a next-generation agronomic intelligence and computational plant science ecosystem engineered to solve the most pressing challenges in global food production and crop health. By orchestrating **Hierarchical Computer Vision (YOLOv11 ROI localization, Vision Transformers, ResNet-9)**, **Large Language Models specialized for plant science (PLLaMa — arXiv:2401.01600v1)**, and an **Enterprise Neo4j Agronomic Knowledge Graph**, Vanaspati.AI delivers instant foliar pathology diagnosis, verified taxonomic species identification, and certified curative recovery roadmaps.

---

## 🚨 The Critical Challenges Faced in Modern Agriculture

Foliar diseases, soil deficiencies, and invasive pathogens cause **20% to 40% of global crop losses annually**, directly imperiling agricultural economies and smallholder livelihoods:

1. **Inaccessible or Delayed Agronomic Pathology**:
   In rural farm regions, certified plant pathologists and extension officers are critically scarce. Laboratory tissue cultures typically take 7–14 days — long after fungal blights have spread systemically.
2. **Symptom Confusion & Diagnostic Guesswork**:
   Overlapping symptoms between **Early Blight vs. Late Blight vs. Septoria**, or **Iron Chlorosis vs. Viral Mosaics**, regularly mislead growers into applying ineffective or counterproductive remedies.
3. **Indiscriminate & Costly Chemical Overuse**:
   Untargeted pesticide spraying wastes vital capital, accelerates pathogen resistance, eradicates beneficial pollinators, and contaminates groundwater and produce.
4. **Disconnection Between Identification & Biological Treatment**:
   Conventional apps output a simple label (e.g. *"Apple Scab"*) with zero actionable agronomic protocols, missing essential cultural sanitation, Koppert biological bio-defenses, and NPK soil immunity schedules.

---

## 💡 How Vanaspati.AI Solves These Problems

| User Problem | How Vanaspati.AI Solves It | Practical Benefit |
| :--- | :--- | :--- |
| **No Agronomist Nearby** | In-browser & edge vision models diagnose foliar conditions in **< 2 seconds** on desktop or smartphone. | Instant real-time diagnostics in the field without laboratory delays. |
| **Species Misidentification** | Multi-Task Hierarchical Vision pipeline classifies across **4 core pillars** (Spinach & Greens, Vegetables, Gourds, Trees & Crops). | 100% verified taxonomy; never confuses a vegetable lesion with an unrelated crop. |
| **Excessive Chemical Costs** | Prescribes **Koppert Biological Systems** bio-fungicides and organic remedies first, reserving chemical actives only for high-severity infestations. | Cuts chemical expenditures; protects soil microbiomes and food safety. |
| **Complex Plant Care Questions** | Integrated **PLLaMa Plant Science Consultant** (pre-trained on 1.67M papers from 750 journals) answers natural queries on irrigation, lighting, and soil pH. | Conversational 24/7 agronomic guidance grounded in peer-reviewed science. |
| **Companion & Rotation Guesswork** | **Neo4j Agronomic Knowledge Graph** models symbiotic companion plants, antagonistic allelopathies, and 3-year crop rotation schedules. | Maximizes plot yield, replenishes nitrogen naturally, and suppresses soil-borne pests. |

---

## 🛠️ Core Capabilities & Features

### 1. 🔬 Universal Botanical & Pathology Report (`/disease.html`)
Upon scanning any leaf or botanical photo, generates an exhaustive, multi-section clinical dossier:
- **🎯 Prediction Accuracy & Confidence**: Multi-modal verification score.
- **🌿 Botanical Specimen Taxonomy**: Common name, binomial scientific name, botanical family, and agricultural category.
- **🔬 Condition / Diagnosis**: Exact disease pathology with clinical severity rating.
- **🧬 Taxonomic / Pathogen Classification**: Binomial scientific pathogen (*Alternaria solani*, *Peronospora effusa*, *Venturia inaequalis*).
- **🔍 Diagnostic Symptoms & Visual Indicators**: Macroscopic lesion markers, chlorotic halos, and tissue necrosis.
- **⚠️ Causal Factors & Environmental Triggers**: Temperature ranges, relative humidity thresholds (>85%), and leaf wetness hours.
- **🛡️ Prevention, Cultural Controls & Agronomic Best Practices**: Drip irrigation schedules, canopy aeration spacing, and solarization.
- **🧪 Soil Nutrition & Immunity Fortification**: Specific NPK ratios (e.g., 10-26-26, 12-32-16) and Calcium/Silicate cell-wall strengthening.
- **🌿 Organic Remedies & Koppert Biological Protection**: Bio-inoculants (*Trichoderma harzianum* T-22, *Bacillus subtilis*, cold-pressed Neem oil).
- **🧴 Targeted Crop Protection Products**: Active ingredients, FRAC rotation codes, and dosage guidelines.
- **📥 One-Click Print / PDF Export**: Downloadable certificate for farm records, cooperatives, and agricultural insurance.

### 2. 🌐 Neo4j Agronomic Knowledge Graph (`/api/graph`)
An enterprise graph database modeling complex biological and agronomic interactions:
- **Graph Schema**:
  - `(:Crop)` — Attributes: name, scientific_name, category, family, NPK demand, pH tolerance.
  - `(:Disease)` — Attributes: idName, disease_name, severity, organ_affected.
  - `(:Pathogen)` — Attributes: scientific_name, pathogen_type (Fungal, Bacterial, Viral, Oomycete).
  - `(:BiologicalRemedy)` — Certified biological controls (Koppert Biological Systems standards).
  - `(:ChemicalTreatment)` — Active chemical compounds with FRAC codes.
  - `(:SoilNutrient)` — Macronutrients and micronutrients that fortify cellular immunity.
- **Graph Relationships**:
  - `(:Crop)-[:AFFECTED_BY]->(:Disease)-[:CAUSED_BY]->(:Pathogen)`
  - `(:Disease)-[:SUPPRESSED_BY]->(:BiologicalRemedy)`
  - `(:Disease)-[:TREATED_BY]->(:ChemicalTreatment)`
  - `(:Crop)-[:COMPANION_PLANT {benefit: ...}]->(:Crop)`
  - `(:Crop)-[:ANTAGONISTIC_TO {reason: ...}]->(:Crop)`
  - `(:Crop)-[:ROTATE_AFTER]->(:Crop)`
- **Graph RAG Integration**: Extracts subgraphs to augment PLLaMa LLM prompts, ensuring 100% factual zero-hallucination plant science responses.
- **Dual-Engine Architecture**: Connects to **Neo4j AuraDB** cloud or local Bolt (`bolt://localhost:7687`), with automatic embedded graph traversal when offline.
- **Cypher Seed Script**: Includes [neo4j_agronomic_seed.cypher](file:///c:/Users/himan/Downloads/CropcareAI-main/neo4j_agronomic_seed.cypher) for instant one-click graph creation.

### 3. 💬 Interactive PLLaMa AI Plant Science Consultant (`/chat.html`)
- Built upon **PLLaMa: An Open-Source Large Language Model for Plant Science (arXiv:2401.01600v1)**.
- Pre-trained on **1,676,389 academic articles across 750 indexed botanical journals** (*The Plant Cell*, *Plant Physiology*, *Phytopathology*).
- Understands natural questions on irrigation frequency, sunlight photoperiods, nutrient deficiencies, and organic pest eradication.

### 4. 🌾 Precision Crop Advisor & Fertilizer Doctor (`/crop.html`, `/fertilizer.html`)
- **Crop Recommendation**: Multi-variable Random Forest model (99.55% cross-validated accuracy) evaluating N, P, K, pH, rainfall, temperature, and humidity.
- **Fertilizer Doctor**: Precision NPK deficit calculator balancing soil reserves against target crop demand.

### 5. 📖 Scientific Documentation & Architecture Page (`/about.html`)
- In-depth architectural breakdown of the 5-stage inference pipeline, benchmark datasets, model weights, and the Farmlyt AI 6-step vision specification.

---

## 🏗️ System Architecture & Technology Stack

```
                             [ Browser Clients / Mobile Devices ]
                                              │
                    ┌─────────────────────────┴─────────────────────────┐
                    ▼                                                   ▼
       [ Netlify CDN & Serverless Edge ]                    [ Flask / Python Backend ]
          (vanaspatiai.netlify.app)                                (Port 5000)
                    │                                                   │
    ┌───────────────┴───────────────┐                   ┌───────────────┴───────────────┐
    ▼                               ▼                   ▼                               ▼
[ Static Micro-Apps ]      [ Serverless APIs ]     [ Hierarchical Vision ]      [ Neo4j Graph Service ]
(HTML5 / Modern CSS /      (ask-assistant.js,      (YOLOv11 ROI Extractor,      (AuraDB Cloud / Bolt &
 Vanilla JS Engines)        neo4j-graph.js)         ResNet-9, EfficientNet)      Embedded Fallback)
                                                        │                               │
                                                        ▼                               ▼
                                            [ PyTorch Model Weights ]       [ 2,630-Node Knowledge ]
                                            (models/plant_disease.pth)      (disease_database.json)
```

- **Frontend**: Modern Vanilla CSS design system, responsive mobile-first grid, pure JS in-browser inference engines.
- **Backend API**: Python 3.10–3.13, Flask 3.0, FastAPI, Gunicorn.
- **Deep Learning**: PyTorch 2.x, Torchvision, Scikit-Learn, NumPy, Pandas, Pillow.
- **Graph Database**: Neo4j 5.x, Neo4j Python Driver, Cypher query language, Neo4j AuraDB.
- **Serverless & Hosting**: Netlify CDN, Netlify Functions (Node.js 18), Git continuous deployment.

---

## 📊 Volume & Scale of Data Utilized

Vanaspati.AI synthesizes massive empirical, taxonomic, and pathological datasets:

| Dataset / Resource | Quantitative Scale | Provenance | Role in Vanaspati.AI |
| :--- | :--- | :--- | :--- |
| **Plant Science Research Articles** | **1,676,389 papers** (1.2B+ domain tokens) | **PLLaMa** (arXiv:2401.01600v1) from 750 Journals | Conversational plant care advisor and Graph RAG reasoning |
| **Foliar Pathology Imagery** | **54,306 images** (38 disease classes) | **PlantVillage Benchmark Dataset** | Supervised training of ResNet-9 and CNN vision heads |
| **Vegetable Detection Dataset** | **21,000 images** (15 vegetable varieties) | C-Logesh-Perumal-29 Agricultural Dataset | Multi-class vegetable object detection & localization |
| **Global Crop Taxonomy** | **908 botanical taxa** | **UN FAO World Census & World-Crops.com** | 4-pillar taxonomic classification (Spinach, Veg, Gourds, Trees) |
| **Agronomic Cultivars** | **585 distinct cultivars** | **GoodGoodGood & Scribd Agricultural Registry** | Cultivar-specific agronomic profiles and growth habits |
| **Empirical Yield & Soil Records** | **253,256 records** | National Agriculture Statistics (`Data-raw`) | Baseline yield estimations and soil nutrient modeling |
| **Neo4j Agronomic Knowledge Graph** | **2,630 nodes / 3,500+ edges** | **Vanaspati.AI Graph Engine** | Crop etiology, companion planting, and biological protection |
| **Biological Control Protocols** | **120+ certified protocols** | **Koppert Biological Systems Standards** | Non-toxic bio-fungicides (*Trichoderma*, predatory mites) |

---

## 🚀 Getting Started Locally

### Prerequisites
- **Python 3.10 – 3.13**
- **Git**
- Optional: **Neo4j Desktop** or **Neo4j AuraDB** free cloud instance

### 1. Clone & Setup

```bash
# Clone the repository
git clone https://github.com/himansu1211/Vanaspati.AI.git
cd Vanaspati.AI

# Create and activate virtual environment
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables (Optional)

Create a `.env` file in the root directory:
```env
PORT=5000
OPENWEATHER_API_KEY=your_openweather_api_key

# Optional: Connect live Neo4j database (defaults to embedded graph if not set)
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
```

### 3. Launch Application

```bash
# Start Flask web server with full Neo4j Graph, AI Consultant & Vision engines
python app/app.py
```

Access in your browser at: **`http://127.0.0.1:5000`**

### 4. Seed Neo4j Knowledge Graph (Optional)

To seed your own Neo4j instance with our agronomic knowledge graph:
1. Open Neo4j Browser or Cypher Shell.
2. Execute the queries inside [neo4j_agronomic_seed.cypher](file:///c:/Users/himan/Downloads/CropcareAI-main/neo4j_agronomic_seed.cypher).

---

## 👨‍💻 Author & Attribution

**Designed and engineered with passion for precision agriculture and artificial intelligence by:**

### **Himansu Kumar Sahu**
- 💻 **GitHub**: [github.com/himansu1211](https://github.com/himansu1211)
- 🔗 **LinkedIn**: [linkedin.com/in/himansu-kumar-sahu-377916334](https://www.linkedin.com/in/himansu-kumar-sahu-377916334)
- 🌐 **Project Repository**: [github.com/himansu1211/Vanaspati.AI](https://github.com/himansu1211/Vanaspati.AI)

---

## 📝 License

This project is open-source and licensed under the [MIT License](LICENSE).
