import urllib.request
import json
from pathlib import Path

url = 'https://aislyn.in/admin/admin/farmly_api.php?slug=plant-identification-software'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read().decode('utf-8'))
    print("Success! Keys in response:", data.keys() if isinstance(data, dict) else len(data))
    
    out_file = Path(r'c:\Users\himan\Downloads\CropcareAI-main\scratch\farmlyt_blog.json')
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Saved to:", out_file)
    
    # Print high level summary
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, str):
                print(f"{k}: {v[:100]}...")
            else:
                print(f"{k}: {type(v)}")
except Exception as e:
    print("Error:", e)
