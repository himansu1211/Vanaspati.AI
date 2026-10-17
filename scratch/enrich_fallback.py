import json
import re

with open('backend/data/diseaseFallback.json', 'r', encoding='utf-8') as f:
    existing_fallback = json.load(f)

with open('Data-processed/extracted_plant_diseases.json', 'r', encoding='utf-8') as f:
    extracted = json.load(f)

def clean_sentence_list(text, default_items):
    if not text:
        return default_items
    # split by punctuation
    sentences = [s.strip() for s in re.split(r'\. |\; |\n', text) if len(s.strip()) > 15]
    if len(sentences) >= 4:
        return {f"k{i+1}": sentences[i] for i in range(4)}
    elif len(sentences) > 0:
        res = {}
        for i, s in enumerate(sentences[:4]):
            res[f"k{i+1}"] = s
        for i in range(len(sentences), 4):
            res[f"k{i+1}"] = default_items.get(f"k{i+1}", default_items.get(f"s{i+1}", "Maintain field sanitation and crop health."))
        return res
    return default_items

added_count = 0
for d in extracted:
    name = d["disease_name"]
    # generate key like "Wheat___Loose_smut" or "Carrot___Black_rot"
    host = d.get("host_plants", "General Crop").split(",")[0].split("(")[0].strip()
    host_slug = re.sub(r'[^a-zA-Z0-9]', '_', host).strip('_')
    disease_slug = re.sub(r'[^a-zA-Z0-9]', '_', name).strip('_')
    key = f"{host_slug}___{disease_slug}"
    
    # check if key or variant already in fallback
    if key in existing_fallback or name in existing_fallback:
        continue
        
    symptoms = clean_sentence_list(d.get("damage_symptoms", ""), {
        "s1": "Leaf spots, wilting, or necrotic lesions appearing on foliage and stems.",
        "s2": "Stunted vegetative growth and reduced photosynthetic vigor.",
        "s3": "Premature leaf chlorosis, yellowing, and leaf drop.",
        "s4": "Blemishes, corky scars, or rots on harvested plant organs and fruit."
    })
    
    causes = clean_sentence_list(d.get("life_cycle", "") or d.get("pathogen", ""), {
        "c1": f"Infection caused by pathogenic organism {d.get('pathogen', 'pathogen')}.",
        "c2": "High relative humidity and extended periods of free surface leaf moisture.",
        "c3": "Soil compaction, poor field drainage, or persistent infected crop residues.",
        "c4": "Dissemination by wind currents, rain splash, irrigation water, or insect vectors."
    })
    
    prevention = clean_sentence_list(d.get("prevention_and_management", ""), {
        "p1": "Plant certified disease-free and disease-resistant crop cultivars.",
        "p2": "Implement a 3 to 4 year crop rotation with non-host botanical families.",
        "p3": "Optimize plant spacing and pruning to facilitate rapid drying air circulation.",
        "p4": "Eradicate and safely dispose of infected crop residues and border weed hosts."
    })
    
    products_text = d.get("biological_products", "")
    bio_items = [p.strip() for p in re.split(r'[,;]\s*', products_text) if len(p.strip()) > 3]
    
    organic = {
        "org1": bio_items[0] if len(bio_items) > 0 else "Koppert Trianum-P (Trichoderma harzianum T-22 bio-fungicide drench).",
        "org2": bio_items[1] if len(bio_items) > 1 else "Koppert Veni GoKlean / Bacillus subtilis bio-protection foliar spray.",
        "org3": bio_items[2] if len(bio_items) > 2 else "Cold-pressed Neem Seed Kernel Extract (NSKE 5%) or horticultural botanical oil.",
        "org4": "Potassium bicarbonate spray (5 g/L) to alter leaf surface pH and suppress pathogens."
    }
    
    fertilizer = {
        "f1": "Balanced N-P-K plant nutrition tailored to crop stage; avoid excessive nitrogen.",
        "f2": "Apply Potassium (K) (Sulfate of Potash) to reinforce plant vascular tissue and cell wall rigidity.",
        "f3": "Supplement with soluble Calcium (Calcium Nitrate) and Silicon to thicken leaf epidermal barriers.",
        "f4": "Incorporate well-decomposed organic compost to enrich beneficial soil microbial antagonists."
    }
    
    pesticides = {
        "pf1": bio_items[0] if len(bio_items) > 0 else "Copper Hydroxide or Bordeaux Mixture (1%) protective spray.",
        "pf2": "Mancozeb (0.2%) or Chlorothalonil contact protectant before anticipated wet weather.",
        "pf3": "Azoxystrobin or Difenoconazole systemic treatment where permitted.",
        "pf4": "Soil drench with bio-inoculant Trichoderma harzianum or Streptomyces lydicus."
    }
    
    control = {
        "dc1": "Prune out and immediately incinerate or bury visibly infected tissues.",
        "dc2": "Sterilize all pruning shears, knives, and equipment with 70% isopropyl alcohol.",
        "dc3": "Avoid overhead sprinkler irrigation; irrigate strictly at the root zone via drip lines.",
        "dc4": "Apply targeted bio-fungicide or bactericide at earliest detection of initial symptoms."
    }
    
    entry = {
        "idName": key,
        "plant_name": f"{host} ({d.get('host_plants', '')[:40]})",
        "disease_name": name,
        "pathogen_type": d.get("category", "Biotic Disease"),
        "scientific_name": d.get("pathogen", "Pathogenic agent"),
        "severity": "Moderate to High",
        "disease_symptoms": {f"s{i+1}": list(symptoms.values())[i] for i in range(min(4, len(symptoms)))},
        "disease_causes": {f"c{i+1}": list(causes.values())[i] for i in range(min(4, len(causes)))},
        "disease_prevention": {f"p{i+1}": list(prevention.values())[i] for i in range(min(4, len(prevention)))},
        "fertilizer_recommendation": fertilizer,
        "pesticides_and_fungicides": pesticides,
        "organic_remedies": organic,
        "disease_control": control,
        "source": d.get("source", "Koppert / Britannica"),
        "reference_url": d.get("url", "")
    }
    
    existing_fallback[key] = entry
    # Also add canonical name as key for direct lookup
    if name not in existing_fallback:
        existing_fallback[name] = entry
    added_count += 1

print(f"Added {added_count} newly formatted disease entries into diseaseFallback.json!")
print(f"Total entries now: {len(existing_fallback)}")

with open('backend/data/diseaseFallback.json', 'w', encoding='utf-8') as f:
    json.dump(existing_fallback, f, indent=2, ensure_ascii=False)

print("backend/data/diseaseFallback.json updated successfully!")
