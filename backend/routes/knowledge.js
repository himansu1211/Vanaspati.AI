const express = require('express');
const router = express.Router();
const farmlytData = require('../data/farmlytKnowledge.json');
const pllamaData = require('../data/pllamaAdvisor.json');
const fallbackDiseases = require('../data/diseaseFallback.json');

// Get Farmlyt AI plant identification software guide
router.get('/plant-identification-software', (req, res) => {
    res.status(200).json(farmlytData);
});

// Get PLLaMa Paper & Model Specifications (arXiv:2401.01600v1)
router.get('/pllama-info', (req, res) => {
    res.status(200).json(pllamaData.model_info);
});

// Get all knowledge articles
router.get('/all', (req, res) => {
    res.status(200).json({
        total: 2,
        articles: [farmlytData, pllamaData.model_info]
    });
});

// Intelligent Plant Science & Agronomy Assistant (PLLaMa & Local LLM advisor)
router.post('/ask-assistant', (req, res) => {
    const { query, current_plant, current_condition } = req.body;
    if (!query || typeof query !== 'string') {
        return res.status(400).json({ error: 'Please provide a valid query string.' });
    }

    const cleanQuery = query.toLowerCase();

    // 1. Search PLLaMa Knowledge Base with word boundaries
    for (const item of pllamaData.knowledge_base) {
        const matches = item.keywords.some(k => {
            const escaped = k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
            const re = new RegExp(`\\b${escaped}\\b`, 'i');
            return re.test(cleanQuery);
        });
        if (matches) {
            return res.status(200).json({
                answer: item.response,
                category: item.category,
                framework: "PLLaMa Botanical Language Engine (arXiv:2401.01600v1)",
                source: "PLLaMa 1.67M Scientific Papers Corpus"
            });
        }
    }

    // 2. Check if asking about specific plant in current session
    const plantKey = current_plant || 'Tomato';
    let diseaseKey = current_condition ? `${plantKey}___${current_condition}` : `${plantKey}___healthy`;
    let fallback = fallbackDiseases[diseaseKey] || fallbackDiseases[`${plantKey}___healthy`] || fallbackDiseases['Tomato___healthy'];

    if (cleanQuery.includes('symptom') || cleanQuery.includes('look like')) {
        const symptoms = Object.values(fallback.disease_symptoms || {}).join(' ');
        return res.status(200).json({
            answer: `Observed symptoms for ${fallback.plant_name || plantKey}: ${symptoms || 'Foliar discoloration or tissue necrosis.'} (Source: PLLaMa / Phytopathology Research)`,
            category: "Symptom Diagnosis",
            framework: "PLLaMa Scientific Engine"
        });
    }

    if (cleanQuery.includes('prevent') || cleanQuery.includes('care') || cleanQuery.includes('manage')) {
        const prev = Object.values(fallback.disease_prevention || {}).join(' ');
        return res.status(200).json({
            answer: `Preventive agronomy for ${fallback.plant_name || plantKey}: ${prev || 'Ensure proper spacing, sanitized tools, and avoid leaf moisture.'} (Source: PLLaMa Agronomy Guidelines)`,
            category: "Cultural Prevention",
            framework: "PLLaMa Scientific Engine"
        });
    }

    if (cleanQuery.includes('remedy') || cleanQuery.includes('cure') || cleanQuery.includes('organic') || cleanQuery.includes('spray')) {
        const org = Object.values(fallback.organic_remedies || {}).join(' ');
        const chem = Object.values(fallback.pesticides_and_fungicides || {}).join(' ');
        return res.status(200).json({
            answer: `Recommended treatments: [Organic]: ${org || 'Neem oil or Bacillus subtilis'}. [Standard]: ${chem || 'Targeted copper or protectant fungicide.'} (Source: PLLaMa & Koppert Biological Control)`,
            category: "Therapeutic Solutions",
            framework: "PLLaMa Scientific Engine"
        });
    }

    // Default intelligent response grounded in PLLaMa scientific principles
    return res.status(200).json({
        answer: `According to research in PLLaMa (arXiv:2401.01600v1) and agricultural best practices, successful botanical management requires: 1) Ensuring well-draining soil with balanced pH (6.0–6.8); 2) Deep root watering early in the day; 3) Staged N-P-K fertilization (balanced during vegetative growth, higher P-K during fruiting); and 4) Regular scouting for early foliar lesions. Ask about specific watering schedules, light requirements, or disease remedies for detailed protocols.`,
        category: "General Agronomic Consultation",
        framework: "PLLaMa Botanical Language Engine",
        source: "PLLaMa Plant Science Corpus"
    });
});

module.exports = router;
