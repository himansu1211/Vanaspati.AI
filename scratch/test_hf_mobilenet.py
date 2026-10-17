from transformers import AutoModelForImageClassification
from PIL import Image
from pathlib import Path
import torch
from torchvision import transforms

model_id = 'linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification'
model = AutoModelForImageClassification.from_pretrained(model_id).eval()

t = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

sample_dir = Path(r'c:\Users\himan\Downloads\CropcareAI-main\public\images\sample_leaves')
for f in sorted(sample_dir.glob('*.jpg')):
    img = Image.open(f).convert('RGB')
    tensor = t(img).unsqueeze(0)
    with torch.no_grad():
        outputs = model(tensor)
        probs = torch.softmax(outputs.logits, dim=1)[0]
        top3 = torch.topk(probs, 3)
        print(f"\nImage: {f.name}")
        for p, i in zip(top3.values, top3.indices):
            print(f"  {model.config.id2label[i.item()]}: {p.item():.4f}")
