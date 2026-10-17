const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, '../backend/data/diseaseFallback.json');
const fallback = JSON.parse(fs.readFileSync(filePath, 'utf8'));

const newEntries = {
  "Downy_mildew": {
    "idName": "Downy_mildew",
    "plant_name": "Vegetables & Cucurbits",
    "disease_name": "Downy Mildew (Pseudoperonospora / Peronospora)",
    "pathogen_type": "Oomycete / Water Mold",
    "scientific_name": "Pseudoperonospora cubensis / Peronospora effusa",
    "severity": "Moderate to High (Rapid Spoilage in Cool, Humid Conditions)",
    "disease_symptoms": {
      "s1": "Angular, pale green to bright chlorotic yellow patches on the upper leaf surface delineated by leaf veins.",
      "s2": "Purplish-gray to brown downy felt or fungal sporulation on the corresponding underside of the leaves in humid weather.",
      "s3": "Severe infections cause rapid foliar browning, leaf curl, and premature defoliation."
    },
    "disease_causes": {
      "c1": "Water mold oospores and sporangia driven by extended leaf wetness (>6 hours) and high humidity (>85%).",
      "c2": "Temperatures between 15°C and 22°C (59°F–72°F) coupled with dense, unventilated plant spacing."
    },
    "disease_prevention": {
      "p1": "Provide wide plant spacing and north-south row alignment to accelerate leaf drying from morning sunlight.",
      "p2": "Use drip or furrow irrigation exclusively; never apply overhead sprinklers during evening or overcast periods."
    },
    "fertilizer_recommendation": {
      "f1": "Balanced N-P-K nutrition (10-10-10 or 8-16-16) with supplemental potassium silicate to fortify epidermal leaf cell walls.",
      "f2": "Avoid heavy spring nitrogen applications which promote excessively soft, vulnerable succulence."
    },
    "pesticides_and_fungicides": {
      "pf1": "Curative systemic fungicides: Mefenoxam + Mancozeb (Ridomil Gold MZ), Cymoxanil (Curzate), or Dimethomorph (Acrobat 50WP).",
      "pf2": "Protectant contact fungicides: Copper hydroxide (Kocide 3000) or Chlorothalonil applied every 7-10 days."
    },
    "organic_remedies": {
      "org1": "Bio-fungicides containing Bacillus subtilis (Serenade ASO) or Trichoderma harzianum as early preventive sprays.",
      "org2": "Potassium bicarbonate (MilStop) or copper octanoate (copper soap) to suppress spore germination without synthetic residue."
    },
    "disease_control": {
      "ctrl1": "Scout lower canopy leaves twice weekly and immediately rogue out early infected leaves into sealed bags.",
      "ctrl2": "Rotate out of host crop families for a minimum of 2-3 years after harvest."
    }
  },
  "Spinach___healthy": {
    "idName": "Spinach___healthy",
    "plant_name": "Spinach (Spinacia oleracea)",
    "disease_name": "Healthy Spinach Specimen",
    "pathogen_type": "None (Optimum Growth)",
    "scientific_name": "Spinacia oleracea",
    "severity": "Optimal Health (Zero Pathology)",
    "disease_symptoms": {
      "s1": "Lush, dark green crinkled (savoy) or smooth tender leaves with crisp turgid petiole structure.",
      "s2": "Uniform leaf blade color with no yellow chlorosis, downy sporulation, or leaf spot lesions.",
      "s3": "Compact rosette growth habit with vigorous crown and white fibrous roots."
    },
    "disease_causes": {
      "c1": "Cool-season growth under moist, organic-rich soil (pH 6.5–7.0) with consistent moisture."
    },
    "disease_prevention": {
      "p1": "Maintain consistent shallow cultivation to suppress weeds without disturbing spinach's delicate feeder roots.",
      "p2": "Ensure afternoon shade or shade cloth during warm spells to prevent premature bolting."
    },
    "fertilizer_recommendation": {
      "f1": "Nitrogen-rich organic foliar feeds (fish emulsion, blood meal, or compost tea) applied bi-weekly.",
      "f2": "Light side-dressing of balanced organic 5-5-5 fertilizer during peak rosette leaf expansion."
    },
    "pesticides_and_fungicides": {
      "pf1": "No chemical intervention needed for healthy spinach.",
      "pf2": "Insecticidal soap or neem spray if leaf miner scouts or aphids are detected on outer leaves."
    },
    "organic_remedies": {
      "org1": "Apply a thin layer of compost mulch around crowns to regulate soil temperature and prevent soil splashing.",
      "org2": "Companion planting with radishes, onions, and strawberries to naturally deter pests."
    },
    "disease_control": {
      "ctrl1": "Harvest outer leaves continuously (cut-and-come-again) to promote vigorous center leaf development."
    }
  },
  "Beetroot___healthy": {
    "idName": "Beetroot___healthy",
    "plant_name": "Beetroot (Beta vulgaris)",
    "disease_name": "Healthy Beetroot Specimen",
    "pathogen_type": "None (Optimum Growth)",
    "scientific_name": "Beta vulgaris",
    "severity": "Optimal Health (Zero Pathology)",
    "disease_symptoms": {
      "s1": "Firm, rounded globe-shaped crimson-purple taproot with smooth skin and unbroken crown.",
      "s2": "Vibrant upright green and maroon foliage free from Cercospora leaf spot or downy mildew.",
      "s3": "Crisp internal rings with deep ruby coloration and sweet, earthy flavor."
    },
    "disease_causes": {
      "c1": "Loose, stone-free sandy loam soil with adequate boron and neutral pH (6.0–6.8)."
    },
    "disease_prevention": {
      "p1": "Thin beet seedlings early to 7-10 cm apart to ensure unobstructed root bulb expansion.",
      "p2": "Maintain uniform soil moisture to prevent woody texture, root splitting, or internal ring discoloration."
    },
    "fertilizer_recommendation": {
      "f1": "High-potassium and phosphorus fertilizer (NPK 5-10-10 or bone meal with wood ash) to promote bulb sizing.",
      "f2": "Apply trace micronutrient boron (Solubor at 1.5 g/L) if soil is boron-deficient to prevent internal black heart."
    },
    "pesticides_and_fungicides": {
      "pf1": "No chemical fungicide or pesticide required for prime healthy beetroot.",
      "pf2": "Diatomaceous earth dusting around seedlings to stop flea beetles."
    },
    "organic_remedies": {
      "org1": "Mulch beds with aged straw or shredded leaves to maintain cool root temperatures.",
      "org2": "Incorporate well-rotted leaf mold compost before sowing to loosen heavy clay soil."
    },
    "disease_control": {
      "ctrl1": "Harvest roots when they reach 5–8 cm in diameter for prime tenderness and maximum nutritional value."
    }
  },
  "Radish___healthy": {
    "idName": "Radish___healthy",
    "plant_name": "Radish (Raphanus sativus)",
    "disease_name": "Healthy Radish Specimen",
    "pathogen_type": "None (Optimum Growth)",
    "scientific_name": "Raphanus sativus",
    "severity": "Optimal Health (Zero Pathology)",
    "disease_symptoms": {
      "s1": "Plump, crisp, and firm scarlet or white taproots with smooth surface and zero splitting.",
      "s2": "Healthy green lyrate lobed leaves with vibrant coloration and no flea beetle shot-hole damage.",
      "s3": "Crisp, peppery white internal flesh without pithiness or internal discoloration."
    },
    "disease_causes": {
      "c1": "Fast-growing cool-season conditions (21-30 days to maturity) in light, friable, moisture-retentive soil."
    },
    "disease_prevention": {
      "p1": "Sow successionally every 10–14 days for a continuous crisp harvest throughout spring and autumn.",
      "p2": "Cover fresh beds with lightweight floating row covers immediately after seeding to exclude root maggots."
    },
    "fertilizer_recommendation": {
      "f1": "Low-nitrogen organic compost; excess nitrogen creates oversized leafy tops with diminutive, split roots.",
      "f2": "Light application of aged wood ash or potassium sulfate to enhance root firmness."
    },
    "pesticides_and_fungicides": {
      "pf1": "No synthetic chemical intervention required for fast-turnaround healthy radishes.",
      "pf2": "Spinosad or pyrethrin spot-spray only if intense flea beetle infestation occurs."
    },
    "organic_remedies": {
      "org1": "Dust bed perimeter with wood ash or neem cake powder to deter subterranean larvae.",
      "org2": "Keep soil evenly damp; drought stress triggers harsh bitterness, premature bolting, and woody pith."
    },
    "disease_control": {
      "ctrl1": "Harvest promptly when roots reach golf-ball diameter; leaving radishes in soil causes rapid pithiness."
    }
  },
  "Ginger___healthy": {
    "idName": "Ginger___healthy",
    "plant_name": "Ginger (Zingiber officinale)",
    "disease_name": "Healthy Ginger Rhizome & Shoot",
    "pathogen_type": "None (Optimum Growth)",
    "scientific_name": "Zingiber officinale",
    "severity": "Optimal Health (Zero Pathology)",
    "disease_symptoms": {
      "s1": "Firm, plump, aromatic rhizome fingers with thin, tan skin and yellow fibrous flesh.",
      "s2": "Erect, reed-like pseudostems with vibrant lanceolate green leaves free from leaf spot or bacterial wilt.",
      "s3": "Clean root buds showing vigorous sprouts with no softness, foul smell, or water-soaking."
    },
    "disease_causes": {
      "c1": "Rich, well-draining warm soil with high organic matter, partial canopy shade, and high humidity."
    },
    "disease_prevention": {
      "p1": "Plant only certified disease-free, plump seed rhizomes treated with Trichoderma viride.",
      "p2": "Ensure raised beds with excellent internal drainage to prevent rhizome rot (soft rot)."
    },
    "fertilizer_recommendation": {
      "f1": "High-potassium organic fertilizer (NPK 8-8-16) applied in 3 split doses during active tillering.",
      "f2": "Top-dress with well-rotted farmyard manure (FYM) or neem cake at 45 and 90 days after planting."
    },
    "pesticides_and_fungicides": {
      "pf1": "No chemical intervention needed for healthy rhizomes.",
      "pf2": "Preventive drench with Mancozeb (0.2%) or Copper Oxychloride (0.25%) before monsoon."
    },
    "organic_remedies": {
      "org1": "Mulch generously with green leaves (10-12 tons/ha) at planting and repeated after 45 days to conserve moisture and suppress weeds.",
      "org2": "Soil solarization of seedbeds prior to planting to eradicate soil-borne Pythium and Ralstonia."
    },
    "disease_control": {
      "ctrl1": "Hill up soil around ginger pseudostems periodically to protect expanding rhizome hands from sun-greening."
    }
  }
};

Object.assign(fallback, newEntries);
fs.writeFileSync(filePath, JSON.stringify(fallback, null, 2), 'utf8');
console.log('Successfully injected 5 comprehensive agronomy records into diseaseFallback.json!');
