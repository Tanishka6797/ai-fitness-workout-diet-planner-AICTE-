def generate_diet(macros, food_type):

    food_type = food_type.lower()

    if food_type == "vegetarian":

        meals = [
            "Paneer curry",
            "Dal (lentils)",
            "Brown rice",
            "Chapati (whole wheat roti)",
            "Peanuts",
            "Milk or yogurt",
            "Soybean curry",
            "Vegetable salad",
            "Banana or seasonal fruit"
        ]

    elif food_type == "vegan":

        meals = [
            "Tofu curry",
            "Chickpea salad",
            "Brown rice",
            "Whole wheat roti",
            "Peanuts or almonds",
            "Soy milk",
            "Vegetable stir fry",
            "Lentil soup"
        ]

    elif food_type == "jain":

        meals = [
            "Moong dal",
            "Steamed rice",
            "Chapati",
            "Paneer curry (no onion/garlic)",
            "Peanuts",
            "Milk",
            "Cucumber salad",
            "Fruit bowl"
        ]

    else:  # Non-veg

        meals = [
            "Grilled chicken breast",
            "Boiled eggs",
            "Fish curry",
            "Rice",
            "Chapati",
            "Vegetable salad",
            "Milk or yogurt",
            "Banana"
        ]

    return {
        "meals": meals,
        "estimated_cost_per_day": "Low budget meal plan"
    }