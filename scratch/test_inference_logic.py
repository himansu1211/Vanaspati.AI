import numpy as np
from PIL import Image

def test_inference(pil_img):
    arr = np.array(pil_img.resize((128, 128)), dtype=np.float32)
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]

    # 1. Non-background check
    non_bg = ~((r > 215) & (g > 215) & (b > 215))
    if np.sum(non_bg) < (128 * 128 * 0.05):
        return {"class": "Background_without_leaves", "plant_identified": False, "plant": None}

    r_sub = r[non_bg]
    g_sub = g[non_bg]
    b_sub = b[non_bg]

    # 2. Ripe tomato fruit check
    red_tomato_mask = (r_sub > 130) & (g_sub < 100) & (b_sub < 90)
    red_pct = np.sum(red_tomato_mask) / len(r_sub)
    if red_pct > 0.45 and np.mean(r_sub) > 170 and np.mean(g_sub) < 115:
        return {"class": "Tomato___healthy", "plant_identified": True, "plant": "Tomato"}

    # 3. Genuine Rose check
    rose_petal_mask = (r_sub > 150) & (g_sub < 75) & (b_sub < 100)
    has_rose_petals = (np.sum(rose_petal_mask) / len(r_sub)) > 0.18
    green_mask = (g_sub > r_sub * 1.05) & (g_sub > b_sub * 1.05) & (g_sub > 40)
    has_green = (np.sum(green_mask) / len(r_sub)) > 0.10
    if has_rose_petals and has_green:
        return {"class": "Rose___healthy", "plant_identified": True, "plant": "Rose"}

    # 4. Foliage presence check
    green_foliage_mask = (g > r * 0.9) & (g > b * 0.9) & (g > 35) & (g < 235)
    foliage_ratio = np.sum(green_foliage_mask) / (128 * 128)
    
    if foliage_ratio < 0.08:
        return {"class": "Background_without_leaves", "plant_identified": False, "plant": None, "reason": "No leaf foliage"}

    return {"class": "DeepLeafInference", "plant_identified": "Conditional", "plant": "Depends on PyTorch Confidence >= 0.95"}

samples = [
    'Data-processed/vegetable_samples/Tomato_1.jpg',
    'Data-processed/vegetable_samples/Tomato_2.jpg',
    'Data-processed/vegetable_samples/Potato_1.jpg',
    'Data-processed/vegetable_samples/Beans_1.jpg'
]

for s in samples:
    img = Image.open(s).convert('RGB')
    res = test_inference(img)
    print(f"{s} -> {res}")
