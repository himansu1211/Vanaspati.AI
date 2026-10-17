const CROP_CENTROIDS = {
  rice: { N: 79.89, P: 47.58, K: 39.87, temp: 23.68, humidity: 82.27, ph: 6.42, rain: 236.18 },
  maize: { N: 77.76, P: 48.44, K: 19.79, temp: 22.38, humidity: 65.09, ph: 6.24, rain: 84.76 },
  chickpea: { N: 40.09, P: 67.79, K: 79.92, temp: 18.87, humidity: 16.86, ph: 7.33, rain: 80.05 },
  kidneybeans: { N: 20.75, P: 67.54, K: 20.05, temp: 20.11, humidity: 21.60, ph: 5.74, rain: 105.91 },
  pigeonpeas: { N: 20.73, P: 67.73, K: 20.29, temp: 27.74, humidity: 48.06, ph: 5.79, rain: 149.45 },
  mothbeans: { N: 21.44, P: 48.01, K: 20.23, temp: 28.19, humidity: 53.16, ph: 6.83, rain: 51.19 },
  mungbean: { N: 20.99, P: 47.28, K: 19.87, temp: 28.52, humidity: 85.94, ph: 6.72, rain: 48.40 },
  blackgram: { N: 40.02, P: 67.47, K: 19.24, temp: 29.97, humidity: 65.11, ph: 7.13, rain: 67.88 },
  lentil: { N: 18.77, P: 68.36, K: 19.41, temp: 24.50, humidity: 75.05, ph: 6.92, rain: 45.68 },
  pomegranate: { N: 18.87, P: 18.75, K: 40.21, temp: 21.83, humidity: 90.12, ph: 6.42, rain: 107.52 },
  banana: { N: 100.23, P: 82.01, K: 50.05, temp: 27.37, humidity: 80.35, ph: 5.98, rain: 104.62 },
  mango: { N: 20.07, P: 27.18, K: 29.92, temp: 31.20, humidity: 50.15, ph: 6.96, rain: 94.70 },
  grapes: { N: 23.18, P: 132.53, K: 200.11, temp: 23.84, humidity: 81.87, ph: 6.02, rain: 69.61 },
  watermelon: { N: 99.42, P: 17.00, K: 50.22, temp: 25.59, humidity: 85.16, ph: 6.49, rain: 50.78 },
  muskmelon: { N: 100.32, P: 17.72, K: 50.08, temp: 28.66, humidity: 92.34, ph: 6.35, rain: 24.68 },
  apple: { N: 20.80, P: 134.22, K: 199.89, temp: 22.63, humidity: 59.35, ph: 5.92, rain: 112.65 },
  orange: { N: 19.58, P: 16.55, K: 10.01, temp: 22.76, humidity: 92.17, ph: 7.01, rain: 110.47 },
  papaya: { N: 49.88, P: 59.05, K: 50.04, temp: 33.72, humidity: 92.40, ph: 6.74, rain: 142.62 },
  coconut: { N: 21.98, P: 16.93, K: 30.59, temp: 27.40, humidity: 94.84, ph: 5.97, rain: 175.68 },
  cotton: { N: 117.77, P: 46.24, K: 19.56, temp: 23.98, humidity: 79.84, ph: 6.91, rain: 80.39 },
  jute: { N: 78.40, P: 46.86, K: 39.99, temp: 24.95, humidity: 79.63, ph: 6.73, rain: 174.79 },
  coffee: { N: 101.20, P: 28.74, K: 29.94, temp: 25.54, humidity: 58.86, ph: 6.79, rain: 158.06 }
};

exports.handler = async function (event, context) {
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: JSON.stringify({ message: "Method Not Allowed" }) };
  }

  try {
    const data = JSON.parse(event.body || "{}");
    const n = parseFloat(data.nitrogen || 50);
    const p = parseFloat(data.phosphorous || 50);
    const k = parseFloat(data.pottasium || 50);
    const ph = parseFloat(data.ph || 6.5);
    const rainfall = parseFloat(data.rainfall || 100);
    const temp = parseFloat(data.temperature || 25.5);
    const humidity = parseFloat(data.humidity || 70.0);

    // Normalized Euclidean Distance Score
    let bestCrop = "rice";
    let minDistance = Infinity;
    const candidates = [];

    for (const [crop, c] of Object.entries(CROP_CENTROIDS)) {
      const d = Math.sqrt(
        Math.pow((n - c.N) / 50, 2) +
        Math.pow((p - c.P) / 50, 2) +
        Math.pow((k - c.K) / 50, 2) +
        Math.pow((temp - c.temp) / 10, 2) +
        Math.pow((humidity - c.humidity) / 20, 2) +
        Math.pow((ph - c.ph) / 2, 2) +
        Math.pow((rainfall - c.rain) / 50, 2)
      );

      candidates.push({ crop, score: d });
      if (d < minDistance) {
        minDistance = d;
        bestCrop = crop;
      }
    }

    candidates.sort((a, b) => a.score - b.score);
    const topThree = candidates.slice(0, 3).map(c => ({
      crop: c.crop,
      confidence: Math.max(0.75, Math.min(0.995, 1 - c.score * 0.15))
    }));

    return {
      statusCode: 200,
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
      },
      body: JSON.stringify({
        status: "success",
        recommended_crop: bestCrop,
        confidence: topThree[0].confidence,
        top_candidates: topThree,
        parameters: { n, p, k, ph, rainfall, temperature: temp, humidity }
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
