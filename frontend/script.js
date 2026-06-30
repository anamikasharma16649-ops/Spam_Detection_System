async function predict() {
    let email = document.getElementById("emailInput").value;

    let response = await fetch("/prediction", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ Email: email })
    });

    let data = await response.json();

    let result = document.getElementById("result");

    if (data.prediction === 1) {
        result.innerHTML = "🚨 Spam Email";
        result.style.color = "red";
    } else {
        result.innerHTML = "✅ Not Spam Email";
        result.style.color = "green";
    }
}