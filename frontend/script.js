document.getElementById("fitnessForm")
.addEventListener("submit", async function(e){

    e.preventDefault()

    // Collect form data
    const data = {
        age: parseInt(document.getElementById("age").value),
        gender: document.getElementById("gender").value,
        height: parseFloat(document.getElementById("height").value),
        weight: parseFloat(document.getElementById("weight").value),
        goal: document.getElementById("goal").value,
        budget: document.getElementById("budget").value,
        food_type: document.getElementById("food_type").value,
        equipment: document.getElementById("equipment").value,
        time: parseInt(document.getElementById("time").value),
        stress: document.getElementById("stress").value,
        sleep: parseFloat(document.getElementById("sleep").value)
    }

    try{

        const response = await fetch("http://127.0.0.1:8000/generate-plan",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify(data)

        })

        const result = await response.json()

        console.log("API Response:", result)

        // Save result for dashboard
        localStorage.setItem("fitnessResult", JSON.stringify(result))

        // Redirect to dashboard
        window.location.href = "dashboard.html"

    }

    catch(error){

        console.error("Error:", error)

        alert("Error connecting to server. Make sure FastAPI is running.")

    }

})