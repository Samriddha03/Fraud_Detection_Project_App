async function checkFraud() {
  const amount = document.getElementById("amount").value;

  if (!amount) {
    alert("Please enter amount");
    return;
  }

  const response = await fetch("http://127.0.0.1:8000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      transaction: [Number(amount)]
    })
  });

  const data = await response.json();
  document.getElementById("result").innerText =
    "Prediction: " + data.prediction;
}
