async function checkFraud() {
  const amountInput = document.getElementById("amount");
  const resultEl = document.getElementById("result");

  const amount = amountInput.value;

  if (amount === "") {
    alert("Please enter a transaction amount");
    return;
  }

  // Show loading state
  resultEl.innerText = "Checking fraud status...";

  try {
    const response = await fetch(
      "https://fraud-api01.onrender.com/predict",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          transaction: [Number(amount)] // ✅ EXACTLY ONE FEATURE
        })
      }
    );

    if (!response.ok) {
      const err = await response.text();
      throw new Error(err);
    }

    const data = await response.json();

    resultEl.innerText =
      `Prediction: ${data.prediction}
Fraud Probability: ${data.fraud_probability}`;

  } catch (error) {
    console.error("API Error:", error);
    resultEl.innerText = "Error calling Fraud API";
  }
}
