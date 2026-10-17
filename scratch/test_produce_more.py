from PIL import Image
from pathlib import Path
import sys
sys.path.append(r'c:\Users\himan\Downloads\CropcareAI-main\scratch')
from test_prototype import run_prototype_inference
from transformers import AutoModelForImageClassification
from torchvision import transforms

m_veg = AutoModelForImageClassification.from_pretrained('dima806/fruit_vegetable_image_detection').eval()
t_veg = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

veg_dir = Path(r'c:\Users\himan\Downloads\CropcareAI-main\scratch\veg_repo\Test_Dataset')
for name in ['Tomato_1.jpg', 'Tomato_2.jpg', 'Potato_1.jpg', 'Potato_2.jpg', 'Peas_1.jpg', 'Peas_2.jpg', 'Onion_1.jpg', 'Onion_2.jpg']:
    p = veg_dir / name
    if p.exists():
        img = Image.open(p).convert('RGB')
        res = run_prototype_inference(img, m_veg, t_veg)
        print(f"{name:15} -> {res['class_name']:25} | plant: {str(res['plant_name']):15} | id: {res['plant_identified']}")
