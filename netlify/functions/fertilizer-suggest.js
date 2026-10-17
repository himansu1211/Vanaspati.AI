const FERTILIZER_STANDARDS = {
  rice: { N: 80, P: 40, K: 40 },
  maize: { N: 80, P: 40, K: 20 },
  chickpea: { N: 40, P: 60, K: 80 },
  kidneybeans: { N: 20, P: 60, K: 20 },
  pigeonpeas: { N: 20, P: 60, K: 20 },
  mothbeans: { N: 20, P: 40, K: 20 },
  mungbean: { N: 20, P: 40, K: 20 },
  blackgram: { N: 40, P: 60, K: 20 },
  lentil: { N: 20, P: 60, K: 20 },
  pomegranate: { N: 20, P: 10, K: 40 },
  banana: { N: 100, P: 75, K: 50 },
  mango: { N: 20, P: 20, K: 30 },
  grapes: { N: 20, P: 125, K: 200 },
  watermelon: { N: 100, P: 10, K: 50 },
  muskmelon: { N: 100, P: 10, K: 50 },
  apple: { N: 20, P: 125, K: 200 },
  orange: { N: 20, P: 10, K: 10 },
  papaya: { N: 50, P: 50, K: 50 },
  coconut: { N: 20, P: 10, K: 30 },
  cotton: { N: 120, P: 40, K: 20 },
  jute: { N: 80, P: 40, K: 40 },
  coffee: { N: 100, P: 20, K: 30 }
};

const REMEDIES = {
  NHigh: {
    status: "Nitrogen Excess",
    summary: "The N value of your soil is high and might stimulate excessive weed growth or vegetative lodging.",
    remedies: [
      "Avoid applying fresh livestock manure or urea.",
      "Add sawdust or fine woodchips to soil - carbon will bind and absorb excess active nitrogen.",
      "Plant heavy nitrogen-feeding crops such as spinach, corn, or brassicas to extract residual nitrates.",
      "Irrigate deeply to leach mobile nitrates below root zones."
    ]
  },
  Nlow: {
    status: "Nitrogen Deficient",
    summary: "The N value of your soil is lower than ideal for optimal photosynthetic vigor.",
    remedies: [
      "Incorporate well-composted farmyard manure (FYM) or vermicompost at 5 tons/ha.",
      "Apply high-N organic amendments like blood meal, feathered meal, or coffee grounds.",
      "Use balanced NPK fertilizers (e.g. 20-10-10 or urea top dressing at tillering stage).",
      "Intercrop with nitrogen-fixing legumes (pulses, beans, clover)."
    ]
  },
  PHigh: {
    status: "Phosphorus Excess",
    summary: "Phosphorus levels are elevated in the soil profile.",
    remedies: [
      "Discontinue bone meal, rock phosphate, and poultry manure.",
      "Use phosphorus-free NPK blends (e.g. 15-0-15 or 20-0-20).",
      "Plant nitrogen-fixing green covers to utilize surrounding nutrients without adding phosphates.",
      "Employ rotational planting with non-accumulating crops."
    ]
  },
  Plow: {
    status: "Phosphorus Deficient",
    summary: "Soil is deficient in phosphorus, which is vital for root elongation, flowering, and energy transfer.",
    remedies: [
      "Apply steamed bone meal (fast acting) or colloidal rock phosphate (slow release).",
      "Apply DAP (Di-ammonium phosphate) or Single Super Phosphate (SSP) near the root zone.",
      "Maintain soil pH between 6.0 and 7.0; acidic or alkaline extremes bind phosphorus into insoluble minerals.",
      "Incorporate organic compost to enhance mycorrhizal fungal colonization."
    ]
  },
  KHigh: {
    status: "Potassium Excess",
    summary: "Potassium content is unusually elevated, which may inhibit magnesium and calcium uptake.",
    remedies: [
      "Avoid muriate of potash (KCl), sulfate of potash, and kelp extracts.",
      "Supplement soil with agricultural gypsum (calcium sulfate) or Epsom salts (magnesium sulfate) to rebalance cation exchange.",
      "Water thoroughly to leach soluble potassium salts.",
      "Use high-nitrogen and moderate-phosphorus formulations without potassium."
    ]
  },
  Klow: {
    status: "Potassium Deficient",
    summary: "Potassium is deficient, reducing drought resistance, disease tolerance, and fruit sizing.",
    remedies: [
      "Apply MOP (Muriate of Potash / Potassium Chloride) or SOP (Potassium Sulfate) as per recommended basal dose.",
      "Apply wood ash from untreated hardwoods (contains 5-7% soluble potash and trace micronutrients).",
      "Incorporate kelp meal, seaweed foliar spray, or buried banana peel compost.",
      "Utilize Sul-Po-Mag (Sulfate of Potash-Magnesia) for simultaneous potassium and magnesium enrichment."
    ]
  }
};

exports.handler = async function (event, context) {
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: JSON.stringify({ message: "Method Not Allowed" }) };
  }

  try {
    const data = JSON.parse(event.body || "{}");
    const crop = (data.cropname || "rice").toLowerCase().trim();
    const n = parseFloat(data.nitrogen || 50);
    const p = parseFloat(data.phosphorous || 50);
    const k = parseFloat(data.pottasium || 50);

    const target = FERTILIZER_STANDARDS[crop] || FERTILIZER_STANDARDS.rice;
    const diffN = target.N - n;
    const diffP = target.P - p;
    const diffK = target.K - k;

    const absDiffs = { N: Math.abs(diffN), P: Math.abs(diffP), K: Math.abs(diffK) };
    let primaryImbalance = "N";
    if (absDiffs.P > absDiffs.N && absDiffs.P > absDiffs.K) primaryImbalance = "P";
    else if (absDiffs.K > absDiffs.N && absDiffs.K > absDiffs.P) primaryImbalance = "K";

    let key = "Nlow";
    if (primaryImbalance === "N") key = diffN < 0 ? "NHigh" : "Nlow";
    else if (primaryImbalance === "P") key = diffP < 0 ? "PHigh" : "Plow";
    else key = diffK < 0 ? "KHigh" : "Klow";

    const remedy = REMEDIES[key];

    return {
      statusCode: 200,
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
      },
      body: JSON.stringify({
        status: "success",
        crop: crop,
        target_npk: target,
        soil_npk: { n, p, k },
        imbalance_nutrient: primaryImbalance,
        status_label: remedy.status,
        summary: remedy.summary,
        remedy_steps: remedy.remedies
      })
    };
  } catch (err) {
    return {
      statusCode: 400,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ status: "error", message: err.message })
    };
  }
};
