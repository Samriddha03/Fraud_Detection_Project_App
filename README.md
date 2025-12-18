# Fraud Detection System (FastAPI)

## Project Overview
This project is a software-based fraud detection system that uses a machine learning model
to predict whether a financial transaction is fraudulent or not.

The machine learning model was trained in Google Colab using a fraud detection dataset
and then deployed as a REST API using FastAPI.

---

## Project Structure
Fraud_Detection_Project/
├── api.py # FastAPI backend
├── test_predict.py # API testing script
├── fraud_model.pkl # Trained ML model
├── scaler.pkl # Feature scaler
├── README.md # Project documentation

---

## Dataset & Model Training
- The dataset was loaded and processed in Google Colab.
- Data preprocessing included scaling numerical features.
- A machine learning classifier was trained to detect fraudulent transactions.
- The trained model and scaler were saved using `joblib`.

---

## Backend API (FastAPI)
- FastAPI is used to expose the model as a REST API.
- Endpoint:
  - `POST /predict` → Predicts fraud based on transaction features
  - `GET /health` → Health check endpoint

---

## How to Run the Project

### Step 1: Start the API server
```bash
uvicorn api:app --reload

