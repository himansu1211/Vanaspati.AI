"""
Plant Disease Imagery Augmentation Pipeline
Addresses real-world environmental shifts (field lighting, sunlight glare, camera orientation, lens blur)
to drastically improve CNN generalization on unconstrained smartphone captures.
"""

from torchvision import transforms
from typing import Tuple

def get_train_augmentations(img_size: int = 256) -> transforms.Compose:
    """
    State-of-the-art augmentation pipeline for training robust leaf disease classifiers.
    Simulates varied field conditions, phone angles, shadows, and leaf flutter.
    """
    return transforms.Compose([
        transforms.Resize((img_size, img_size)),
        transforms.RandomResizedCrop(img_size, scale=(0.8, 1.0), ratio=(0.9, 1.1)),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomVerticalFlip(p=0.3),
        transforms.RandomRotation(degrees=30),
        transforms.RandomAffine(
            degrees=0,
            translate=(0.08, 0.08),
            scale=(0.95, 1.05),
            shear=8
        ),
        transforms.ColorJitter(
            brightness=0.25,
            contrast=0.25,
            saturation=0.25,
            hue=0.05
        ),
        transforms.RandomPerspective(distortion_scale=0.2, p=0.4),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

def get_val_augmentations(img_size: int = 256) -> transforms.Compose:
    """
    Deterministic preprocessing pipeline for evaluation & inference.
    """
    return transforms.Compose([
        transforms.Resize((img_size, img_size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

def get_inference_transforms(img_size: int = 256) -> transforms.Compose:
    """
    Fast inference transform for real-time web uploads.
    """
    return transforms.Compose([
        transforms.Resize(img_size),
        transforms.CenterCrop(img_size),
        transforms.ToTensor()
    ])
