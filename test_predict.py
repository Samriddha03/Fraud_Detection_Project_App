import requests
import json

# API URL
url = "http://127.0.0.1:8000/predict"

# --- Valid input (must match model feature count) ---
valid_transaction = {
    "transaction": [500.0]
}

# --- Invalid input (too few/many features) ---
invalid_transaction = {
    "transaction": [500.0, 1000.0]
}

# --- Non-numeric input ---
non_numeric_transaction = {
    "transaction": ["abc"]
}

# Helper function to test API
def test_api(data, description):
    print(f"\nTesting: {description}")
    try:
        response = requests.post(url, json=data, timeout=5)
        print("Status Code:", response.status_code)
        try:
            print("Response JSON:", response.json())
        except json.JSONDecodeError:
            print("Response Text:", response.text)
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

# Run tests
test_api(valid_transaction, "Valid input")
test_api(invalid_transaction, "Invalid number of features")
test_api(non_numeric_transaction, "Non-numeric feature")
