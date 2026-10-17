exports.handler = async function (event, context) {
  return {
    statusCode: 200,
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*"
    },
    body: JSON.stringify({
      status: "healthy",
      service: "Vanaspati.AI Netlify Serverless API",
      version: "2.0.0",
      architecture: "Hierarchical Multi-Task Vision (Vegetables, Spinach, Trees, Crops)",
      supported_crops_count: 22,
      supported_disease_classes: 38,
      platform: "Netlify Edge & Serverless Functions"
    })
  };
};
