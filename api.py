# Model and scaler trained in Google Colab using fraud dataset
# Saved as fraud_model.pkl and scaler.pkl

from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import List
import joblib
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Fraud Detection API",
    description="API for predicting fraudulent transactions",
    version="1.0"
)

# Load model & scaler safely
try:
    model = joblib.load("fraud_model.pkl")
    scaler = joblib.load("scaler.pkl")
except Exception as e:
    raise RuntimeError(f"Failed to load model or scaler: {e}")

expected_features = scaler.scale_.shape[0]

class TransactionRequest(BaseModel):
    transaction: List[float]

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(request: TransactionRequest = Body(...)):
    logging.info(f"Received transaction with {len(request.transaction)} features")

    if len(request.transaction) != expected_features:
        raise HTTPException(
            status_code=422,
            detail=f"Invalid number of features. Expected {expected_features}, got {len(request.transaction)}"
        )

    try:
        data = np.array(request.transaction).reshape(1, -1)
        data_scaled = scaler.transform(data)
        prediction = model.predict(data_scaled)[0]

        probability = None
        if hasattr(model, "predict_proba"):
            probability = float(model.predict_proba(data_scaled)[0][1])

        label = "Fraud" if prediction == 1 else "Not Fraud"

        logging.info(f"Prediction result: {label}, Probability: {probability}")

        return {
            "prediction": label,
            "fraud_prediction": int(prediction),
            "fraud_probability": probability
        }

    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
