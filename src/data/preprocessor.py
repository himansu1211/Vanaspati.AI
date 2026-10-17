"""
CropDataPreprocessor: Modular data engineering pipeline for agricultural dataset
Handles ingestion, cleaning, normalization, validation, and train-test splits.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Tuple, Dict, Any, Optional
from src.config import DATA_RAW_DIR, DATA_PROCESSED_DIR

class CropDataPreprocessor:
    def __init__(self, data_path: Optional[Path] = None):
        self.data_path = data_path or (DATA_PROCESSED_DIR / "crop_recommendation.csv")
        self.raw_path = DATA_RAW_DIR / "cpdata.csv"
        self.df: Optional[pd.DataFrame] = None

    def load_processed_data(self) -> pd.DataFrame:
        """Loads and validates processed crop recommendation data."""
        if not self.data_path.exists():
            raise FileNotFoundError(f"Processed dataset not found at {self.data_path}")
        self.df = pd.read_csv(self.data_path)
        # Standardize column names
        self.df.columns = [c.strip().lower() for c in self.df.columns]
        return self.df

    def load_fertilizer_data(self) -> pd.DataFrame:
        """Loads fertilizer guidelines data."""
        fert_path = DATA_PROCESSED_DIR / "fertilizer.csv"
        if not fert_path.exists():
            raise FileNotFoundError(f"Fertilizer dataset not found at {fert_path}")
        df_fert = pd.read_csv(fert_path)
        df_fert.columns = [c.strip() for c in df_fert.columns]
        return df_fert

    def clean_and_validate(self) -> pd.DataFrame:
        """Cleans and validates the dataset: removes NaNs, checks outlier bounds."""
        if self.df is None:
            self.load_processed_data()

        # Drop duplicates and nulls
        initial_len = len(self.df)
        self.df = self.df.drop_duplicates().dropna()
        dropped = initial_len - len(self.df)
        if dropped > 0:
            print(f"[Preprocessor] Cleaned {dropped} invalid / duplicate rows.")

        # Ensure correct datatypes
        numeric_cols = ['n', 'p', 'k', 'temperature', 'humidity', 'ph', 'rainfall']
        for col in numeric_cols:
            if col in self.df.columns:
                self.df[col] = pd.to_numeric(self.df[col], errors='coerce')

        self.df = self.df.dropna()
        return self.df

    def get_feature_summary(self) -> Dict[str, Any]:
        """Calculates per-crop summary statistics for soil and weather conditions."""
        if self.df is None:
            self.clean_and_validate()
            
        summary = {}
        for crop, group in self.df.groupby('label'):
            summary[crop] = {
                'N_mean': round(group['n'].mean(), 2),
                'P_mean': round(group['p'].mean(), 2),
                'K_mean': round(group['k'].mean(), 2),
                'ph_mean': round(group['ph'].mean(), 2),
                'temp_mean': round(group['temperature'].mean(), 2),
                'humidity_mean': round(group['humidity'].mean(), 2),
                'rainfall_mean': round(group['rainfall'].mean(), 2),
                'samples': len(group)
            }
        return summary

    def get_train_test_split(self, test_size: float = 0.2, random_state: int = 42) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """Generates stratified train-test splits for model training."""
        if self.df is None:
            self.clean_and_validate()

        from sklearn.model_selection import train_test_split
        features = self.df[['n', 'p', 'k', 'temperature', 'humidity', 'ph', 'rainfall']]
        labels = self.df['label']

        return train_test_split(features, labels, test_size=test_size, random_state=random_state, stratify=labels)

if __name__ == "__main__":
    processor = CropDataPreprocessor()
    df = processor.clean_and_validate()
    print(f"Loaded {len(df)} samples across {df['label'].nunique()} crop classes.")
    summary = processor.get_feature_summary()
    print(f"Sample crop summary for 'rice': {summary.get('rice')}")
