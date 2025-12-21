import joblib
import numpy as np
import logging
from fastapi import FastAPI, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

# -------------------------
# Logging
# -------------------------
logging.basicConfig(level=logging.INFO)

# -------------------------
# Load 1-feature model
# -------------------------
try:
    model = joblib.load("fraud_model_1feature.pkl")
    logging.info("1-feature model loaded successfully")
except Exception as e:
    logging.error(f"Model load failed: {e}")
    raise

# -------------------------
# FastAPI app
# -------------------------
app = FastAPI(
    title="Fraud Detection API",
    description="Fraud prediction using 1 feature (Amount)",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all frontends
    allow_credentials=True,
    allow_methods=["*"],  # allow POST, GET, OPTIONS
    allow_headers=["*"],  # allow all headers
)


# -------------------------
# Request schema
# -------------------------
class TransactionRequest(BaseModel):
    transaction: list[float]  # exactly ONE value

# -------------------------
# Health check
# -------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# -------------------------
# Predict endpoint
# -------------------------
@app.post("/predict")
def predict(request: TransactionRequest = Body(...)):
    logging.info(f"Received input: {request.transaction}")

    if len(request.transaction) != 1:
        raise HTTPException(
            status_code=422,
            detail=f"Invalid number of features. Expected 1, got {len(request.transaction)}"
        )

    try:
        X = np.array(request.transaction).reshape(1, 1)
        prediction = model.predict(X)[0]

        probability = None
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(X)[0]
            probability = float(proba[1]) if len(proba) > 1 else 0.0

        return {
    "prediction": "Fraud" if prediction == 1 else "Not Fraud",
    "fraud_prediction": int(prediction),
    "fraud_probability": round(probability or 0, 4),
    "amount": request.transaction[0],
    "note": "Demo model using only transaction amount"
}

    except Exception as e:
        logging.exception("Prediction failed")
        raise HTTPException(status_code=500, detail=str(e))
