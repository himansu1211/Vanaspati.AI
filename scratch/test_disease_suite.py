import sys
from pathlib import Path
from PIL import Image

sys.path.append(r'c:\Users\himan\Downloads\CropcareAI-main\image-based-ident-api')
from main import run_disease_inference

print("--- Testing Sample Leaves ---")
sample_dir = Path(r'c:\Users\himan\Downloads\CropcareAI-main\public\images\sample_leaves')
for f in sorted(sample_dir.glob('*.jpg')):
    img = Image.open(f)
    res = run_disease_inference(img)
    print(f"{f.name:25} -> {res['class_name']:35} | plant: {str(res['plant_name']):15} | id: {res['plant_identified']} | conf: {res['confidence']}")

print("\n--- Testing Vegetables from Test_Dataset ---")
veg_dir = Path(r'c:\Users\himan\Downloads\CropcareAI-main\scratch\veg_repo\Test_Dataset')
for f in sorted(veg_dir.glob('*_1.jpg'))[:10]:
    img = Image.open(f)
    res = run_disease_inference(img)
    print(f"{f.name:25} -> {res['class_name']:35} | plant: {str(res['plant_name']):15} | id: {res['plant_identified']} | conf: {res['confidence']}")
