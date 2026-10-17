import urllib.request
import re
import json
import concurrent.futures

slugs = [
    ("Fusarium spp.", "Fusarium spp.", "fusarium-spp"),
    ("Black rot of carrots", "Alternaria radicina", "black-rot-of-carrots"),
    ("Bacterial soft rot, bacterial stem rot", "Pectobacterium carotovorum", "bacterial-soft-rot-bacterial-stem-rot"),
    ("Black sigatoka disease", "Mycosphaerella fijiensis", "black-sigatoka-disease"),
    ("Blight of pepper", "Phytophthora capsici", "blight-of-pepper"),
    ("Powdery mildew", "Erysiphe, Podosphaera, Oidium, Leveillula spp.", "powdery-mildew"),
    ("Damping-off", "Pythium aphanidermatum", "damping-off"),
    ("Bacterial wilt, brown rot", "Ralstonia solanacearum", "bacterial-wilt-brown-rot"),
    ("Loose smut of wheat", "Ustilago tritici", "loose-smut-of-wheat"),
    ("Angular leaf spot", "Xanthomonas fragariae", "angular-leaf-spot"),
    ("Apple collar rot", "Phytophthora cactorum", "apple-collar-rot"),
    ("Apple scab", "Venturia inaequalis", "apple-scab"),
    ("Bacterial canker of tomato", "Clavibacter michiganensis", "bacterial-canker-of-tomato"),
    ("Bacterial spot", "Xanthomonas vesicatoria", "bacterial-spot"),
    ("Black leg of seedlings", "Pythium ultimum", "black-leg-of-seedlings"),
    ("Black root rot of cucurbits", "Phomopsis sclerotioides", "black-root-rot-of-cucurbits"),
    ("Brown root rot, corky root rot", "Pyrenochaeta lycopersici", "brown-root-rot-corky-root-rot"),
    ("Cercospora leaf spot", "Cercospora spp.", "cercospora-leaf-spot"),
    ("Charcoal rot", "Macrophomina phaseolina", "charcoal-rot"),
    ("Cottony soft rot", "Sclerotinia sclerotiorum", "cottony-soft-rot"),
    ("Crazy roots, hairy roots, crown gall", "Rhizobium spp.", "crazy-roots-hairy-roots-crown-gall"),
    ("Downy mildew of Cucurbits", "Pseudoperonospora cubensis", "downy-mildew-of-cucurbits"),
    ("Dwarf bunt", "Tilletia controversa", "dwarf-bunt"),
    ("Early blight", "Alternaria solani", "early-blight"),
    ("Fusarium head blight or scab", "Fusarium graminearum", "fusarium-head-blight-or-scab"),
    ("Fusarium wilt", "Fusarium oxysporum", "fusarium-wilt"),
    ("Grape downy mildew", "Plasmopara viticola", "grape-downy-mildew"),
    ("Grapevine powdery mildew", "Erysiphe necator", "grapevine-powdery-mildew"),
    ("Gummy stem blight", "Didymella bryoniae", "gummy-stem-blight"),
    ("Leaf stripe", "Pyrenophora graminea", "leaf-stripe"),
    ("Loose smut of barley", "Ustilago nuda", "loose-smut-of-barley"),
    ("Pea blight, leaf and pod spot", "Ascochyta pisi", "pea-blight-leaf-and-pod-spot"),
    ("Phytophthora blight", "Phytophthora infestans", "phytophthora-blight"),
    ("Pierce's disease of grapevine", "Xylella fastidiosa", "pierces-disease-of-grapevine"),
    ("Pomegranate bacterial blight", "Xanthomonas axonopodis pv. punicae", "pomegranate-bacterial-blight"),
    ("Pomegranate wilt complex", "Ceratocystis fimbriata", "pomegranate-wilt-complex"),
    ("Root and crown rot of strawberry", "Pestalotiopsis clavispora", "root-and-crown-rot-of-strawberry"),
    ("Root rot of carrot", "Rhexocercosporidium carotae", "root-rot-of-carrot"),
    ("Southern blight", "Sclerotium rolfsii", "southern-blight"),
    ("Verticillium wilt", "Verticillium spp.", "verticillium-wilt"),
    ("Wheat bunt", "Tilletia tritici and Tilletia laevis", "wheat-bunt")
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch_disease(item):
    name, pathogen, slug = item
    url = f"https://www.koppert.in/disease-control/{slug}"
    result = {
        "source": "Koppert India",
        "url": url,
        "disease_name": name,
        "pathogen": pathogen,
        "slug": slug,
        "general_overview": "",
        "damage_symptoms": "",
        "life_cycle": "",
        "prevention_and_management": "",
        "biological_products": []
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8', errors='ignore')
        
        # Split by h2
        parts = re.split(r'<h[23][^>]*>', html)
        for part in parts[1:]:
            heading_end = part.find('</h')
            if heading_end == -1:
                continue
            h_text = ' '.join(re.sub(r'<[^>]+>', ' ', part[:heading_end]).split()).lower()
            body = part[heading_end:]
            body = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL)
            body = re.sub(r'<style.*?</style>', '', body, flags=re.DOTALL)
            clean_body = ' '.join(re.sub(r'<[^>]+>', ' ', body).split())
            
            # Remove footer stuff
            footer_cut = clean_body.find("Partners with Nature")
            if footer_cut != -1:
                clean_body = clean_body[:footer_cut].strip()
            learn_cut = clean_body.find("Learn more about")
            if learn_cut != -1:
                clean_body = clean_body[:learn_cut].strip()
                
            if 'general' in h_text and not result["general_overview"]:
                result["general_overview"] = clean_body
            elif 'symptom' in h_text and not result["damage_symptoms"]:
                result["damage_symptoms"] = clean_body
            elif ('life cycle' in h_text or 'appearance' in h_text) and not result["life_cycle"]:
                result["life_cycle"] = clean_body
            elif ('prevent' in h_text or 'control' in h_text or 'manage' in h_text) and not result["prevention_and_management"]:
                result["prevention_and_management"] = clean_body
                
        # Products
        prod_matches = re.findall(r'<a[^>]*href=["\']/products/disease-control/([^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL)
        prods = []
        for p_slug, p_text in prod_matches:
            c = ' '.join(re.sub(r'<[^>]+>', ' ', p_text).split())
            if c and c not in prods:
                prods.append(c)
        result["biological_products"] = prods
        
    except Exception as e:
        result["error"] = str(e)
        
    return result

print(f"Starting extraction for {len(slugs)} Koppert diseases...")
results = []
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(fetch_disease, item) for item in slugs]
    for fut in concurrent.futures.as_completed(futures):
        res = fut.result()
        print(f"Done: {res['disease_name']} (Symptoms len: {len(res['damage_symptoms'])}, Prev len: {len(res['prevention_and_management'])})")
        results.append(res)

with open('scratch/koppert_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"\nSuccessfully extracted all {len(results)} Koppert diseases to scratch/koppert_extracted.json!")
