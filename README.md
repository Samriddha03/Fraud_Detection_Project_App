# Full Stack Fraud Detection System (ML + FastAPI + Frontend)
 
 # Project Overview

This project is a full stack fraud detection web application that predicts whether a
financial transaction is Fraudulent or Not Fraud using a machine learning model.

The system integrates:

Machine Learning for fraud prediction

FastAPI for backend REST API

HTML, CSS, JavaScript for frontend user interaction

Users can enter a transaction amount in the browser and receive real-time fraud predictions.

# System Architecture
Frontend (HTML / CSS / JavaScript)
            ↓
FastAPI Backend (REST API)
            ↓
Machine Learning Model (.pkl)

# Project Structure
Fraud_Detection_Project_App/
├── api.py                      # FastAPI backend
├── train_1feature_model.py     # ML model training script
├── fraud_model_amount_only.pkl # Trained ML model
├── test_predict.py             # API testing script
├── requirements.txt            # Python dependencies
├── frontend/
│   ├── index.html              # Frontend UI
│   └── script.js               # Frontend logic
└── README.md                   # Project documentation

# Dataset & Model Training

The model was trained in Google Colab

Transaction data was preprocessed and used to train a classifier

The current implementation uses transaction amount as the feature

The trained model was saved using joblib

The model is loaded directly by the FastAPI backend

# This is a simplified fraud detection model created for learning and demonstration purposes.

# Backend API (FastAPI)
Available Endpoints

POST /predict – Predicts whether a transaction is fraudulent

GET /health – Health check endpoint

Example Request
{
  "transaction": [500]
}

Example Response
{
  "prediction": "Not Fraud"
}

# Frontend Application

Built using HTML, CSS, and JavaScript

User-friendly interface to enter transaction amount

Sends requests to backend using fetch

Displays prediction dynamically without page reload

# How to Run the Project Locally


1️  Start the Backend Server
uvicorn api:app --reload


Backend will run at:

http://127.0.0.1:8000

2 Run the Frontend

Open the frontend folder

Open index.html in any browser

Enter a transaction amount and click Check
# Deployment

Backend deployed using Render

Frontend connects to the deployed API endpoint

Fully functional end-to-end full stack application

# Technologies Used

Python

FastAPI

Scikit-learn

HTML

CSS

JavaScript

Git & GitHub

Render (Deployment)

# Project Highlights

Full stack integration of ML + Backend + Frontend

Real-time fraud prediction

Clean API design

Deployment-ready architecture

Portfolio and interview-ready project

# Disclaimer

This project is created for educational and demonstration purposes only and should not
be used directly in real-world financial systems without further security, data, and model enhancements.

