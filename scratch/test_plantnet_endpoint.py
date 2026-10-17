import requests
import json

test_img_path = 'Data-processed/vegetable_samples/Tomato_1.jpg'

print(f"Testing /identify/plantnet with {test_img_path}...")
with open(test_img_path, 'rb') as f:
    files = {'file': ('Tomato_1.jpg', f, 'image/jpeg')}
    data = {'organ': 'fruit'}
    resp = requests.post('http://127.0.0.1:10000/identify/plantnet', files=files, data=data)
    print("STATUS:", resp.status_code)
    print("RESPONSE:", json.dumps(resp.json(), indent=2))

print("\nTesting /identify/multi-source with Tomato_1.jpg...")
with open(test_img_path, 'rb') as f:
    files = {'file': ('Tomato_1.jpg', f, 'image/jpeg')}
    data = {'organ': 'fruit'}
    resp = requests.post('http://127.0.0.1:10000/identify/multi-source', files=files, data=data)
    print("STATUS:", resp.status_code)
    print("RESPONSE:", json.dumps(resp.json(), indent=2))
