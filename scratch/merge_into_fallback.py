import json

with open('backend/data/diseaseFallback.json', 'r', encoding='utf-8') as f:
    existing_fallback = json.load(f)

print(f"Current entries in diseaseFallback.json: {len(existing_fallback)}")

with open('Data-processed/extracted_plant_diseases.json', 'r', encoding='utf-8') as f:
    extracted = json.load(f)

print(f"Extracted entries: {len(extracted)}")

# Let's map extracted entries to the fallback format if missing
# Fallback format:
# {
#   "disease_name": ...,
#   "plant_type": ...,
#   "condition_class": ...,
#   "pathogen_cause": ...,
#   "visual_symptoms": ...,
#   "causes": ...,
#   "prevention": ...,
#   "fertilizers": ...,
#   "pesticides_insecticides": ...,
#   "cure_steps": [...]
# }

existing_keys = {item.get("condition_disease_name", item.get("disease_name", "")).strip().lower(): item for item in existing_fallback}

added_count = 0
for d in extracted:
    name = d["disease_name"]
    name_clean = name.strip().lower()
    if name_clean not in existing_keys:
        # Build entry
        new_entry = {
            "disease_name": name,
            "condition_disease_name": name,
            "plant_common_name": d.get("host_plants", "Multiple Agricultural & Horticultural Crops").split(",")[0].strip(),
            "plant_type": "Crop / Horticultural",
            "botanical_name": "Various",
            "organ_category": "Foliage / Vascular / Stem / Fruit",
            "condition_class": d.get("category", "Biotic Disease"),
            "pathogen_cause": d.get("pathogen", "Pathogen"),
            "visual_symptoms": d.get("damage_symptoms", "Necrotic spotting, wilting, or lesions."),
            "causes": f"Infection by {d.get('pathogen')}. {d.get('life_cycle', '')[:300]}",
            "prevention": d.get("prevention_and_management", "Crop rotation, sanitation, resistant varieties."),
            "fertilizers": "Balanced N-P-K nutrition, avoid excess nitrogen, supplement with calcium and potassium to enhance cell wall strength.",
            "pesticides_insecticides": d.get("biological_products", "Bio-fungicides and approved protective sprays."),
            "cure_steps": [
                "Isolate or prune visibly infected tissue immediately and dispose away from fields.",
                d.get("prevention_and_management", "Apply preventive cultural measures.")[:150],
                f"Apply biological or chemical control agents: {d.get('biological_products', 'Registered treatments')[:150]}",
                "Sanitize all farm tools, shears, and footwear with disinfectant."
            ],
            "source": d.get("source", "Koppert / Britannica"),
            "reference_url": d.get("url", "")
        }
        existing_fallback.append(new_entry)
        existing_keys[name_clean] = new_entry
        added_count += 1

print(f"Added {added_count} new unique diseases to diseaseFallback.json!")
print(f"Total entries now: {len(existing_fallback)}")

with open('backend/data/diseaseFallback.json', 'w', encoding='utf-8') as f:
    json.dump(existing_fallback, f, indent=2, ensure_ascii=False)

print("Updated backend/data/diseaseFallback.json successfully.")
