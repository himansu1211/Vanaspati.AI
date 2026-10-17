import torch
from torchvision import transforms
from PIL import Image
import numpy as np
import os
import sys

# Test images
test_imgs = [
    'Data-processed/vegetable_samples/Tomato_1.jpg',
    'Data-processed/vegetable_samples/Capsicum_1.jpg',
    'Data-processed/vegetable_samples/Beans_1.jpg',
    'Data-processed/vegetable_samples/Potato_1.jpg'
]

# Check YOLO
try:
    from ultralytics import YOLO
    yolo_model = YOLO('image-based-ident-api/models/vegetable_yolov8n.pt')
    print("YOLO model loaded.")
except Exception as e:
    print("YOLO load error:", e)
    yolo_model = None

for p in test_imgs:
    if os.path.exists(p):
        print(f"\n--- Testing {p} ---")
        if yolo_model:
            results = yolo_model(p, conf=0.35, verbose=False)
            boxes = results[0].boxes
            if len(boxes) > 0:
                best_box = max(boxes, key=lambda b: float(b.conf[0].item()))
                cls_id = int(best_box.cls[0].item())
                conf = float(best_box.conf[0].item())
                veg_name = yolo_model.names[cls_id]
                print(f"   YOLO Result: {veg_name} (conf: {conf*100:.1f}%)")
            else:
                print("   YOLO Result: No confident detection.")
