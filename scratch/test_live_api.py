import requests
from pathlib import Path

endpoint = "http://127.0.0.1:10000/predict"

def test_file(path_str):
    p = Path(path_str)
    if not p.exists():
        print(f"File not found: {p}")
        return
    with open(p, "rb") as f:
        resp = requests.post(endpoint, files={"file": (p.name, f, "image/jpeg")})
    data = resp.json()
    print(f"{p.name:25} -> {data.get('class_name'):28} | plant: {str(data.get('plant_name')):15} | id: {str(data.get('plant_identified')):5} | conf: {data.get('confidence')}")

print("--- Testing Sample Leaves & Pathology ---")
for f in sorted(Path(r'c:\Users\himan\Downloads\CropcareAI-main\public\images\sample_leaves').glob('*.jpg')):
    test_file(str(f))

print("\n--- Testing Vegetables & Produce ---")
for name in ['Beans_1.jpg', 'Beetroot_1.jpg', 'Bitterguard_1.jpg', 'Brinjal_1.jpg', 'Cabbage_1.jpg', 'Capsicum_1.jpg', 'Carrot_1.jpg', 'Cauliflower_1.jpg', 'Corn_1.jpg', 'Garlic_1.jpg', 'Tomato_1.jpg', 'Potato_1.jpg', 'Peas_1.jpg', 'Onion_1.jpg']:
    p = Path(r'c:\Users\himan\Downloads\CropcareAI-main\scratch\veg_repo\Test_Dataset') / name
    test_file(str(p))

print("\n--- Testing Non-Leaf / Screenshot ---")
screenshot = Path(r'C:\Users\himan\.gemini\antigravity-ide\brain\07b2b30b-6d39-4d78-a302-45e29e6de70d\.user_uploaded\media_1792189022769.png')
test_file(str(screenshot))
