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
    names = [spicy_foods[0,2]["mame"] for spicy_foods[0,2]["mame"] in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [spicy_foods[0,2] for spicy_foods[0,2] in spicy_foods if spicy_foods[0,2]["mame"] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for i in spicy_foods:
        for j in i
            if j["heat_level"] == 3:
                print(f"{j["name"]} + | Heat Level : 🌶🌶🌶" )
            elif j["heat_level"] == 6:
                print(f"{j["name"]} + | Heat Level : 🌶🌶🌶🌶🌶🌶" )
            elif j["heat_level"] == 9:
                print(f"{j["name"]} + | Heat Level : 🌶🌶🌶🌶🌶🌶🌶🌶🌶" )
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    for i in spicy_foods:
        for j in i:
            if j["heat_level"] > 5:
                print(f"{j["name"]}")

def get_average_heat_level(spicy_foods):
    for i in spicy_foods:
        count = 0
        for j in i:
            count += j["heat_level"]
                print(count)

def create_spicy_food(spicy_foods, spicy_food):
    pass
