# api.py
import joblib
import numpy as np
import logging
from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel

# ----------------- Logging -----------------
logging.basicConfig(level=logging.INFO)

# ----------------- Load Model -----------------
try:
    model = joblib.load("fraud_model_1feature.pkl")  # 1-feature model
    logging.info("Model loaded successfully")
except Exception as e:
    logging.error(f"Failed to load model: {e}")
    raise

# No scaler is used
scaler = None

# ----------------- Expected Features -----------------
expected_features = 1  # 1 feature only

# ----------------- FastAPI App -----------------
app = FastAPI()

# ----------------- Request Schema -----------------
class TransactionRequest(BaseModel):
    transaction: list  # list of numbers

# ----------------- Predict Endpoint -----------------
@app.post("/predict")
def predict(request: TransactionRequest = Body(...)):
    logging.info("Entered /predict endpoint")
    logging.info(f"Received transaction with {len(request.transaction)} features")

    # Validate number of features
    if len(request.transaction) != expected_features:
        logging.error(
            f"Invalid number of features. Expected {expected_features}, "
            f"got {len(request.transaction)}"
        )
        raise HTTPException(
            status_code=422,
            detail=f"Invalid number of features. Expected {expected_features}, got {len(request.transaction)}"
        )

    # Validate numeric input
    if not all(isinstance(x, (int, float)) for x in request.transaction):
        logging.error("All features must be numeric")
        raise HTTPException(
            status_code=422,
            detail="All features must be numeric"
        )

    try:
        # Prepare data
        data = np.array(request.transaction).reshape(1, -1)

        # No scaler, use data as-is
        prediction = model.predict(data)[0]

        # Probability if available
        probability = float(model.predict_proba(data)[0][1]) if hasattr(model, "predict_proba") else None

        label = "Fraud" if prediction == 1 else "Not Fraud"

        logging.info(f"Prediction result: {label}, Probability: {probability}")

        return {
            "prediction": label,
            "fraud_prediction": int(prediction),
            "fraud_probability": probability
        }

    except Exception as e:
        logging.exception("Unhandled error in /predict")
        raise HTTPException(status_code=500, detail=str(e))
