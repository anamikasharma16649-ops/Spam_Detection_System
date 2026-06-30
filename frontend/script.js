async function predict() {
    let email = document.getElementById("emailInput").value;

     if(email.trim() == ""){
        alert("Please enter an email.");
        return;
    }
    
    try {
        let response = await fetch("/prediction", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ Email: email })
        });

        let data = await response.json();

        console.log(data);

        let result = document.getElementById("result");

        if (data.prediction === 1) {
            result.innerHTML = "Spam Email";
            result.style.color = "red";
        } else {
            result.innerHTML = "Not Spam Email";
            result.style.color = "green";
        }

    } catch (err) {
        console.log(err);
        alert("Error");
    }
}
