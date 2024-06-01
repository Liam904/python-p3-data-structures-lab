spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food["name"])

    return names


def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
    return spiciest_foods


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        formatted_food = (
            f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}"
        )
        print(formatted_food)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    foods = {}
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            foods.update(food)
    return foods


def print_spiciest_foods(spicy_foods):
    foods = []

    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        if food["heat_level"] > 5:
            formatted_food = (
                f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}"
            )
            foods.append(formatted_food)
    for food in foods:
        print(food)


def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    for food in spicy_foods:
        total_heat_level += food["heat_level"]
    average_heat_level = total_heat_level / 3
    return average_heat_level


def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food] 



# print(get_names(spicy_foods))


# print_spicy_foods(spicy_foods)

# print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))

# print_spiciest_foods(spicy_foods)

# print(get_average_heat_level(spicy_foods))
