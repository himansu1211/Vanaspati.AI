import sys
from pathlib import Path
from PIL import Image
import torch
import numpy as np

sys.path.append(r'c:\Users\himan\Downloads\CropcareAI-main\image-based-ident-api')
from main import MODEL, VEG_MODEL, PLANT_VILLAGE_CLASSES, t_veg
from torchvision import transforms

transform_pt = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
])

sample_dir = Path(r'c:\Users\himan\Downloads\CropcareAI-main\public\images\sample_leaves')
for f in sorted(sample_dir.glob('*.jpg')):
    print(f"\n=================== {f.name} ===================")
    img = Image.open(f).convert('RGB')
    
    # ResNet9
    t_m = transform_pt(img).unsqueeze(0)
    with torch.no_grad():
        out = MODEL(t_m)
        probs = torch.softmax(out, dim=1)[0]
        top_k = torch.topk(probs, 5)
        print("ResNet-9 Top 5:")
        for idx, (p, i) in enumerate(zip(top_k.values, top_k.indices)):
            print(f"  {idx+1}. {PLANT_VILLAGE_CLASSES[i.item()]}: {p.item():.4f}")
            
    # ViT
    if VEG_MODEL is not None:
        t_v = t_veg(img).unsqueeze(0)
        with torch.no_grad():
            out_v = VEG_MODEL(t_v).logits
            probs_v = torch.softmax(out_v, dim=1)[0]
            top_k_v = torch.topk(probs_v, 3)
            print("ViT Top 3:")
            for idx, (p, i) in enumerate(zip(top_k_v.values, top_k_v.indices)):
                print(f"  {idx+1}. {VEG_MODEL.config.id2label[i.item()]}: {p.item():.4f}")

    arr = np.array(img.resize((128, 128)), dtype=np.float32)
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    green = (g > r * 1.05) & (g > b * 1.05) & (g > 35)
    necrotic = (r < 85) & (g < 90) & (b < 75) & (r + g + b > 35)
    rust = (r > 155) & (r > g * 1.3) & (b < 60)
    scab = (r < 100) & (g < 115) & (b < 60) & (g > b * 1.2)
    print(f"Metrics: green={np.mean(green):.3f}, necrotic={np.mean(necrotic):.3f}, rust={np.mean(rust):.3f}, scab={np.mean(scab):.3f}")
