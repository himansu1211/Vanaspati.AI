"""
Vanaspati.AI Machine Learning & Deep Learning Architectures
Lazy imports to support environments without C++ runtime / PyTorch DLLs.
"""

def get_crop_trainer():
    from .crop_recommender import CropRecommendationTrainer
    return CropRecommendationTrainer

def get_disease_trainer():
    from .disease_classifier import PlantDiseaseTrainer
    return PlantDiseaseTrainer

__all__ = [
    'get_crop_trainer',
    'get_disease_trainer'
]
