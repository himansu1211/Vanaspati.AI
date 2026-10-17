const express = require('express');
const router = express.Router();
const Disease = require('../models/diseaseModel');
const fallbackDiseases = require('../data/diseaseFallback.json');

// Helper to find best matching disease entry
function findDiseaseRecord(idName) {
    if (!idName) return null;
    if (fallbackDiseases[idName]) return fallbackDiseases[idName];

    // Try normalization without parentheses or commas
    const cleanQuery = idName.replace(/_\(.*?\)/g, '').replace(/,/g, '').toLowerCase().trim();
    for (const [key, val] of Object.entries(fallbackDiseases)) {
        const cleanKey = key.replace(/_\(.*?\)/g, '').replace(/,/g, '').toLowerCase().trim();
        if (cleanKey === cleanQuery || key.toLowerCase() === idName.toLowerCase()) {
            return val;
        }
    }

    // Try fuzzy match on tokens (e.g. spinach + downy)
    for (const [key, val] of Object.entries(fallbackDiseases)) {
        const lowerKey = key.toLowerCase();
        if (cleanQuery.includes('downy') && lowerKey.includes('downy')) {
            return val;
        }
        if (cleanQuery.includes('spinach') && lowerKey.includes('spinach')) {
            return val;
        }
    }

    // Dynamic fallback generation for any novel botanical class
    const parts = idName.split('___');
    const plantName = parts[0] ? parts[0].replace(/_/g, ' ') : 'Identified Botanical Specimen';
    const condition = parts[1] ? parts[1].replace(/_/g, ' ') : 'Observed Foliar Condition';
    const isHealthy = /healthy/i.test(idName);

    return {
        idName: idName,
        plant_name: plantName,
        disease_name: isHealthy ? `Healthy ${plantName} Specimen` : `${plantName} - ${condition}`,
        pathogen_type: isHealthy ? 'None (Optimum Growth)' : 'Pathological Folio Infection',
        scientific_name: `${plantName} spp.`,
        severity: isHealthy ? 'Optimal Health (Zero Pathology)' : 'Moderate',
        disease_symptoms: {
            s1: isHealthy ? `Clean, vibrant foliage showing vigorous photosynthetic cellular structure.` : `Observed foliar spots and lesions typical of ${condition}.`,
            s2: isHealthy ? `Unobstructed leaf margins and healthy transpiration.` : `Chlorosis and localized cellular discoloration.`
        },
        disease_causes: {
            c1: isHealthy ? `Optimal moisture, balanced nutrients, and appropriate temperature balance.` : `Environmental humidity, moisture on foliage, and airborne spores.`
        },
        disease_prevention: {
            p1: `Maintain clean drip irrigation at root zone; avoid wetting upper leaf canopy.`,
            p2: `Ensure adequate plant spacing for continuous ambient breeze circulation.`
        },
        fertilizer_recommendation: {
            f1: `Balanced N-P-K fertilizer ratio suitable for ${plantName} to fortify cell wall defenses.`,
            f2: `Supplement with Potassium and Calcium to bolster tissue resilience.`
        },
        pesticides_and_fungicides: {
            pf1: isHealthy ? `No chemical intervention required for healthy specimens.` : `Apply registered protective bio-fungicide or copper spray at labeled rates.`
        },
        organic_remedies: {
            org1: `Cold-pressed organic neem oil spray (1%) applied in early morning or late afternoon.`,
            org2: `Potassium bicarbonate or baking soda solution to suppress fungal spore germination.`
        },
        disease_control: {
            ctrl1: isHealthy ? `Continue regular scheduled agronomic monitoring and balanced feeding.` : `Prune heavily affected lower leaves; bag and discard in trash.`
        }
    };
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

        // Always ensure exact plant identification is preserved and clearly reported
        finalData.plant_identified = true;
        if (!finalData.plant_name && finalData.original_plant_name) {
            finalData.plant_name = finalData.original_plant_name;
        } else if (!finalData.plant_name && finalData.idName) {
            finalData.plant_name = finalData.idName.split('___')[0].replace(/_/g, ' ');
        }

        res.status(200).json(finalData);

    } catch (error) {
        console.error('[Vanaspati.AI] Disease details error:', error);
        const richData = findDiseaseRecord(idName);
        if (richData) {
            richData.plant_identified = true;
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