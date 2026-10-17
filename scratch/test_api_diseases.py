import urllib.request
import urllib.parse
import json

test_names = [
    'Angular leaf spot', 
    'Aster Yellows', 
    'Fire Blight', 
    'Blight of pepper', 
    'Rose___Black_spot',
    'Powdery mildew',
    'Panama Disease (Fusarium Wilt)'
]

for name in test_names:
    url = f"http://localhost:4000/api/diseases/details?name={urllib.parse.quote(name)}"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"OK [200] -> '{name}': {data.get('disease_name')} | Pathogen: {data.get('scientific_name')}")
    except Exception as e:
        print(f"FAIL -> '{name}': {e}")
