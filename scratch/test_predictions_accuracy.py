import requests
import json
import os

test_imgs = [
    'Data-processed/vegetable_samples/Tomato_1.jpg',
    'Data-processed/vegetable_samples/Potato_1.jpg',
    'Data-processed/vegetable_samples/Corn_1.jpg',
    'Data-processed/vegetable_samples/Capsicum_1.jpg'
]

for img_p in test_imgs:
    if os.path.exists(img_p):
        with open(img_p, 'rb') as f:
            resp = requests.post('http://127.0.0.1:10000/predict', files={'file': f})
            print(f"=== {img_p} ===")
            print("Status:", resp.status_code)
            data = resp.json()
            print("Response:", json.dumps(data, indent=2))
            
            # Now test backend disease details
            b_url = f"http://localhost:4000/api/diseases/details?name={data['class_name']}&plant_identified={str(data.get('plant_identified', False)).lower()}"
            b_resp = requests.get(b_url)
            print("Backend details status:", b_resp.status_code)
            b_data = b_resp.json()
            print("Plant Name in Backend:", b_data.get('plant_name'))
            print("Plant Identified in Backend:", b_data.get('plant_identified'))
            print()
