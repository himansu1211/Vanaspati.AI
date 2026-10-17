# Vanaspati.AI - Computer Vision Disease Identifier API 🌿

High-performance FastAPI microservice for diagnosing plant pathology from leaf imagery.

## Technologies Used:
- Python 3
- FastAPI & Uvicorn
- TensorFlow / PyTorch / Computer Vision Heuristic Fallback
- Pillow & NumPy

## Installation:
```bash
pip install -r requirements.txt
```

## Running the Service:
```bash
python main.py
# Or with uvicorn directly:
uvicorn main:app --host localhost --port 10000 --reload
```
Default URL: `http://localhost:10000`

## API Endpoints:
- `GET /`: Service metadata, active deep learning framework, and supported class count.
- `GET /health` & `GET /ping`: Microservice health check.
- `POST /predict`: Upload image multipart form (`file`) to obtain disease classification, class index, and confidence score.