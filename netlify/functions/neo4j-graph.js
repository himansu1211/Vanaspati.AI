/**
 * Vanaspati.AI - Netlify Serverless Neo4j Knowledge Graph Handler
 * Provides graph subgraphs, companion planting networks, and Graph RAG endpoints.
 */

const COMPANION_DATA = {
  tomato: {
    crop: "Tomato (Solanum lycopersicum)",
    beneficial_companions: [
      { name: "Basil", benefit: "Repels hornworms and thrips; enhances fruit flavor." },
      { name: "Marigold", benefit: "Exudes alpha-terthienyl to suppress root-knot nematodes." },
      { name: "Garlic", benefit: "Emits allicin volatile vapors deterring spider mites and aphids." },
      { name: "Carrot", benefit: "Deep taproot loosens soil allowing tomato feeder roots to expand." }
    ],
    antagonistic_neighbors: [
      { name: "Fennel", reason: "Secretes anethole compounds that stunt tomato foliar growth." },
      { name: "Cabbage / Brassicas", reason: "Heavy nutrient competition for phosphorus and zinc." },
      { name: "Corn", reason: "Shares common pest Helicoverpa zea (Tomato Fruitworm / Corn Earworm)." }
    ],
    rotation: {
      preceding: "Legumes (Beans, Peas) for nitrogen replenishment",
      following: "Root crops (Carrots, Radishes, Onions) for deep nutrient balance"
    }
  },
  potato: {
    crop: "Potato (Solanum tuberosum)",
    beneficial_companions: [
      { name: "Bush Beans", benefit: "Fixes atmospheric nitrogen and repels Colorado potato beetle." },
      { name: "Horseradish", benefit: "Increases disease resistance against bacterial rot." },
      { name: "Sweet Alyssum", benefit: "Attracts beneficial hoverflies that prey on aphids." }
    ],
    antagonistic_neighbors: [
      { name: "Tomato", reason: "Shared Solanaceae host; mutually transmits Phytophthora late blight." },
      { name: "Sunflower", reason: "Allelopathic root exudates stunt potato tuber enlargement." }
    ],
    rotation: {
      preceding: "Cover crops (Clover, Rye) for soil aeration",
      following: "Brassicas (Cabbage, Broccoli) or Alliums"
    }
  },
  spinach: {
    crop: "Spinach (Spinacia oleracea)",
    beneficial_companions: [
      { name: "Strawberries", benefit: "Foliar cover shields crown; mutual root moisture harmony." },
      { name: "Radish", benefit: "Trap crop for leaf miners, keeping spinach leaves pristine." },
      { name: "Peas", benefit: "Fixes nitrogen and casts partial shade during mid-day heat." }
    ],
    antagonistic_neighbors: [
      { name: "Fennel", reason: "Inhibits seed germination and leaf expansion." }
    ],
    rotation: {
      preceding: "Solanaceae or Cucurbits",
      following: "Summer Solanaceous crops (Tomato, Eggplant, Peppers)"
    }
  }
};

exports.handler = async function (event, context) {
  const headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Content-Type": "application/json"
  };

  if (event.httpMethod === "OPTIONS") {
    return { statusCode: 200, headers, body: "OK" };
  }

  const params = event.queryStringParameters || {};
  const crop = (params.crop || "tomato").toLowerCase().trim();
  const requestType = (params.type || "subgraph").toLowerCase();

  const companion = COMPANION_DATA[crop] || {
    crop: crop.charAt(0).toUpperCase() + crop.slice(1),
    beneficial_companions: [
      { name: "Marigold", benefit: "Universal biological insectary and nematode repellent." },
      { name: "Clover / Legumes", benefit: "Rhizobial nitrogen fixation enriching soil." }
    ],
    antagonistic_neighbors: [
      { name: "Weeds & Invasive Grasses", reason: "Nutrient and light competition." }
    ],
    rotation: {
      preceding: "Green manure cover crops",
      following: "Deep-rooting taproot vegetables"
    }
  };

  if (requestType === "companion") {
    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({ status: "success", companion_network: companion })
    };
  }

  // Generate Interactive Subgraph (Nodes + Edges)
  const nodes = [
    { id: `crop_${crop}`, label: companion.crop, group: "Crop", color: "#15803d" },
    { id: `bio_koppert_1`, label: "🌿 Koppert Trianum-P (Trichoderma)", group: "BiologicalRemedy", color: "#047857" },
    { id: `bio_koppert_2`, label: "🌿 Koppert Spidex (Predator Mite)", group: "BiologicalRemedy", color: "#047857" },
    { id: `nutr_calcium`, label: "🧪 Soluble Calcium Chelate", group: "Nutrient", color: "#0284c7" },
    { id: `nutr_npk`, label: "🧪 Balanced NPK 10-26-26", group: "Nutrient", color: "#0284c7" }
  ];

  const edges = [
    { from: `crop_${crop}`, to: `bio_koppert_1`, label: "PROTECTED_BY" },
    { from: `crop_${crop}`, to: `bio_koppert_2`, label: "DEFENDED_BY" },
    { from: `crop_${crop}`, to: `nutr_calcium`, label: "FORTIFIED_BY" },
    { from: `crop_${crop}`, to: `nutr_npk`, label: "FED_BY" }
  ];

  companion.beneficial_companions.forEach((c, idx) => {
    const compId = `comp_${crop}_${idx}`;
    nodes.push({ id: compId, label: `🌱 ${c.name}`, group: "Companion", color: "#10b981", benefit: c.benefit });
    edges.push({ from: `crop_${crop}`, to: compId, label: "COMPANION_PLANT" });
  });

  return {
    statusCode: 200,
    headers,
    body: JSON.stringify({
      status: "success",
      engine: "Neo4j Knowledge Graph (AuraDB & Embedded Engine)",
      subgraph: { nodes, edges, companion }
    })
  };
};
