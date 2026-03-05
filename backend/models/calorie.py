def calculate_bmr(age, gender, weight, height):
    if gender.lower() == "male":
        return 10*weight + 6.25*height - 5*age + 5
    else:
        return 10*weight + 6.25*height - 5*age - 161


def calculate_tdee(bmr, activity_factor=1.55):
    return bmr * activity_factor


def adjust_calories(tdee, goal):
    if goal == "Weight gain":
        return tdee + 300
    elif goal == "Fat loss":
        return tdee - 400
    return tdee


def calculate_macros(calories, weight):
    protein = weight * 1.6
    fats = calories * 0.25 / 9
    carbs = (calories - (protein*4 + fats*9)) / 4

    return {
        "calories": round(calories),
        "protein": round(protein),
        "carbs": round(carbs),
        "fats": round(fats)
    }