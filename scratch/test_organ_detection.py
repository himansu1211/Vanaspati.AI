from PIL import Image
import numpy as np

def analyze_specimen(path):
    img = Image.open(path).convert('RGB')
    arr = np.array(img.resize((128, 128)), dtype=np.float32)
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    
    # Exclude white/grey background
    bg_mask = (r > 215) & (g > 215) & (b > 215)
    non_bg = ~bg_mask
    if np.sum(non_bg) < (128 * 128 * 0.05):
        return "Background/Blank", 0.0
        
    r_sub = r[non_bg]
    g_sub = g[non_bg]
    b_sub = b[non_bg]
    
    r_m = np.mean(r_sub)
    g_m = np.mean(g_sub)
    b_m = np.mean(b_sub)
    
    # Check for green foliage
    green_mask = (g_sub > r_sub * 1.05) & (g_sub > b_sub * 1.05) & (g_sub > 40)
    green_pct = np.sum(green_mask) / len(r_sub)
    
    # Check for ripe red tomato (bright red with low blue/green)
    red_tomato_mask = (r_sub > 130) & (g_sub < 100) & (b_sub < 90)
    red_tomato_pct = np.sum(red_tomato_mask) / len(r_sub)
    
    # Check for potato tuber (buff/khaki/tan color: r > g > b, moderate saturation)
    potato_mask = (r_sub > 120) & (g_sub > 100) & (b_sub > 60) & (r_sub > g_sub) & (g_sub > b_sub) & ((r_sub - b_sub) > 25) & (r_sub < 225)
    potato_pct = np.sum(potato_mask) / len(r_sub)
    
    print(f"File: {path}")
    print(f"   Green Leaf %: {green_pct*100:.1f}%")
    print(f"   Red Fruit %:  {red_tomato_pct*100:.1f}%")
    print(f"   Potato %:     {potato_pct*100:.1f}%")
    print(f"   Mean RGB:     [{r_m:.1f}, {g_m:.1f}, {b_m:.1f}]")
    
    if green_pct > 0.40:
        return "Foliage/Leaf", green_pct
    elif red_tomato_pct > 0.40:
        return "Tomato Fruit", red_tomato_pct
    elif potato_pct > 0.40:
        return "Potato Tuber", potato_pct
    else:
        return "Uncertain", 0.0

for p in [
    'Data-processed/vegetable_samples/Tomato_1.jpg',
    'Data-processed/vegetable_samples/Tomato_2.jpg',
    'Data-processed/vegetable_samples/Potato_1.jpg',
    'Data-processed/vegetable_samples/Potato_2.jpg',
    'Data-processed/vegetable_samples/Capsicum_1.jpg',
    'Data-processed/vegetable_samples/Beans_1.jpg'
]:
    res, conf = analyze_specimen(p)
    print(f"   --> Detected: {res} ({conf*100:.1f}%)\n")
