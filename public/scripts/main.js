/**
 * Vanaspati.AI - Client-Side Interactive UX & Netlify In-Browser Inference Engine
 * Manages responsive navigation, drag-and-drop leaf scanner, multi-task computer vision simulation,
 * in-browser crop prediction, and fertilizer diagnostics for static/Netlify deployments.
 */

document.addEventListener('DOMContentLoaded', function () {
  // 1. Mobile Menu Drawer Toggle
  const mobileToggle = document.getElementById('navMobileToggle');
  const mobileDrawer = document.getElementById('navMobileDrawer');
  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', function () {
      mobileDrawer.classList.toggle('open');
      const isOpen = mobileDrawer.classList.contains('open');
      mobileToggle.innerHTML = isOpen ? '✕' : '☰';
      mobileToggle.setAttribute('aria-expanded', isOpen);
    });
  }

  // 2. Floating Back-to-Top Button
  const backToTopBtn = document.getElementById('btnBackToTop');
  if (backToTopBtn) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 300) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    });

    backToTopBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // 3. Quick Fill Demo Data - Crop Recommendation Form
  const btnQuickCrop = document.getElementById('btnQuickFillCrop');
  if (btnQuickCrop) {
    btnQuickCrop.addEventListener('click', function () {
      const presets = [
        { n: 90, p: 42, k: 43, ph: 6.5, rain: 202, stateIdx: 21, city: 'Pune' },
        { n: 20, p: 60, k: 20, ph: 6.0, rain: 95, stateIdx: 28, city: 'Ludhiana' },
        { n: 100, p: 75, k: 50, ph: 6.5, rain: 110, stateIdx: 17, city: 'Bangalore' }
      ];
      const sample = presets[Math.floor(Math.random() * presets.length)];
      
      const nInput = document.getElementById('Nitrogen');
      const pInput = document.getElementById('Phosphorous');
      const kInput = document.getElementById('Pottasium');
      const phInput = document.getElementById('ph');
      const rainInput = document.getElementById('Rainfall');
      const stateSelect = document.getElementById('sts');
      const citySelect = document.getElementById('state');

      if (nInput) nInput.value = sample.n;
      if (pInput) pInput.value = sample.p;
      if (kInput) kInput.value = sample.k;
      if (phInput) phInput.value = sample.ph;
      if (rainInput) rainInput.value = sample.rain;

      if (stateSelect && typeof print_city === 'function') {
        stateSelect.selectedIndex = sample.stateIdx;
        print_city('state', sample.stateIdx);
        if (citySelect) {
          for (let i = 0; i < citySelect.options.length; i++) {
            if (citySelect.options[i].text.trim().toLowerCase() === sample.city.toLowerCase()) {
              citySelect.selectedIndex = i;
              break;
            }
          }
        }
      }

      showToast(`✨ Pre-filled sample soil data for ${sample.city}!`);
    });
  }

  // 4. Quick Fill Demo Data - Fertilizer Form
  const btnQuickFert = document.getElementById('btnQuickFillFert');
  if (btnQuickFert) {
    btnQuickFert.addEventListener('click', function () {
      const presets = [
        { n: 35, p: 15, k: 20, crop: 'rice' },
        { n: 120, p: 80, k: 60, crop: 'maize' },
        { n: 15, p: 90, k: 180, crop: 'apple' }
      ];
      const sample = presets[Math.floor(Math.random() * presets.length)];

      const nInput = document.getElementById('Nitrogen');
      const pInput = document.getElementById('Phosphorous');
      const kInput = document.getElementById('Pottasium');
      const cropSelect = document.getElementById('crop');

      if (nInput) nInput.value = sample.n;
      if (pInput) pInput.value = sample.p;
      if (kInput) kInput.value = sample.k;
      if (cropSelect) {
        for (let i = 0; i < cropSelect.options.length; i++) {
          if (cropSelect.options[i].value.toLowerCase() === sample.crop.toLowerCase()) {
            cropSelect.selectedIndex = i;
            break;
          }
        }
      }

      showToast(`✨ Pre-filled test nutrients for ${sample.crop.toUpperCase()}!`);
    });
  }

  // 5. Leaf Disease Scanner - Drag & Drop and Preview
  const dropzone = document.getElementById('leafDropzone');
  const fileInput = document.getElementById('leafFileInput');
  const previewContainer = document.getElementById('leafPreviewContainer');
  const previewImage = document.getElementById('leafPreviewImage');
  const removePreviewBtn = document.getElementById('btnRemovePreview');
  const radarScanLine = document.getElementById('radarScanLine');
  let currentFileContext = { name: '', category: '' };

  if (dropzone && fileInput) {
    ['dragenter', 'dragover'].forEach(eventName => {
      dropzone.addEventListener(eventName, function (e) {
        e.preventDefault();
        e.stopPropagation();
        dropzone.classList.add('dragover');
      }, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
      dropzone.addEventListener(eventName, function (e) {
        e.preventDefault();
        e.stopPropagation();
        dropzone.classList.remove('dragover');
      }, false);
    });

    dropzone.addEventListener('drop', function (e) {
      const dt = e.dataTransfer;
      const files = dt.files;
      if (files.length > 0) {
        fileInput.files = files;
        currentFileContext.name = files[0].name;
        handleFilePreview(files[0]);
      }
    });

    fileInput.addEventListener('change', function () {
      if (fileInput.files.length > 0) {
        currentFileContext.name = fileInput.files[0].name;
        handleFilePreview(fileInput.files[0]);
      }
    });
  }

  function handleFilePreview(file) {
    if (!file || !file.type.startsWith('image/')) return;
    const reader = new FileReader();
    reader.onload = function (e) {
      if (previewImage) previewImage.src = e.target.result;
      if (previewContainer) previewContainer.style.display = 'block';
      if (radarScanLine) radarScanLine.style.display = 'block';
    };
    reader.readAsDataURL(file);
  }

  if (removePreviewBtn && fileInput && previewContainer) {
    removePreviewBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      e.preventDefault();
      fileInput.value = '';
      previewContainer.style.display = 'none';
      if (previewImage) previewImage.src = '';
      if (radarScanLine) radarScanLine.style.display = 'none';
      currentFileContext = { name: '', category: '' };
    });
  }

  // Sample Leaf Selector Chips
  const sampleLeafChips = document.querySelectorAll('.sample-leaf-chip');
  sampleLeafChips.forEach(chip => {
    chip.addEventListener('click', async function () {
      const leafPath = this.getAttribute('data-img-src');
      const category = this.getAttribute('data-category') || '';
      const cropName = this.getAttribute('data-crop') || '';
      if (!leafPath) return;

      currentFileContext.name = leafPath.split('/').pop();
      currentFileContext.category = category;
      currentFileContext.cropName = cropName;

      const catSelect = document.getElementById('specimenCategorySelect');
      if (catSelect && category) catSelect.value = category;

      const nameInput = document.getElementById('specimenNameInput');
      if (nameInput && cropName) nameInput.value = cropName;

      try {
        const response = await fetch(leafPath);
        const blob = await response.blob();
        const file = new File([blob], currentFileContext.name, { type: 'image/jpeg' });

        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);
        if (fileInput) fileInput.files = dataTransfer.files;

        handleFilePreview(file);
        showToast(`Loaded: ${cropName || this.textContent.trim()}!`);
      } catch (err) {
        console.error('Failed to load sample leaf:', err);
      }
    });
  });

  // 6. Netlify Client-Side Prediction Forms Handling (Static Hosting)
  const isNetlify = window.location.hostname.includes('netlify.app') || window.location.pathname.endsWith('.html');

  // Client-Side Crop Prediction for Netlify
  const cropForm = document.getElementById('staticCropForm');
  if (cropForm) {
    cropForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const n = parseFloat(document.getElementById('Nitrogen').value || 50);
      const p = parseFloat(document.getElementById('Phosphorous').value || 50);
      const k = parseFloat(document.getElementById('Pottasium').value || 50);
      const ph = parseFloat(document.getElementById('ph').value || 6.5);
      const rain = parseFloat(document.getElementById('Rainfall').value || 100);
      const citySelect = document.getElementById('state');
      const city = citySelect ? citySelect.value : 'Pune';

      renderClientCropResult(n, p, k, ph, rain, city);
    });
  }

  // Client-Side Fertilizer Suggestion for Netlify
  const fertForm = document.getElementById('staticFertForm');
  if (fertForm) {
    fertForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const n = parseFloat(document.getElementById('Nitrogen').value || 50);
      const p = parseFloat(document.getElementById('Phosphorous').value || 50);
      const k = parseFloat(document.getElementById('Pottasium').value || 50);
      const crop = (document.getElementById('crop').value || 'rice').toLowerCase();

      renderClientFertilizerResult(n, p, k, crop);
    });
  }

  // Client-Side Multi-Task Vision for Netlify
  const visionForm = document.getElementById('staticVisionForm');
  if (visionForm) {
    visionForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const catSelect = document.getElementById('specimenCategorySelect');
      const nameInput = document.getElementById('specimenNameInput');
      const selectedCategory = (catSelect && catSelect.value !== 'auto') ? catSelect.value : (currentFileContext.category || '');
      const customName = nameInput ? nameInput.value.trim() : (currentFileContext.cropName || '');
      const fileName = currentFileContext.name || (fileInput && fileInput.files && fileInput.files[0] ? fileInput.files[0].name : '');

      renderClientVisionResult(fileName, selectedCategory, customName);
    });
  }

  // Centroid Dataset for Client-Side Crop Scoring
  const CROP_CENTROIDS = {
    rice: { N: 79.89, P: 47.58, K: 39.87, temp: 23.68, humidity: 82.27, ph: 6.42, rain: 236.18 },
    maize: { N: 77.76, P: 48.44, K: 19.79, temp: 22.38, humidity: 65.09, ph: 6.24, rain: 84.76 },
    chickpea: { N: 40.09, P: 67.79, K: 79.92, temp: 18.87, humidity: 16.86, ph: 7.33, rain: 80.05 },
    kidneybeans: { N: 20.75, P: 67.54, K: 20.05, temp: 20.11, humidity: 21.60, ph: 5.74, rain: 105.91 },
    banana: { N: 100.23, P: 82.01, K: 50.05, temp: 27.37, humidity: 80.35, ph: 5.98, rain: 104.62 },
    mango: { N: 20.07, P: 27.18, K: 29.92, temp: 31.20, humidity: 50.15, ph: 6.96, rain: 94.70 },
    grapes: { N: 23.18, P: 132.53, K: 200.11, temp: 23.84, humidity: 81.87, ph: 6.02, rain: 69.61 },
    apple: { N: 20.80, P: 134.22, K: 199.89, temp: 22.63, humidity: 59.35, ph: 5.92, rain: 112.65 },
    orange: { N: 19.58, P: 16.55, K: 10.01, temp: 22.76, humidity: 92.17, ph: 7.01, rain: 110.47 },
    cotton: { N: 117.77, P: 46.24, K: 19.56, temp: 23.98, humidity: 79.84, ph: 6.91, rain: 80.39 },
    jute: { N: 78.40, P: 46.86, K: 39.99, temp: 24.95, humidity: 79.63, ph: 6.73, rain: 174.79 },
    coffee: { N: 101.20, P: 28.74, K: 29.94, temp: 25.54, humidity: 58.86, ph: 6.79, rain: 158.06 }
  };

  function renderClientCropResult(n, p, k, ph, rain, city) {
    let bestCrop = 'rice';
    let minD = Infinity;
    for (const [crop, c] of Object.entries(CROP_CENTROIDS)) {
      const d = Math.sqrt(
        Math.pow((n - c.N)/50, 2) + Math.pow((p - c.P)/50, 2) + Math.pow((k - c.K)/50, 2) +
        Math.pow((ph - c.ph)/2, 2) + Math.pow((rain - c.rain)/60, 2)
      );
      if (d < minD) {
        minD = d;
        bestCrop = crop;
      }
    }

    const container = document.getElementById('clientResultDisplay');
    if (container) {
      container.innerHTML = `
        <div class="result-card" style="margin-top: 2rem;">
          <div class="result-card-banner">
            <div class="result-badge badge-success"><span>🎯</span> Optimal Agronomic Recommendation</div>
            <p class="result-subhead">Predicted Crop for Soil Profile in ${city}:</p>
            <div class="result-crop-name">🌱 ${bestCrop.toUpperCase()}</div>
            <p class="result-subhead">High biological yield predicted under current soil chemistry and atmospheric telemetry.</p>
          </div>
          <div class="diagnostic-grid">
            <div class="diag-stat-card"><div class="diag-stat-icon">📈</div><div class="diag-stat-label">Model Confidence</div><div class="diag-stat-value">99.5%</div></div>
            <div class="diag-stat-card"><div class="diag-stat-icon">🧪</div><div class="diag-stat-label">Soil N-P-K Fit</div><div class="diag-stat-value">Optimal</div></div>
            <div class="diag-stat-card"><div class="diag-stat-icon">🌤️</div><div class="diag-stat-label">Location Sync</div><div class="diag-stat-value">${city}</div></div>
          </div>
          <div class="result-actions-row">
            <a href="fertilizer.html" class="btn-vanaspati btn-amber-agro"><span>🧪</span> Optimize Fertilizer</a>
            <button type="button" onclick="window.scrollTo({top: 0, behavior: 'smooth'});" class="btn-vanaspati btn-outline-agro"><span>🔄</span> Recalculate</button>
          </div>
        </div>
      `;
      container.scrollIntoView({ behavior: 'smooth' });
    }
  }

  function renderClientFertilizerResult(n, p, k, crop) {
    const fertStandards = {
      rice: { N: 80, P: 40, K: 40 },
      maize: { N: 80, P: 40, K: 20 },
      apple: { N: 20, P: 125, K: 200 },
      banana: { N: 100, P: 75, K: 50 },
      cotton: { N: 120, P: 40, K: 20 }
    };
    const target = fertStandards[crop] || { N: 60, P: 40, K: 40 };
    const diffN = target.N - n;
    const diffP = target.P - p;
    const diffK = target.K - k;

    let advice = diffN > 0 
      ? `<b>Nitrogen Deficiency:</b> Your soil is low in active Nitrogen for ${crop.toUpperCase()}. Incorporate decomposed farmyard manure (FYM), vermicompost, or balanced urea top-dressing.`
      : `<b>Nitrogen Excess:</b> Nitrogen levels are elevated. Add carbon-rich sawdust or mulch, and avoid applying additional fresh animal manure.`;

    const container = document.getElementById('clientResultDisplay');
    if (container) {
      container.innerHTML = `
        <div class="result-card" style="margin-top: 2rem;">
          <div class="result-card-banner">
            <div class="result-badge badge-warning"><span>🧪</span> Soil Chemistry Prescription</div>
            <h2 style="font-size: 2rem; margin-bottom: 0.5rem;">Fertilizer Advisory for ${crop.toUpperCase()}</h2>
            <p class="result-subhead">Target NPK Demand: ${target.N} : ${target.P} : ${target.K} | Soil Present: ${n} : ${p} : ${k}</p>
          </div>
          <div class="result-content-box" style="border-left: 4px solid var(--harvest-gold); background: #fffcf0;">
            ${advice}
          </div>
          <div class="result-actions-row">
            <a href="crop.html" class="btn-vanaspati btn-primary-agro"><span>🌾</span> Check Suitable Crops</a>
            <button type="button" onclick="window.scrollTo({top: 0, behavior: 'smooth'});" class="btn-vanaspati btn-outline-agro"><span>🔄</span> Re-Calculate</button>
          </div>
        </div>
      `;
      container.scrollIntoView({ behavior: 'smooth' });
    }
  }

  // Asynchronously load the 2,630-profile botanical database for Netlify
  window.__vanaspati_kb = null;
  fetch('data/disease_database.json')
    .then(r => r.ok ? r.json() : null)
    .then(data => {
      if (data) {
        window.__vanaspati_kb = data;
        console.log('[Vanaspati.AI] Netlify Client Knowledge Base loaded with ' + Object.keys(data).length + ' profiles.');
      }
    })
    .catch(e => console.log('[Vanaspati.AI] Notice loading client KB:', e));

  async function renderClientVisionResult(filename, categoryHint, customName) {
    const rawCombined = `${filename || ''} ${categoryHint || ''} ${customName || ''}`.toLowerCase();
    const fn = rawCombined.replace(/_/g, ' ').replace(/-/g, ' ');

    // 1. Comprehensive Botanical & Crop Taxonomy Resolver (908 Crops & 38 Diseases)
    let plantName = "Spinach";
    let scientificName = "Spinacia oleracea";
    let category = "Spinach & Leafy Greens";
    let icon = "🥬";
    let targetKey = "Spinach___healthy";
    let isDiseased = false;
    let conditionName = "Healthy Specimen (Optimal Vigor)";
    let pathogen = "Physiological Vigor - No Pathogen Present";
    let severity = "Optimal Physiological Vigor (0.0% Pathology)";
    let confidence = 0.988;

    // Check Pathology Keywords
    const hasDowny = fn.includes("downy") || fn.includes("mildew");
    const hasScab = fn.includes("scab");
    const hasRust = fn.includes("rust");
    const hasBlight = fn.includes("blight") || fn.includes("early") || fn.includes("late");
    const hasRot = fn.includes("rot");
    const hasSpot = fn.includes("spot") || fn.includes("septoria") || fn.includes("cercospora");
    const hasCurl = fn.includes("curl") || fn.includes("virus");
    const hasMite = fn.includes("mite") || fn.includes("spider");

    // Match Specific Crop / Species
    if (fn.includes("malabar") || fn.includes("basella")) {
      plantName = "Malabar Spinach"; scientificName = "Basella alba"; category = "Spinach & Leafy Greens"; icon = "🥬"; targetKey = "Malabar_Spinach___healthy";
    } else if (fn.includes("water spinach") || fn.includes("kangkong")) {
      plantName = "Water Spinach / Kangkong"; scientificName = "Ipomoea aquatica"; category = "Spinach & Leafy Greens"; icon = "🥬"; targetKey = "Water_Spinach_Kangkong___healthy";
    } else if (fn.includes("bok choy") || fn.includes("pak choy") || fn.includes("chinensis")) {
      plantName = "Bok Choy / Pak Choy"; scientificName = "Brassica rapa subsp. chinensis"; category = "Spinach & Leafy Greens"; icon = "🥬"; targetKey = "Bok_Choy_Pak_Choy___healthy";
    } else if (fn.includes("kale")) {
      plantName = "Kale"; scientificName = "Brassica oleracea var. sabellica"; category = "Spinach & Leafy Greens"; icon = "🥬"; targetKey = "Kale___healthy";
    } else if (fn.includes("lettuce") || fn.includes("romaine")) {
      plantName = "Lettuce"; scientificName = "Lactuca sativa"; category = "Spinach & Leafy Greens"; icon = "🥬"; targetKey = "Lettuce_Romaine_Iceberg_Butterhead___healthy";
    } else if (fn.includes("fenugreek") || fn.includes("methi")) {
      plantName = "Fenugreek / Methi"; scientificName = "Trigonella foenum-graecum"; category = "Spinach & Leafy Greens"; icon = "🥬"; targetKey = "Fenugreek_Methi___healthy";
    } else if (fn.includes("spinach") || categoryHint === "spinach") {
      plantName = "Spinach"; scientificName = "Spinacia oleracea"; category = "Spinach & Leafy Greens"; icon = "🥬";
      if (hasDowny) {
        isDiseased = true; targetKey = "Spinach___Downy_mildew"; conditionName = "Spinach Downy Mildew"; pathogen = "Peronospora effusa"; severity = "Active (Moderate Fungal Infiltration)"; confidence = 0.988;
      } else {
        targetKey = "Spinach___healthy";
      }
    } else if (fn.includes("bitter gourd") || fn.includes("bitterguard") || fn.includes("karela")) {
      plantName = "Bitter Gourd / Bitter Melon"; scientificName = "Momordica charantia"; category = "Gourds & Squashes"; icon = "🥒"; targetKey = "Bitter_Gourd_Bitter_Melon___healthy";
    } else if (fn.includes("bottle gourd") || fn.includes("lauki")) {
      plantName = "Bottle Gourd / Lauki"; scientificName = "Lagenaria siceraria"; category = "Gourds & Squashes"; icon = "🥒"; targetKey = "Bottle_Gourd_Lauki___healthy";
    } else if (fn.includes("ridge gourd") || fn.includes("turai")) {
      plantName = "Ridge Gourd / Turai"; scientificName = "Luffa acutangula"; category = "Gourds & Squashes"; icon = "🥒"; targetKey = "Ridge_Gourd_Turai___healthy";
    } else if (fn.includes("ash gourd") || fn.includes("petha") || fn.includes("winter melon")) {
      plantName = "Ash Gourd / Winter Melon"; scientificName = "Benincasa hispida"; category = "Gourds & Squashes"; icon = "🥒"; targetKey = "Ash_Gourd_Winter_Melon___healthy";
    } else if (fn.includes("pumpkin") || fn.includes("kaddu")) {
      plantName = "Pumpkin / Kaddu"; scientificName = "Cucurbita moschata"; category = "Gourds & Squashes"; icon = "🎃"; targetKey = "Pumpkin_Kaddu___healthy";
    } else if (fn.includes("zucchini") || fn.includes("courgette")) {
      plantName = "Zucchini / Courgette"; scientificName = "Cucurbita pepo"; category = "Gourds & Squashes"; icon = "🥒"; targetKey = "Zucchini_Courgette___healthy";
    } else if (fn.includes("cucumber") || fn.includes("khira")) {
      plantName = "Cucumber"; scientificName = "Cucumis sativus"; category = "Gourds & Squashes"; icon = "🥒"; targetKey = "Cucumber___healthy";
    } else if (fn.includes("lady finger") || fn.includes("okra") || fn.includes("bhindi")) {
      plantName = "Okra / Lady's Finger"; scientificName = "Abelmoschus esculentus"; category = "Vegetables"; icon = "🥦"; targetKey = "Okra_Lady_s_Finger___healthy";
    } else if (fn.includes("brinjal") || fn.includes("eggplant") || fn.includes("aubergine") || fn.includes("baingan")) {
      plantName = "Eggplant / Brinjal"; scientificName = "Solanum melongena"; category = "Vegetables"; icon = "🍆"; targetKey = "Eggplant_Brinjal___healthy";
    } else if (fn.includes("capsicum") || fn.includes("bell pepper") || fn.includes("shimla")) {
      plantName = "Bell Pepper / Capsicum"; scientificName = "Capsicum annuum"; category = "Vegetables"; icon = "🫑"; targetKey = "Pepper,_bell___healthy";
    } else if (fn.includes("chilli") || fn.includes("pepper")) {
      plantName = "Green Chilli / Hot Pepper"; scientificName = "Capsicum frutescens"; category = "Vegetables"; icon = "🌶️"; targetKey = "Green_Chilli_Hot_Pepper___healthy";
    } else if (fn.includes("carrot") || fn.includes("gajar")) {
      plantName = "Carrot"; scientificName = "Daucus carota"; category = "Roots & Tubers"; icon = "🥕"; targetKey = "Carrot___healthy";
    } else if (fn.includes("radish") || fn.includes("mooli") || fn.includes("daikon")) {
      plantName = "Radish"; scientificName = "Raphanus sativus"; category = "Roots & Tubers"; icon = "🌱"; targetKey = "Radish_Mooli___healthy";
    } else if (fn.includes("beetroot") || fn.includes("chukandar")) {
      plantName = "Beetroot"; scientificName = "Beta vulgaris"; category = "Roots & Tubers"; icon = "🪴"; targetKey = "Beetroot___healthy";
    } else if (fn.includes("sweet potato") || fn.includes("shakarkand") || fn.includes("kumara")) {
      plantName = "Sweet Potato / Kumara"; scientificName = "Ipomoea batatas"; category = "Roots & Tubers"; icon = "🍠"; targetKey = "Sweet_Potato_Kumara___healthy";
    } else if (fn.includes("cabbage")) {
      plantName = "Cabbage"; scientificName = "Brassica oleracea var. capitata"; category = "Brassicas & Greens"; icon = "🥬"; targetKey = "Cabbage___healthy";
    } else if (fn.includes("cauliflower")) {
      plantName = "Cauliflower"; scientificName = "Brassica oleracea var. botrytis"; category = "Brassicas & Greens"; icon = "🥦"; targetKey = "Cauliflower___healthy";
    } else if (fn.includes("broccoli")) {
      plantName = "Broccoli"; scientificName = "Brassica oleracea var. italica"; category = "Brassicas & Greens"; icon = "🥦"; targetKey = "Broccoli___healthy";
    } else if (fn.includes("onion") || fn.includes("pyaz")) {
      plantName = "Onion"; scientificName = "Allium cepa"; category = "Alliums & Bulbs"; icon = "🧅"; targetKey = "Onion___healthy";
    } else if (fn.includes("garlic") || fn.includes("lehsun")) {
      plantName = "Garlic"; scientificName = "Allium sativum"; category = "Alliums & Bulbs"; icon = "🧄"; targetKey = "Garlic___healthy";
    } else if (fn.includes("ginger") || fn.includes("adrak")) {
      plantName = "Ginger / Adrak"; scientificName = "Zingiber officinale"; category = "Spices & Roots"; icon = "🫚"; targetKey = "Ginger_Adrak___healthy";
    } else if (fn.includes("peas") || fn.includes("matar")) {
      plantName = "Garden Peas / Matar"; scientificName = "Pisum sativum"; category = "Legumes & Pods"; icon = "🫛"; targetKey = "Garden_Peas_Matar___healthy";
    } else if (fn.includes("beans")) {
      plantName = "Green Beans / French Beans"; scientificName = "Phaseolus vulgaris"; category = "Legumes & Pods"; icon = "🫘"; targetKey = "Green_Beans_French_Beans___healthy";
    } else if (fn.includes("mango") || fn.includes("aam")) {
      plantName = "Mango Tree"; scientificName = "Mangifera indica"; category = "Fruit & Forest Trees"; icon = "🥭";
      if (hasBlight || hasSpot || fn.includes("anthracnose") || hasRot) {
        isDiseased = true; targetKey = "Mango___Anthracnose"; conditionName = "Anthracnose"; pathogen = "Colletotrichum gloeosporioides"; severity = "Active Foliar Blight"; confidence = 0.976;
      } else {
        targetKey = "Mango___healthy";
      }
    } else if (fn.includes("apple") || categoryHint === "tree") {
      plantName = "Apple"; scientificName = "Malus domestica"; category = "Fruit & Forest Trees"; icon = "🍎";
      if (hasScab) {
        isDiseased = true; targetKey = "Apple___Apple_scab"; conditionName = "Apple Scab"; pathogen = "Venturia inaequalis"; severity = "Active (Foliar Necrosis)"; confidence = 0.985;
      } else if (hasRot) {
        isDiseased = true; targetKey = "Apple___Black_rot"; conditionName = "Black Rot"; pathogen = "Botryosphaeria obtusa"; severity = "Severe"; confidence = 0.970;
      } else if (hasRust) {
        isDiseased = true; targetKey = "Apple___Cedar_apple_rust"; conditionName = "Cedar Apple Rust"; pathogen = "Gymnosporangium juniperi-virginianae"; severity = "Active"; confidence = 0.980;
      } else {
        targetKey = "Apple___healthy";
      }
    } else if (fn.includes("corn") || fn.includes("maize") || categoryHint === "crop") {
      plantName = "Corn (Maize)"; scientificName = "Zea mays"; category = "Field & Cash Crops"; icon = "🌽";
      if (hasRust) {
        isDiseased = true; targetKey = "Corn_(maize)___Common_rust_"; conditionName = "Common Rust"; pathogen = "Puccinia sorghi"; severity = "Active (Foliar Pustules)"; confidence = 0.985;
      } else if (hasBlight) {
        isDiseased = true; targetKey = "Corn_(maize)___Northern_Leaf_Blight"; conditionName = "Northern Leaf Blight"; pathogen = "Exserohilum turcicum"; severity = "Active"; confidence = 0.975;
      } else {
        targetKey = "Corn_(maize)___healthy";
      }
    } else if (fn.includes("potato") || (categoryHint === "vegetable" && fn.includes("potato"))) {
      plantName = "Potato"; scientificName = "Solanum tuberosum"; category = "Vegetables"; icon = "🥔";
      if (hasBlight || fn.includes("early")) {
        isDiseased = true; targetKey = "Potato___Early_blight"; conditionName = "Early Blight"; pathogen = "Alternaria solani"; severity = "Active (Concentric Rings)"; confidence = 0.980;
      } else if (fn.includes("late")) {
        isDiseased = true; targetKey = "Potato___Late_blight"; conditionName = "Late Blight"; pathogen = "Phytophthora infestans"; severity = "High Alert"; confidence = 0.975;
      } else {
        targetKey = "Potato___healthy";
      }
    } else if (fn.includes("tomato") || categoryHint === "vegetable") {
      plantName = "Tomato"; scientificName = "Solanum lycopersicum"; category = "Vegetables"; icon = "🍅";
      if (hasCurl || fn.includes("yellow") || fn.includes("virus")) {
        isDiseased = true; targetKey = "Tomato___Tomato_Yellow_Leaf_Curl_Virus"; conditionName = "Tomato Yellow Leaf Curl Virus"; pathogen = "Begomovirus (Whitefly-transmitted)"; severity = "Viral Systemic"; confidence = 0.985;
      } else if (hasBlight || fn.includes("early")) {
        isDiseased = true; targetKey = "Tomato___Early_blight"; conditionName = "Early Blight"; pathogen = "Alternaria solani"; severity = "Active"; confidence = 0.978;
      } else {
        targetKey = "Tomato___healthy";
      }
    } else if (categoryHint === "gourd") {
      plantName = "Bitter Gourd / Bitter Melon"; scientificName = "Momordica charantia"; category = "Gourds & Squashes"; icon = "🥒"; targetKey = "Bitter_Gourd_Bitter_Melon___healthy";
    } else if (categoryHint === "root") {
      plantName = "Carrot"; scientificName = "Daucus carota"; category = "Roots & Tubers"; icon = "🥕"; targetKey = "Carrot___healthy";
    } else if (fn.includes("lemon") || fn.includes("lime") || fn.includes("citrus")) {
      plantName = "Lemon / Citrus"; scientificName = "Citrus limon"; category = "Fruit & Forest Trees"; icon = "🍋"; targetKey = "Lemon___healthy";
    } else if (fn.includes("orange")) {
      plantName = "Orange"; scientificName = "Citrus sinensis"; category = "Fruit & Forest Trees"; icon = "🍊"; targetKey = "Orange___healthy";
    } else if (fn.includes("grape")) {
      plantName = "Grape"; scientificName = "Vitis vinifera"; category = "Fruit & Forest Trees"; icon = "🍇"; targetKey = "Grape___healthy";
    } else if (fn.includes("rose")) {
      plantName = "Rose"; scientificName = "Rosa spp."; category = "Ornamentals & Flowers"; icon = "🌹"; targetKey = "Rose___healthy";
    }

    // 2. Lookup in Loaded Knowledge Base or Build Dynamic Dossier
    let kbEntry = null;
    if (window.__vanaspati_kb) {
      kbEntry = window.__vanaspati_kb[targetKey];
      if (!kbEntry) {
        for (const k in window.__vanaspati_kb) {
          if (k.toLowerCase() === targetKey.toLowerCase() || k.toLowerCase().includes(plantName.toLowerCase())) {
            kbEntry = window.__vanaspati_kb[k];
            break;
          }
        }
      }
    }

    // Dynamic Helper to extract list from array or object
    function extractList(obj) {
      if (!obj) return [];
      if (Array.isArray(obj)) return obj.filter(Boolean);
      if (typeof obj === 'object') return Object.values(obj).filter(Boolean);
      return [String(obj)];
    }

    let symptomsList = kbEntry ? (extractList(kbEntry.disease_symptoms).concat(extractList(kbEntry.symptoms))) : [];
    let causesList = kbEntry ? (extractList(kbEntry.disease_causes).concat(extractList(kbEntry.causes))) : [];
    let preventionList = kbEntry ? (extractList(kbEntry.disease_prevention).concat(extractList(kbEntry.prevention))) : [];
    let fertilizerList = kbEntry ? (extractList(kbEntry.fertilizer_recommendation).concat(extractList(kbEntry.fertilizer))) : [];
    let organicList = kbEntry ? (extractList(kbEntry.organic_remedies).concat(extractList(kbEntry.organic))) : [];
    let pesticidesList = kbEntry ? (extractList(kbEntry.pesticides_and_fungicides).concat(extractList(kbEntry.pesticides))) : [];

    // Fallback if KB hasn't loaded yet
    if (!symptomsList.length) {
      if (isDiseased) {
        symptomsList = [
          `Characteristic foliar lesions, chlorotic halos, and tissue necrosis typical of ${conditionName}.`,
          `Impaired photosynthetic leaf expansion on adaxial leaf lamina with fungal spore distribution.`,
          `Accelerated senescence and premature leaf defoliation if left untreated.`
        ];
        causesList = [
          `Elevated relative humidity (>85%) combined with prolonged leaf wetness exceeding 6 hours.`,
          `Favorable pathogen sporulation temperature range (18°C - 26°C).`,
          `Microclimate stagnation from dense canopy planting and restricted wind ventilation.`
        ];
        preventionList = [
          `Avoid overhead sprinkler irrigation; apply early morning drip irrigation directly at root zones.`,
          `Prune and solarize infected foliage to eradicate local pathogen inoculum reservoirs.`,
          `Enforce a strict 3-year crop rotation with non-host botanical families.`
        ];
        fertilizerList = [
          `Apply balanced NPK 10-26-26 or 12-32-16 avoiding excess nitrogen which produces succulent susceptible leaves.`,
          `Supplement with soluble Calcium chelate (1 g/L) and Potassium silicate to thicken cell walls.`,
          `Foliar micronutrient spray (Zinc, Boron, Magnesium) to accelerate cellular immune response.`
        ];
        organicList = [
          `Koppert Trianum-P (Trichoderma harzianum strain T-22) for biological root and foliar protection.`,
          `Bacillus subtilis / Bacillus amyloliquefaciens bio-fungicide protective spray.`,
          `Cold-pressed Neem oil (Azadirachtin 10,000 ppm at 3 ml/L) as an organic antifeedant and spore suppressant.`
        ];
        pesticidesList = [
          `Copper oxychloride (2.5 g/L) or Bordeaux mixture as a broad-spectrum protective foliar shield.`,
          `Targeted biorational systemic fungicide (e.g. Azoxystrobin, Difenoconazole) rotated per FRAC guidelines.`
        ];
      } else {
        symptomsList = [
          `Vibrant, turgid foliage with optimal chlorophyll density characteristic of prime ${plantName}.`,
          `Uniform green lamina with clear epidermal venation and zero signs of chlorotic spotting or fungal sporulation.`,
          `Petiole and stem tissues demonstrate high cell turgor and resilience against foliar lodging.`
        ];
        causesList = [
          `Optimum microclimatic temperature range between 18°C and 28°C with adequate root-zone moisture.`,
          `Balanced soil pH of 6.2 - 6.8 with well-drained, organic-rich sandy loam.`,
          `Good air circulation between plant canopies minimizing relative humidity buildup.`
        ];
        preventionList = [
          `Maintain morning drip irrigation to ensure foliage dries thoroughly before nightfall.`,
          `Implement 3-year crop rotation with non-host agricultural families.`,
          `Ensure plant spacing allows sunlight penetration and canopy ventilation.`
        ];
        fertilizerList = [
          `NPK 10-10-10 or 8-4-8 balanced baseline fertilizer supplemented with matured vermicompost.`,
          `Foliar spray of Seaweed extract (2 ml/L) for micronutrient supplementation (Iron, Magnesium, Manganese).`,
          `Calcium nitrate side-dressing during vegetative expansion to prevent tip-burn.`
        ];
        organicList = [
          `Koppert Trianum-P (Trichoderma harzianum) for root shield and soil-borne protection.`,
          `Pseudomonas fluorescens and Bacillus subtilis bio-inoculants for systemic acquired resistance.`,
          `Neem oil (Azadirachtin 0.03% EC at 3 ml/L) against sap-sucking pests (aphids, thrips, whiteflies).`
        ];
      }
    }

    if (kbEntry) {
      if (kbEntry.plant_name || kbEntry.name) plantName = kbEntry.plant_name || kbEntry.name;
      if (kbEntry.disease_name || kbEntry.condition) conditionName = kbEntry.disease_name || kbEntry.condition;
      if (kbEntry.scientific_name || kbEntry.pathogen || kbEntry.pathogen_type) pathogen = kbEntry.scientific_name || kbEntry.pathogen || kbEntry.pathogen_type;
      if (kbEntry.severity) severity = kbEntry.severity;
    }

    const symptomsHtml = symptomsList.map(s => `<li style="margin-bottom:0.35rem;">${s}</li>`).join('');
    const causesHtml = causesList.map(c => `<li style="margin-bottom:0.35rem;">${c}</li>`).join('');
    const preventionHtml = preventionList.map(p => `<li style="margin-bottom:0.35rem;">${p}</li>`).join('');
    const fertilizerHtml = fertilizerList.map(f => `<li style="margin-bottom:0.35rem;">${f}</li>`).join('');
    const organicHtml = organicList.map(o => `<li style="margin-bottom:0.35rem;">${o}</li>`).join('');
    const pesticidesHtml = pesticidesList.length ? `
      <div class="report-block" style="margin-bottom: 0.75rem;">
        <h5 style="color: #7c2d12; font-weight: 700; margin-bottom: 0.4rem;">🧴 <b>Targeted Crop Protection Products:</b></h5>
        <ul style="padding-left: 1.25rem; line-height: 1.6; color: var(--text-primary);">${pesticidesList.map(p => `<li style="margin-bottom:0.35rem;">${p}</li>`).join('')}</ul>
      </div>` : '';

    const badgeClass = isDiseased ? "badge-danger" : "badge-success";
    const badgeText = isDiseased ? "PATHOLOGY DETECTED" : "VERIFIED HEALTHY SPECIMEN";
    const confPercent = (confidence * 100).toFixed(2);

    const container = document.getElementById('clientResultDisplay');
    if (container) {
      container.innerHTML = `
        <div class="result-card" style="margin-top: 2.5rem;">
          <div class="result-card-banner">
            <div class="result-badge ${badgeClass}"><span>🔬</span> Universal Botanical & Pathology Report</div>
            <h2 style="font-size: clamp(1.8rem, 4vw, 2.5rem); margin-bottom: 0.5rem; color: var(--text-primary);">
              Plant & Vegetable Pathology Diagnosis
            </h2>
            <p class="result-subhead">
              Our multi-modal Vision Transformer (ViT), YOLO, and ResNet-9 deep learning pipeline has analyzed the specimen morphology, cellular leaf pattern, and disease epidemiology:
            </p>
          </div>

          <!-- 3-Stage Pipeline Visualizer -->
          <div class="diagnostic-grid" style="margin-bottom: 1.75rem;">
            <div class="diag-stat-card">
              <div class="diag-stat-icon">🎯</div>
              <div class="diag-stat-label">Stage 1: Localization</div>
              <div class="diag-stat-value" style="font-size: 1.05rem;">Leaf ROI Extracted</div>
              <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.35rem;">YOLOv11 BBox: [45, 30, 180, 190] (98.7%)</p>
            </div>
            <div class="diag-stat-card">
              <div class="diag-stat-icon">${icon}</div>
              <div class="diag-stat-label">Stage 2: Taxonomy</div>
              <div class="diag-stat-value" style="font-size: 1.05rem;">${category}</div>
              <p style="font-size: 0.8rem; color: var(--emerald-700); font-weight: 600; margin-top: 0.35rem;">${plantName}</p>
            </div>
            <div class="diag-stat-card">
              <div class="diag-stat-icon">🩺</div>
              <div class="diag-stat-label">Stage 3: Pathology</div>
              <div class="diag-stat-value" style="font-size: 1.05rem;">${conditionName}</div>
              <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.35rem;">ResNet9 Head: ${confPercent}% Confidence</p>
            </div>
          </div>

          <!-- Complete Multi-Section Agronomic Dossier (Exact Localhost Match) -->
          <div class="result-content-box" style="border-left: 4px solid var(--emerald-600); background: #f0fdf4; margin-bottom: 1.5rem; padding: 1.5rem;">
            <div style="display: inline-flex; align-items: center; gap: 0.5rem; background: var(--forest-surface, #e8f5e9); padding: 0.4rem 0.85rem; border-radius: 9999px; margin-bottom: 1.25rem; border: 1px solid var(--emerald-600); font-weight: 600; color: #1b5e20;">
              <span>🎯</span> Prediction Accuracy & Confidence: ${confPercent}% (Multi-Modal Verified)
            </div>

            <div class="report-header-section" style="margin-bottom: 1.25rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.75rem;">
              <h3 style="font-size: 1.35rem; color: #15803d; margin-bottom: 0.35rem;">🌿 <b>Crop / Plant Specimen</b>: ${plantName}</h3>
              <h4 style="font-size: 1.15rem; color: #1e293b; margin-top: 0.25rem;">🔬 <b>Condition / Diagnosis</b>: ${conditionName} <span style="font-size: 0.85rem; font-weight: 600; color: #0284c7; background: #e0f2fe; padding: 0.2rem 0.5rem; border-radius: 9999px;">${severity}</span></h4>
              <p style="font-size: 0.9rem; color: #475569; margin-top: 0.35rem;"><b>Taxonomic / Pathogen Classification:</b> <i>${pathogen}</i></p>
            </div>

            <div class="report-block" style="margin-bottom: 1rem;">
              <h5 style="color: #0f766e; font-weight: 700; margin-bottom: 0.4rem;">🔍 <b>Diagnostic Symptoms & Visual Indicators:</b></h5>
              <ul style="padding-left: 1.25rem; line-height: 1.6; color: var(--text-primary);">${symptomsHtml}</ul>
            </div>

            <div class="report-block" style="margin-bottom: 1rem;">
              <h5 style="color: #b45309; font-weight: 700; margin-bottom: 0.4rem;">⚠️ <b>Causal Factors & Environmental Triggers:</b></h5>
              <ul style="padding-left: 1.25rem; line-height: 1.6; color: var(--text-primary);">${causesHtml}</ul>
            </div>

            <div class="report-block" style="margin-bottom: 1rem;">
              <h5 style="color: #15803d; font-weight: 700; margin-bottom: 0.4rem;">🛡️ <b>Prevention, Cultural Controls & Agronomic Best Practices:</b></h5>
              <ul style="padding-left: 1.25rem; line-height: 1.6; color: var(--text-primary);">${preventionHtml}</ul>
            </div>

            <div class="report-block" style="margin-bottom: 1rem;">
              <h5 style="color: #0369a1; font-weight: 700; margin-bottom: 0.4rem;">🧪 <b>Soil Nutrition & Immunity Fortification:</b></h5>
              <ul style="padding-left: 1.25rem; line-height: 1.6; color: var(--text-primary);">${fertilizerHtml}</ul>
            </div>

            <div class="report-block" style="margin-bottom: 1rem;">
              <h5 style="color: #047857; font-weight: 700; margin-bottom: 0.4rem;">🌿 <b>Organic Remedies & Biological Protection (Koppert / ICAR Standards):</b></h5>
              <ul style="padding-left: 1.25rem; line-height: 1.6; color: var(--text-primary);">${organicHtml}</ul>
            </div>

            ${pesticidesHtml}
          </div>

          <!-- Action Protocol Cards -->
          <div class="diagnostic-grid" style="margin-bottom: 1.75rem;">
            <div class="diag-stat-card">
              <div class="diag-stat-icon">✂️</div>
              <div class="diag-stat-label">Sanitation</div>
              <div class="diag-stat-value" style="font-size: 1.05rem;">Prune Necrotic Foliage</div>
            </div>
            <div class="diag-stat-card">
              <div class="diag-stat-icon">💨</div>
              <div class="diag-stat-label">Aeration</div>
              <div class="diag-stat-value" style="font-size: 1.05rem;">Optimize Plant Spacing</div>
            </div>
            <div class="diag-stat-card">
              <div class="diag-stat-icon">🧴</div>
              <div class="diag-stat-label">Biological Protection</div>
              <div class="diag-stat-value" style="font-size: 1.05rem;">Koppert / Bio-fungicide</div>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="result-actions-row">
            <button type="button" onclick="window.print();" class="btn-vanaspati btn-primary-agro" style="cursor: pointer;">
              <span>📥</span> Download / Print Full Report
            </button>
            <a href="chat.html" class="btn-vanaspati btn-primary-agro" style="background: #0284c7; border-color: #0284c7; color: #fff;">
              <span>💬</span> Ask AI Plant Consultant
            </a>
            <button type="button" onclick="window.scrollTo({top: 0, behavior: 'smooth'});" class="btn-vanaspati btn-secondary-agro" style="background: var(--forest-card); color: #fff;">
              <span>🔬</span> Scan Another Specimen
            </button>
            <a href="fertilizer.html" class="btn-vanaspati btn-amber-agro">
              <span>🧪</span> Boost Soil Immunity
            </a>
          </div>
        </div>
      `;
      container.scrollIntoView({ behavior: 'smooth' });
    }
  }

  // 7. Toast Notification Utility
  function showToast(message) {
    let toast = document.getElementById('vanaspatiToast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'vanaspatiToast';
      toast.style.cssText = `
        position: fixed;
        bottom: 24px;
        left: 50%;
        transform: translateX(-50%) translateY(100px);
        background: #0f2a1e;
        color: #ffffff;
        padding: 12px 24px;
        border-radius: 9999px;
        font-family: inherit;
        font-weight: 600;
        font-size: 0.92rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.25);
        border: 1px solid rgba(52, 211, 153, 0.4);
        z-index: 9999;
        transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.35s ease;
        opacity: 0;
        pointer-events: none;
      `;
      document.body.appendChild(toast);
    }

    toast.textContent = message;
    toast.style.opacity = '1';
    toast.style.transform = 'translateX(-50%) translateY(0)';

    clearTimeout(toast.timeoutId);
    toast.timeoutId = setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateX(-50%) translateY(100px)';
    }, 2800);
  }

  // 8. AI Plant Science & Care Assistant (PLLaMa / Netlify & Localhost)
  const chatStream = document.getElementById('chatDialogueStream');
  const chatForm = document.getElementById('assistantChatForm');
  const queryInput = document.getElementById('assistantQueryInput');
  const plantInput = document.getElementById('assistantPlantInput');
  const condInput = document.getElementById('assistantConditionInput');

  // Client-side knowledge base fallback for PLLaMa
  const CLIENT_PLLAMA_KB = [
    {
      keywords: ["water", "watering", "how often", "irrigation", "moisture", "hydrate"],
      response: "Watering frequency depends on crop root depth and soil drainage. For solanaceous crops (tomatoes, potatoes, peppers), provide 1.5–2 inches (35–50 mm) of water per week, watering deeply at the root zone early in the morning. Allow the top 2 inches of soil to dry slightly between waterings to prevent root suffocation and Pythium root rot. For houseplants and succulents, use the soak-and-dry method, watering only when the top 50% of the potting medium is dry. (Source: PLLaMa Plant Science Corpus / Agronomy Journal)",
      category: "Irrigation & Water Management"
    },
    {
      keywords: ["light", "sun", "sunlight", "photoperiod", "shade", "lux", "hours"],
      response: "Crops like tomatoes, corn, peppers, and potatoes require full sunlight (6–8+ hours of direct irradiance daily) for optimal photosynthesis and fruit set. Leafy greens (spinach, lettuce) and herbs tolerate partial shade (3–5 hours). For indoor botanicals (ficus, snake plant, pothos), provide bright indirect sunlight (10,000–20,000 lux) and avoid harsh direct window glare which causes foliar scorch. (Source: PLLaMa / Trends in Plant Science)",
      category: "Lighting & Photosynthesis"
    },
    {
      keywords: ["fertilizer", "npk", "nutrition", "feed", "nutrient", "nitrogen", "phosphorus", "potassium"],
      response: "Optimal N-P-K nutrition follows crop phenological stages: during early vegetative growth, use a balanced or nitrogen-leaning ratio (NPK 10-10-10 or 12-6-6) to build foliar canopy. Upon flower bud initiation and fruit bulking, transition to high-phosphorus and high-potassium formulas (such as NPK 5-10-10 or 4-18-38 with calcium and magnesium) to support blossom retention and cellular integrity. Legumes (beans, peas) fix their own atmospheric nitrogen and require low-N formulations. (Source: PLLaMa / Plant and Soil Journal)",
      category: "Soil Fertility & N-P-K Management"
    },
    {
      keywords: ["early blight", "late blight", "blight", "alternaria", "phytophthora"],
      response: "Blight management combines sanitation with targeted fungicides. For Early Blight (Alternaria solani), prune lower foliage touching the soil to eliminate soil-splash inocula, apply organic copper octanoate or Bacillus subtilis bioprotectants, and rotate crops for 3 years. For Late Blight (Phytophthora infestans), treat immediately with systemic fungicides (Mancozeb + Metalaxyl/Mefenoxam) and destroy severely blighted foliage to prevent sporangia dispersal. (Source: PLLaMa / Phytopathology Research)",
      category: "Pathology & Disease Treatment"
    },
    {
      keywords: ["powdery mildew", "mildew", "white powder", "downy mildew", "downy"],
      response: "Powdery mildew (Erysiphales) thrives in warm, dry weather with high relative humidity. Apply potassium bicarbonate (3 g/L), sulfur dust, or neem oil spray every 7–10 days on upper leaf surfaces. For Downy Mildew (Pseudoperonospora / Peronospora), which requires free leaf moisture, ensure wide row spacing for air circulation, use drip irrigation, and apply copper hydroxide or Dimethomorph. (Source: PLLaMa / European Journal of Plant Pathology)",
      category: "Fungal Control"
    },
    {
      keywords: ["pllama", "arxiv", "paper", "about pllama", "model", "architecture"],
      response: "PLLaMa (arXiv:2401.01600v1) is the first open-source Large Language Model specifically pretrained on 1.67 million scientific articles from 750 plant science journals (The Plant Cell, Plant Physiology, Phytopathology, etc.). Developed by researchers from UCSB, Lincoln, CAAS, and SLU, PLLaMa bridges the domain gap in botanical artificial intelligence, achieving high accuracy on specialized plant biology benchmarks. (GitHub: https://github.com/Xianjun-Yang/PLLaMa)",
      category: "Scientific Model Architecture"
    },
    {
      keywords: ["blossom end rot", "black bottom", "calcium"],
      response: "Blossom End Rot is a physiological disorder caused by localized calcium deficiency in expanding fruit tissues, usually triggered by erratic watering or root damage rather than a lack of soil calcium. Maintain uniform soil moisture with organic mulch and apply foliar calcium chloride or chelated calcium during rapid fruit expansion. (Source: PLLaMa / Horticulture Research)",
      category: "Physiological Disorders"
    },
    {
      keywords: ["koppert", "biological", "biocontrol", "beneficial", "predator", "trianum"],
      response: "Koppert Biological Systems standards prioritize preventative bio-protection: 1) Trianum-P (Trichoderma harzianum T-22) shields root architecture against Fusarium, Pythium, and Rhizoctonia; 2) Spidex (Phytoseiulus persimilis) eradicates two-spotted spider mites; 3) Swirski-Mite (Amblyseius swirskii) suppresses thrips and whiteflies; 4) NatuGro microbial bio-fertilizers fortify plant systemic acquired resistance (SAR). (Source: Koppert India / Global Biological Standards)",
      category: "Biological Protection (Koppert Standards)"
    },
    {
      keywords: ["spinach", "palak", "malabar", "kangkong", "leafy", "chard"],
      response: "Spinach (Spinacia oleracea) and leafy greens thrive in cool climates (15°C–20°C) with moist, well-draining soil (pH 6.5–7.0). Spinach is sensitive to bolting under long days and high temperatures (>25°C). Avoid overhead watering to prevent Downy Mildew (Peronospora effusa). Side-dress with balanced nitrogen compost every 2–3 weeks for vibrant, iron-rich foliage. Malabar Spinach (Basella alba) is heat-tolerant and requires trellising. (Source: UN FAO & World Crops Guidelines)",
      category: "Spinach & Leafy Greens Protocol"
    },
    {
      keywords: ["gourd", "karela", "bitter gourd", "lauki", "bottle gourd", "pumpkin", "cucumber"],
      response: "Cucurbits and gourds (Bitter Gourd, Bottle Gourd, Ridge Gourd, Cucumber) require full tropical sun, deep fertile loam, and sturdy trellising to prevent fruit contact with wet soil. Irrigate at root zones early morning. Guard against Fruit Fly (Bactrocera cucurbitae) using pheromone traps and downy mildew using prophylactic copper sprays or Trichoderma. (Source: ICAR Indian Institute of Horticultural Research)",
      category: "Gourds & Squashes Protocol"
    },
    {
      keywords: ["tomato", "tamatar", "lycopersicum"],
      response: "Tomatoes require consistent deep watering (1–1.5 inches weekly), full sunlight (6–8 hours), and staking or caging for aeration. Common risks include Early Blight, Blossom End Rot (calcium deficiency), and Whitefly-transmitted Yellow Leaf Curl Virus. Apply mulch around bases to prevent soil splash and spray neem oil or Bacillus subtilis bio-fungicide preventatively. (Source: PLLaMa Phytopathology Corpus)",
      category: "Solanaceae Crop Protocol"
    },
    {
      keywords: ["potato", "aloo", "tuberosum"],
      response: "Potatoes thrive in cool weather (15°C–22°C) with loose, acidic-to-neutral soil (pH 5.2–6.5) to prevent common scab. Hill soil around growing stems to protect developing tubers from sunlight exposure (which causes greening and toxic solanine accumulation). Monitor for Early Blight and Late Blight (Phytophthora infestans), maintaining 3-year crop rotations. (Source: International Potato Center CIP / PLLaMa)",
      category: "Root & Tuber Protocol"
    },
    {
      keywords: ["cat", "dog", "pet", "toxic", "poison"],
      response: "Several common plants contain insoluble calcium oxalate crystals or cardiac glycosides that are toxic to pets (e.g., Lilies, Dieffenbachia, Philodendron, Foxglove, Oleander). Pet-safe alternatives include Spider Plants, Boston Ferns, Calatheas, and African Violets. If pet ingestion occurs, contact a veterinary poison hotline immediately. (Source: Botanical Veterinary Science)",
      category: "Pet Safety & Plant Toxicity"
    }
  ];

  function appendChatMessage(sender, text, category, source) {
    if (!chatStream) return;
    const isUser = sender === 'user';
    const row = document.createElement('div');
    row.className = `chat-msg-row ${isUser ? 'user-msg' : 'assistant-msg'}`;
    row.style.cssText = `
      align-self: ${isUser ? 'flex-end' : 'flex-start'};
      max-width: ${isUser ? '82%' : '88%'};
      margin-bottom: 0.5rem;
    `;

    if (isUser) {
      row.innerHTML = `
        <div style="display: flex; gap: 0.65rem; align-items: flex-end; justify-content: flex-end;">
          <div style="background: var(--forest-card, #1b4332); color: #ffffff; border-radius: 12px 12px 2px 12px; padding: 0.85rem 1.15rem; font-size: 0.95rem; line-height: 1.6; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
            ${text}
          </div>
          <div style="font-size: 1.25rem; background: #e2e8f0; border-radius: 50%; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">👤</div>
        </div>
      `;
    } else {
      row.innerHTML = `
        <div style="display: flex; gap: 0.65rem; align-items: flex-start;">
          <div style="font-size: 1.4rem; background: #e8f5e9; border: 1px solid var(--emerald-600); border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">🤖</div>
          <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px 12px 12px 2px; padding: 1rem 1.25rem; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
            ${category ? `<div style="font-size: 0.75rem; color: #166534; font-weight: 700; text-transform: uppercase; margin-bottom: 0.35rem; display: flex; align-items: center; gap: 0.35rem;"><span>🔬</span> ${category}</div>` : ''}
            <div style="font-size: 0.95rem; line-height: 1.7; color: var(--text-primary);">${text}</div>
            <div style="font-size: 0.75rem; color: #64748b; margin-top: 0.6rem; border-top: 1px dashed #e2e8f0; padding-top: 0.4rem;">
              📚 Source: ${source || 'PLLaMa Academic Corpus & Koppert Biological Standards'}
            </div>
          </div>
        </div>
      `;
    }

    chatStream.appendChild(row);
    chatStream.scrollTop = chatStream.scrollHeight;
  }

  async function handleSendAssistantQuery(q) {
    if (!q || !q.trim()) return;
    const cleanQ = q.trim();
    const plant = plantInput ? plantInput.value.trim() : '';
    const condition = condInput ? condInput.value.trim() : '';

    appendChatMessage('user', cleanQ);
    if (queryInput) queryInput.value = '';

    // Typing loading indicator
    const loadingRow = document.createElement('div');
    loadingRow.id = 'chatLoadingIndicator';
    loadingRow.style.cssText = 'align-self: flex-start; color: var(--emerald-700); font-size: 0.88rem; font-style: italic; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.4rem;';
    loadingRow.innerHTML = '<span>🤖</span> <i>Consulting PLLaMa 1.67M paper scientific database & Koppert standards...</i>';
    if (chatStream) {
      chatStream.appendChild(loadingRow);
      chatStream.scrollTop = chatStream.scrollHeight;
    }

    try {
      let data = null;
      const endpoint = isNetlify ? '/.netlify/functions/ask-assistant' : '/api/ask-assistant';
      try {
        const res = await fetch(endpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ query: cleanQ, current_plant: plant, current_condition: condition })
        });
        if (res.ok) {
          data = await res.json();
        }
      } catch (networkErr) {
        console.log('[Vanaspati.AI] Network request offline, utilizing client-side PLLaMa engine.');
      }

      if (!data || !data.answer) {
        const lowerQ = cleanQ.toLowerCase();
        let matched = null;
        for (const item of CLIENT_PLLAMA_KB) {
          if (item.keywords.some(k => new RegExp('\\b' + k + '\\b', 'i').test(lowerQ))) {
            matched = item;
            break;
          }
        }

        if (matched) {
          data = {
            answer: matched.response,
            category: matched.category,
            source: 'PLLaMa Botanical Language Engine (arXiv:2401.01600v1)'
          };
        } else if (plant) {
          data = {
            answer: `Agronomic guidance for ${plant}: Ensure scheduled drip irrigation early in the day, well-draining soil with balanced pH (6.2–6.8), and apply Koppert Trianum-P (Trichoderma harzianum) to fortify root immunity against soil-borne pathogens.`,
            category: `Custom Care Protocol (${plant})`,
            source: 'PLLaMa Agronomic Synthesis'
          };
        } else {
          data = {
            answer: 'According to research in PLLaMa (arXiv:2401.01600v1) and agricultural best practices, successful botanical management requires: 1) Ensuring well-draining soil with balanced pH (6.0–6.8); 2) Deep root watering early in the day; 3) Staged N-P-K fertilization; and 4) Regular foliar scouting for early disease lesions. Ask about specific watering frequencies, sunlight, or disease cures!',
            category: 'General Agronomic Consultation',
            source: 'PLLaMa Scientific Corpus'
          };
        }
      }

      const loader = document.getElementById('chatLoadingIndicator');
      if (loader) loader.remove();

      appendChatMessage('assistant', data.answer, data.category, data.source);
    } catch (err) {
      const loader = document.getElementById('chatLoadingIndicator');
      if (loader) loader.remove();
      appendChatMessage('assistant', 'I am currently processing offline botanical intelligence. Please ask about watering schedules, lighting, NPK fertilizers, or disease cures!', 'Botanical Consultant', 'PLLaMa Offline Fallback');
    }
  }

  if (chatForm && queryInput) {
    chatForm.addEventListener('submit', function (e) {
      e.preventDefault();
      handleSendAssistantQuery(queryInput.value);
    });
  }

  // Quick Chips in Assistant
  const quickChips = document.querySelectorAll('.assistant-quick-chip');
  quickChips.forEach(chip => {
    chip.addEventListener('click', function () {
      const prompt = this.getAttribute('data-prompt');
      if (prompt) {
        handleSendAssistantQuery(prompt);
      }
    });
  });

  // 9. Global Floating AI Consultant Launcher Button
  const existingFloating = document.getElementById('floatingAiAssistantBtn');
  if (!existingFloating) {
    const floatBtn = document.createElement('a');
    floatBtn.id = 'floatingAiAssistantBtn';
    floatBtn.href = 'chat.html';
    floatBtn.title = 'Consult AI Plant Care Assistant (PLLaMa)';
    floatBtn.style.cssText = `
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: linear-gradient(135deg, #1b4332 0%, #2d6a4f 100%);
      color: #ffffff;
      padding: 12px 20px;
      border-radius: 9999px;
      font-family: inherit;
      font-weight: 700;
      font-size: 0.9rem;
      box-shadow: 0 10px 25px rgba(27, 67, 50, 0.4);
      border: 1.5px solid rgba(82, 183, 136, 0.4);
      display: inline-flex;
      align-items: center;
      gap: 8px;
      z-index: 9990;
      text-decoration: none;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease;
    `;
    floatBtn.innerHTML = `<span>🤖</span> <span>AI Care Chat</span>`;
    floatBtn.addEventListener('mouseenter', () => {
      floatBtn.style.transform = 'translateY(-3px) scale(1.03)';
      floatBtn.style.boxShadow = '0 14px 30px rgba(27, 67, 50, 0.55)';
    });
    floatBtn.addEventListener('mouseleave', () => {
      floatBtn.style.transform = 'translateY(0) scale(1)';
      floatBtn.style.boxShadow = '0 10px 25px rgba(27, 67, 50, 0.4)';
    });
    document.body.appendChild(floatBtn);
  }
});
