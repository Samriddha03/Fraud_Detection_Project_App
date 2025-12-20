async function checkFraud() {
  const amount = document.getElementById("amount").value;

  if (!amount) {
    alert("Please enter a transaction amount");
    return;
  }
  const FEATURE_COUNT = 30;
  const features = new Array(FEATURE_COUNT).fill(0);
   features[0] = Number(amount);

  const response = await fetch(
    "https://fraud-detection-project-app-7.onrender.com/predict",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        transaction: [features]
      })
    }
  );

  const data = await response.json();

  document.getElementById("result").innerText =
    `Prediction: ${data.prediction}`;
}
