from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
from pathlib import Path
import torch

model_id = 'rodynaemad/plant-disease-dinov2-small'
processor = AutoImageProcessor.from_pretrained(model_id)
model = AutoModelForImageClassification.from_pretrained(model_id).eval()

sample_dir = Path(r'c:\Users\himan\Downloads\CropcareAI-main\public\images\sample_leaves')
for f in sorted(sample_dir.glob('*.jpg')):
    img = Image.open(f).convert('RGB')
    inputs = processor(images=img, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)[0]
        top3 = torch.topk(probs, 3)
        print(f"\nImage: {f.name}")
        for p, i in zip(top3.values, top3.indices):
            print(f"  {model.config.id2label[i.item()]}: {p.item():.4f}")
