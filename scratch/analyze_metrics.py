import sys
from pathlib import Path
from PIL import Image
import numpy as np

def analyze(img_path):
    img = Image.open(img_path).convert('RGB')
    arr = np.array(img.resize((128, 128)), dtype=np.float32)
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    
    # Masks
    green = (g > r * 1.05) & (g > b * 1.05) & (g > 35)
    necrotic = (r < 85) & (g < 90) & (b < 75) & (r + g + b > 35)
    rust = (r > 145) & (r > g * 1.25) & (b < 80)
    scab = (r < 100) & (g < 115) & (b < 60) & (g > b * 1.15) & ~green
    powder = (r > 170) & (g > 175) & (b > 165) & (r < 235) & (g < 235)
    yellow_chlorosis = (r > 135) & (g > 135) & (b < 100) & (np.abs(r - g) < 40)
    
    # Edge/texture variance in green
    dx = np.diff(g, axis=1)
    dy = np.diff(g, axis=0)
    grad_var = np.var(dx) + np.var(dy)
    
    print(f"{Path(img_path).name:24} | grn:{np.mean(green):.3f} | nec:{np.mean(necrotic):.3f} | rst:{np.mean(rust):.3f} | scb:{np.mean(scab):.3f} | pwd:{np.mean(powder):.3f} | yel:{np.mean(yellow_chlorosis):.3f} | gvar:{grad_var:.1f}")

print("--- Sample Leaves ---")
for p in sorted(Path(r'c:\Users\himan\Downloads\CropcareAI-main\public\images\sample_leaves').glob('*.jpg')):
    analyze(p)

print("\n--- Test Produce / Veg ---")
for p in sorted(Path(r'c:\Users\himan\Downloads\CropcareAI-main\scratch\veg_repo\Test_Dataset').glob('*_1.jpg'))[:10]:
    analyze(p)
