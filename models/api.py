from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, conlist
import joblib
import numpy as np

app = FastAPI(
    title="Fraud Detection API",
    description="API for predicting fraudulent transactions",
    version="1.0"
)

# Load your pre-trained model and scaler safely
try:
    model = joblib.load("fraud_model.pkl")
    scaler = joblib.load("scaler.pkl")
except Exception as e:
    raise RuntimeError(f"Failed to load model or scaler: {str(e)}")

# Determine the expected number of features from the model/scaler
try:
    expected_features = scaler.scale_.shape[0]  # number of features scaler expects
except AttributeError:
    raise RuntimeError("Scaler does not have 'scale_' attribute. Check your scaler.")

# Request body
class TransactionRequest(BaseModel):
    transaction: conlist(float, min_items=1) = Field(
        ..., description="List of numeric transaction features"
    )

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fraud Detection API!"}

@app.post("/predict")
def predict(request: TransactionRequest):
    # Step 1: Validate feature count
    if len(request.transaction) != expected_features:
        raise HTTPException(
            status_code=422,
            detail=f"Invalid number of features. Expected {expected_features}, got {len(request.transaction)}"
        )

    try:
        # Step 2: Convert input to numpy array
        data = np.array(request.transaction).reshape(1, -1)

        # Step 3: Scale the data
        data_scaled = scaler.transform(data)

        # Step 4: Make prediction
        prediction = model.predict(data_scaled)[0]

        # Step 5: Make probability prediction if supported
        if hasattr(model, "predict_proba"):
            probability = float(model.predict_proba(data_scaled)[0][1])
        else:
            probability = None  # or you can return 0.0 / -1 if preferred

        return {
            "fraud_prediction": int(prediction),
            "fraud_probability": probability
        }

    except ValueError as ve:
        # Catch errors from invalid input shapes or types
        raise HTTPException(status_code=422, detail=f"Invalid input: {str(ve)}")
    except Exception as e:
        # Catch any other server errors safely
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
