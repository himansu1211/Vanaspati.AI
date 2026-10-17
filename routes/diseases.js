const express = require('express');
const router = express.Router();
const Disease = require('../models/diseaseModel');
const fallbackDiseases = require('../data/diseaseFallback.json');

// Helper to find best matching disease entry
function findDiseaseRecord(idName) {
    if (!idName) return null;
    if (fallbackDiseases[idName]) return fallbackDiseases[idName];

    // Try normalization without parentheses or commas
    const cleanQuery = idName.replace(/_\(.*?\)/g, '').replace(/,/g, '').toLowerCase();
    for (const [key, val] of Object.entries(fallbackDiseases)) {
        const cleanKey = key.replace(/_\(.*?\)/g, '').replace(/,/g, '').toLowerCase();
        if (cleanKey === cleanQuery || key.toLowerCase() === idName.toLowerCase()) {
            return val;
        }
    }
    return null;
}

// Helper to sanitize condition/disease title when host plant is unverified
function sanitizeConditionForUnverifiedPlant(diseaseName, originalPlantName) {
    if (!diseaseName) return 'Foliage Pathology Analysis';
    let sanitized = diseaseName;
    if (/healthy/i.test(sanitized)) {
        return 'Healthy Foliage (No Pathological Lesions Detected)';
    }
    const plantWords = [
        'Rose', 'Tomato', 'Potato', 'Apple', 'Corn', 'Grape', 'Peach', 'Pepper bell', 'Pepper', 
        'Strawberry', 'Cherry', 'Orange', 'Squash', 'Okra', 'Brinjal', 'Eggplant', 'Carrot', 
        'Wheat', 'Groundnut', 'Peanut', 'Cucumber', 'Pomegranate', 'Tea', 'Bhendi'
    ];
    if (originalPlantName) {
        const baseName = originalPlantName.split('(')[0].trim();
        if (baseName && !plantWords.includes(baseName)) {
            plantWords.push(baseName);
        }
    }
    plantWords.sort((a, b) => b.length - a.length);
    for (const w of plantWords) {
        const re = new RegExp('\\b' + w + '\\b', 'gi');
        sanitized = sanitized.replace(re, '').trim();
    }
    sanitized = sanitized.replace(/^[-–—:\s,]+|[-–—:\s,]+$/g, '').replace(/\s{2,}/g, ' ');
    return sanitized || 'Observed Foliar Pathology';
}

router.get('/details', async (req, res) => {
    const idName = req.query.name;
    
    try {
        const richData = findDiseaseRecord(idName);

        // Attempt DB query if MongoDB is connected
        let dbDoc = null;
        if (Disease && Disease.db && Disease.db.readyState === 1) {
            try {
                dbDoc = await Disease.findOne({ idName: idName }).lean();
            } catch (dbErr) {
                console.warn('[Vanaspati.AI] DB query fallback:', dbErr.message);
            }
        }
        
        // Prioritize comprehensive rich agronomy data over sparse dummy DB records
        let finalData = null;
        if (richData) {
            finalData = { ...richData };
            // If DB doc has custom fields, merge them without overriding rich arrays
            if (dbDoc && dbDoc._id) {
                finalData._id = dbDoc._id;
            }
        } else if (dbDoc) {
            finalData = dbDoc;
        }
        
        if (!finalData) {
            return res.status(404).json({ message: 'Disease details not found for ' + idName });
        }

        // Enforce strict 100% accuracy rule for plant identification
        if (req.query.plant_identified === 'false' || req.query.plant_identified === false) {
            finalData.plant_identified = false;
            finalData.original_plant_name = finalData.plant_name;
            finalData.plant_name = null;
            finalData.disease_name = sanitizeConditionForUnverifiedPlant(finalData.disease_name, finalData.original_plant_name);
        } else if (req.query.plant_identified === 'true' || req.query.plant_identified === true) {
            finalData.plant_identified = true;
        } else {
            // Default when chosen explicitly via dropdown
            finalData.plant_identified = true;
        }

        res.status(200).json(finalData);

    } catch (error) {
        console.error('[Vanaspati.AI] Disease details error:', error);
        const richData = findDiseaseRecord(idName);
        if (richData) {
            return res.status(200).json(richData);
        }
        res.status(500).json({ message: 'Server error' });
    }
});

// List all supported diseases
router.get('/list', (req, res) => {
    res.status(200).json({
        total: Object.keys(fallbackDiseases).length,
        diseases: Object.keys(fallbackDiseases)
    });
});

module.exports = router;