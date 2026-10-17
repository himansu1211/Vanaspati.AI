"""
Vanaspati.AI - Core Dataset Registry & Download Guide
Manages dataset metadata, class catalogs, and loaders for the 4 pillars:
1. Plant/Crop Disease: PlantVillage (54,000+ images across 38 classes)
2. Plant & Tree Identification: PlantCLEF, iNaturalist, Leafsnap
3. Vegetable & Spinach Identification: Kaggle Vegetable Image Dataset
4. Agricultural Soil & Crop Benchmarks: ICAR / Kaggle Crop Recommendation
"""

from typing import Dict, Any, List

DATASET_PILLARS = {
    "plant_disease": {
        "name": "PlantVillage Benchmark Dataset",
        "description": "54,305 curated images of plant leaves categorized across 38 distinct crop-disease combinations and healthy controls.",
        "samples_count": 54305,
        "classes_count": 38,
        "crops": ["Apple", "Blueberry", "Cherry", "Corn", "Grape", "Orange", "Peach", "Pepper", "Potato", "Raspberry", "Soybean", "Squash", "Strawberry", "Tomato"],
        "kaggle_url": "https://www.kaggle.com/vipoooool/new-plant-diseases-dataset",
        "recommended_split": {"train": 0.8, "val": 0.1, "test": 0.1}
    },
    "vegetable_and_spinach": {
        "name": "Kaggle Vegetable Image Dataset",
        "description": "21,000 images across 15 common vegetable and leafy green categories including spinach, cabbage, broccoli, carrot, and capsicum.",
        "samples_count": 21000,
        "classes_count": 15,
        "key_species": ["Spinach", "Broccoli", "Cabbage", "Carrot", "Cauliflower", "Cucumber", "Eggplant", "Papaya", "Potato", "Pumpkin", "Radish", "Tomato"],
        "kaggle_url": "https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset"
    },
    "tree_identification": {
        "name": "Leafsnap & PlantCLEF Tree Dataset",
        "description": "High-resolution leaf profiles of 185 tree species from the Northeastern United States and global forest repositories.",
        "samples_count": 30866,
        "classes_count": 185,
        "url": "http://leafsnap.com/dataset/"
    },
    "soil_and_crop": {
        "name": "Agricultural Production & Crop Recommendation Dataset",
        "description": "2,200 multi-parameter soil and climate profiles correlating N, P, K, pH, rainfall, and weather to 22 agricultural crops.",
        "samples_count": 2200,
        "classes_count": 22
    }
}

def get_dataset_metadata(pillar_name: str) -> Dict[str, Any]:
    """Retrieves metadata for specified dataset pillar."""
    return DATASET_PILLARS.get(pillar_name, {})
