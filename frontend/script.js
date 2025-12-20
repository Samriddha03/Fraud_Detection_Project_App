async function checkFraud() {
  const amount = document.getElementById("amount").value;

  const response = await fetch("https://fraud-detection-project-app-5.onrender.com/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ amount: amount })
  });

  const data = await response.json();
  document.getElementById("result").innerText =
    "Prediction: " + data.prediction;
}
