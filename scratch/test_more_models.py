from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
from pathlib import Path
import torch

for m_id in ['neghani/plantvillage-mobilenetv2', 'kimcomehome/plantvillage-vit-leaf-disease']:
    try:
        print(f"\n=================== Testing {m_id} ===================")
        processor = AutoImageProcessor.from_pretrained(m_id)
        model = AutoModelForImageClassification.from_pretrained(m_id).eval()
        sample_dir = Path(r'c:\Users\himan\Downloads\CropcareAI-main\public\images\sample_leaves')
        for f in sorted(sample_dir.glob('*.jpg')):
            img = Image.open(f).convert('RGB')
            inputs = processor(images=img, return_tensors="pt")
            with torch.no_grad():
                outputs = model(**inputs)
                probs = torch.softmax(outputs.logits, dim=1)[0]
                top2 = torch.topk(probs, 2)
                p1, i1 = top2.values[0].item(), top2.indices[0].item()
                print(f"  {f.name:25} -> {model.config.id2label[i1]} ({p1:.3f})")
    except Exception as e:
        print(f"Error {m_id}: {e}")
