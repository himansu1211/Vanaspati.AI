"""
CLI Pipeline: Train and evaluate Crop Recommendation model
Replaces ad-hoc Crop_Recommendation_Model.ipynb with reproducible, automated training.
Usage:
    python -m src.pipelines.train_crop_model [--n-estimators 100] [--test-size 0.2]
"""

import argparse
import sys
from pathlib import Path

# Add project root to path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.models.crop_recommender import CropRecommendationTrainer

def main():
    parser = argparse.ArgumentParser(description="Train Crop Recommendation Model")
    parser.add_argument("--n-estimators", type=int, default=100, help="Number of trees in forest")
    parser.add_argument("--test-size", type=float, default=0.2, help="Validation test split ratio")
    parser.add_argument("--random-state", type=int, default=42, help="Random seed for reproducibility")
    parser.add_argument("--save", action="store_true", default=True, help="Save model checkpoint")
    args = parser.parse_args()

    print("=" * 60)
    print("Vanaspati.AI - Crop Recommendation Training Pipeline")
    print("=" * 60)

    trainer = CropRecommendationTrainer(
        n_estimators=args.n_estimators,
        random_state=args.random_state
    )
    metrics = trainer.train(test_size=args.test_size)

    print("\nTraining Results:")
    print(f"  • Test Accuracy:       {metrics['test_accuracy'] * 100:.2f}%")
    print(f"  • 5-Fold CV Accuracy:  {metrics['cv_mean_accuracy'] * 100:.2f}% (+/- {metrics['cv_std'] * 100:.2f}%)")
    print(f"  • Train Samples:       {metrics['num_train_samples']}")
    print(f"  • Test Samples:        {metrics['num_test_samples']}")
    print("\nFeature Importances:")
    for feat, imp in metrics["feature_importances"].items():
        print(f"  • {feat:12s}: {imp * 100:.2f}%")

    if args.save:
        saved_paths = trainer.save_model()
        print(f"\nModel exported successfully to {len(saved_paths)} target locations.")

if __name__ == "__main__":
    main()
