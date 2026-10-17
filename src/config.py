"""
Vanaspati.AI - Centralized Configuration Module
Provides uniform paths, constants, API keys, and model parameters.
"""

from pathlib import Path
import os

# Project Roots
BASE_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = BASE_DIR / "src"
DATA_RAW_DIR = BASE_DIR / "Data-raw"
DATA_PROCESSED_DIR = BASE_DIR / "Data-processed"
APP_DIR = BASE_DIR / "app"
APP_MODELS_DIR = APP_DIR / "models"
ROOT_MODELS_DIR = BASE_DIR / "models"

DEFAULT_WEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY", "your_openweather_api_key_here")

# Supported Crops & Classes
SUPPORTED_CROPS = [
    'rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
    'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
    'banana', 'mango', 'grapes', 'watermelon', 'muskmelon',
    'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee'
]

DISEASE_CLASSES = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

# Soil Parameter Ideal Ranges
PARAMETER_RANGES = {
    'nitrogen': {'min': 0, 'max': 140, 'unit': 'ratio / mg/kg', 'ideal_avg': 50},
    'phosphorous': {'min': 5, 'max': 145, 'unit': 'ratio / mg/kg', 'ideal_avg': 53},
    'pottasium': {'min': 5, 'max': 205, 'unit': 'ratio / mg/kg', 'ideal_avg': 48},
    'ph': {'min': 3.5, 'max': 10.0, 'unit': 'pH scale', 'ideal_avg': 6.5},
    'rainfall': {'min': 20.0, 'max': 300.0, 'unit': 'mm', 'ideal_avg': 103.0},
    'temperature': {'min': 8.0, 'max': 45.0, 'unit': '°C', 'ideal_avg': 25.6},
    'humidity': {'min': 14.0, 'max': 100.0, 'unit': '%', 'ideal_avg': 71.4}
}
