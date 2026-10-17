"""
CLI Pipeline: Modular training and fine-tuning pipeline for Plant Disease ResNet9 model
Replaces plant-disease-classification-resnet-99-2.ipynb with structured, checkpointed execution.
Usage:
    python -m src.pipelines.train_disease_model [--epochs 10] [--batch-size 32] [--lr 0.0001]
"""

import argparse
import sys
from pathlib import Path
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder

BASE_DIR = Path(__file__).resolve().parent.parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.models.disease_classifier import ResNet9, PlantDiseaseTrainer
from src.models.augmentations import get_train_augmentations, get_val_augmentations
from src.config import DISEASE_CLASSES, BASE_DIR, APP_MODELS_DIR

def main():
    parser = argparse.ArgumentParser(description="Train/Fine-tune Plant Disease ResNet9 Model")
    parser.add_argument("--epochs", type=int, default=5, help="Number of training epochs")
    parser.add_argument("--batch-size", type=int, default=32, help="DataLoader batch size")
    parser.add_argument("--lr", type=float, default=1e-4, help="Learning rate")
    parser.add_argument("--data-dir", type=str, default=str(BASE_DIR / "dataset" / "plant_diseases"), help="Dataset directory")
    args = parser.parse_args()

    print("=" * 60)
    print("Vanaspati.AI - Plant Disease ResNet9 Training Pipeline")
    print("=" * 60)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Hardware compute device: {device}")

    data_path = Path(args.data_dir)
    if not data_path.exists() or len(list(data_path.iterdir())) == 0:
        print(f"[Notice] Dataset folder at {data_path} is empty or unpopulated.")
        print("To train from scratch, place PlantVillage / Kaggle images into class folders.")
        print("Verifying current pre-trained model status instead...")
        trainer = PlantDiseaseTrainer()
        print(f"Pre-trained model loaded successfully: {len(trainer.classes)} classes supported.")
        return

    # Dataset loader
    train_transform = get_train_augmentations(256)
    dataset = ImageFolder(root=str(data_path), transform=train_transform)
    loader = DataLoader(dataset, batch_size=args.batch_size, shuffle=True, num_workers=0)

    model = ResNet9(3, len(DISEASE_CLASSES)).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr, weight_decay=1e-4)

    print(f"Beginning training across {len(dataset)} images for {args.epochs} epochs...")
    model.train()
    for epoch in range(args.epochs):
        running_loss = 0.0
        correct = 0
        total = 0
        for i, (images, labels) in enumerate(loader):
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            _, preds = torch.max(outputs, 1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)

        acc = (correct / total) * 100 if total > 0 else 0
        print(f"Epoch [{epoch+1}/{args.epochs}] Loss: {running_loss/len(loader):.4f} | Train Acc: {acc:.2f}%")

    out_path = APP_MODELS_DIR / "plant_disease_model.pth"
    torch.save(model.state_dict(), out_path)
    print(f"Model saved to {out_path}")

if __name__ == "__main__":
    main()
