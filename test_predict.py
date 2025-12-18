import requests
import json

# API URL
url = "http://127.0.0.1:8000/predict"

# --- Valid input (must match model feature count) ---
valid_transaction = {
    "transaction": [0.1]*30
}

# --- Invalid input (too few features) ---
invalid_transaction = {
    "transaction": [0.5, 1.2, 3.4]
}

# Helper function to test API
def test_api(data, description):
    print(f"\nTesting: {description}")
    response = requests.post(url, json=data, timeout=5)
    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except json.JSONDecodeError:
        print("Response Text:", response.text)

# Test valid input
test_api(valid_transaction, "Valid input")

# Test invalid input
test_api(invalid_transaction, "Invalid input")
