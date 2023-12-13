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
    names = [food["name"] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    hot_level = [food for food in spicy_foods if food["heat_level"]>2]
    for food in hot_level:
        hots = food["name"] + " " + "(" + food["cuisine"] + ")" + "|" + "Heat Level: "+ "🌶"*food["heat_level"]
        return hots
    
     
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    hot_level = [food for food in spicy_foods if food["heat_level"]>5]
    for food in hot_level:
        hots = food["name"] + " " + "(" + food["cuisine"] + ")" + "|" + "Heat Level: "+ "🌶"*food["heat_level"]
        return hots

def get_average_heat_level(spicy_foods):
    count = 0
    for food in spicy_foods:
        count += food["heat_level"]
    
    count = count/len(spicy_foods)
    return count 

def create_spicy_food(spicy_foods, spicy_food):
    pass
