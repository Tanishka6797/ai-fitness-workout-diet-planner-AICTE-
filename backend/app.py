from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.calorie import calculate_bmr, calculate_tdee, adjust_calories, calculate_macros
from models.workout import generate_workout
from models.diet import generate_diet
from llm.gemini_service import generate_llm_response

import os

app = FastAPI()

# Enable CORS so frontend can connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-plan")
def generate_plan(data: dict):

    # ---------- CALORIE CALCULATIONS ----------
    bmr = calculate_bmr(
        data["age"],
        data["gender"],
        data["weight"],
        data["height"]
    )

    tdee = calculate_tdee(bmr)

    calories = adjust_calories(tdee, data["goal"])

    macros = calculate_macros(calories, data["weight"])

    # ---------- WORKOUT GENERATION ----------
    workout = generate_workout(
        goal=data["goal"],
        equipment=data["equipment"],
        time=data["time"]
    )

    # ---------- DIET GENERATION ----------
    diet = generate_diet(
        macros,
        data["food_type"]
    )

    # ---------- AI COACH ADVICE ----------
    try:
        ai_explanation = generate_llm_response(data, macros)
    except:
        ai_explanation = "Stay consistent with workouts, eat balanced meals, and get proper sleep."

    # ---------- FINAL RESPONSE ----------
    return {
        "status": "success",
        "macros": macros,
        "workout": workout,
        "diet": diet,
        "ai_explanation": ai_explanation
    }

# Required for Render
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)