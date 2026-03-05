def generate_workout(goal, equipment, time):
    if equipment == "None":
        base = ["Push-ups", "Squats", "Plank", "Lunges"]
    elif equipment == "Dumbbells":
        base = ["Dumbbell Press", "Rows", "Goblet Squat"]
    else:
        base = ["Bench Press", "Deadlift", "Pull-ups"]

    sets = 3 if time <= 30 else 4
    reps = "12-15" if goal == "Fat loss" else "8-12"

    return {
        "weekly_split": "Push / Pull / Legs",
        "exercises": base,
        "sets": sets,
        "reps": reps,
        "progression": "Increase weight or reps weekly by 5%"
    }