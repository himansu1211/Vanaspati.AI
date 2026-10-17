"""
CropRecommendationTrainer: Modular trainer for Crop Recommendation model
Trains, evaluates, tunes, and exports RandomForestClassifier for precision agriculture.
"""

import pickle
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Dict, Any, Optional, Tuple
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.model_selection import cross_val_score
from src.config import APP_MODELS_DIR, ROOT_MODELS_DIR
from src.data.preprocessor import CropDataPreprocessor

class CropRecommendationTrainer:
    def __init__(self, n_estimators: int = 100, max_depth: Optional[int] = None, random_state: int = 42):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.random_state = random_state
        self.model = RandomForestClassifier(
            n_estimators=self.n_estimators,
            max_depth=self.max_depth,
            random_state=self.random_state,
            n_jobs=-1
        )
        self.feature_names = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
        self.preprocessor = CropDataPreprocessor()

    def train(self, test_size: float = 0.2) -> Dict[str, Any]:
        """
        Executes end-to-end model training, validation, and metrics calculation.
        """
        X_train, X_test, y_train, y_test = self.preprocessor.get_train_test_split(test_size=test_size, random_state=self.random_state)
        
        print(f"[Trainer] Training RandomForest on {len(X_train)} samples across {y_train.nunique()} crops...")
        self.model.fit(X_train, y_train)

        # Cross-validation
        cv_scores = cross_val_score(self.model, X_train, y_train, cv=5)
        
        # Test evaluation
        y_pred = self.model.predict(X_test)
        test_acc = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)

        feature_importances = dict(zip(self.feature_names, self.model.feature_importances_))

        metrics = {
            "test_accuracy": round(float(test_acc), 4),
            "cv_mean_accuracy": round(float(np.mean(cv_scores)), 4),
            "cv_std": round(float(np.std(cv_scores)), 4),
            "feature_importances": {k: round(float(v), 4) for k, v in feature_importances.items()},
            "num_train_samples": len(X_train),
            "num_test_samples": len(X_test)
        }
        print(f"[Trainer] Model Test Accuracy: {metrics['test_accuracy'] * 100:.2f}% | 5-Fold CV: {metrics['cv_mean_accuracy'] * 100:.2f}%")
        return metrics

    def predict_crop(self, n: float, p: float, k: float, temp: float, humidity: float, ph: float, rainfall: float) -> Tuple[str, Dict[str, float]]:
        """
        Returns top recommended crop and class probabilities.
        """
        features = np.array([[n, p, k, temp, humidity, ph, rainfall]])
        pred = self.model.predict(features)[0]
        
        if hasattr(self.model, "predict_proba"):
            probs = self.model.predict_proba(features)[0]
            top_indices = np.argsort(probs)[::-1][:3]
            top_candidates = {self.model.classes_[idx]: round(float(probs[idx]), 3) for idx in top_indices}
        else:
            top_candidates = {pred: 1.0}

        return pred, top_candidates

    def save_model(self, output_paths: Optional[list] = None) -> list:
        """
        Persists trained RandomForest model to both app/models and root models.
        """
        targets = output_paths or [
            APP_MODELS_DIR / "RandomForest.pkl",
            ROOT_MODELS_DIR / "RandomForest.pkl"
        ]
        saved = []
        for path in targets:
            Path(path).parent.mkdir(parents=True, exist_ok=True)
            with open(path, "wb") as f:
                pickle.dump(self.model, f)
            saved.append(path)
            print(f"[Trainer] Model saved to {path}")
        return saved

if __name__ == "__main__":
    trainer = CropRecommendationTrainer()
    metrics = trainer.train()
    print("Metrics:", metrics)
    trainer.save_model()
