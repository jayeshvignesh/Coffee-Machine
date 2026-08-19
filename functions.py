from resources import MENU
from resources import resources
def money_converter(t, l, q, d, n, coffee):
    money_given = (t * 2) + l + (q * 0.25) + (d * 0.10) + (n * 0.05)
    cost = MENU[coffee]["cost"]
    return money_given - cost

def deductor(coffee1):
    ingredients = MENU[coffee1]
    ingredients = ingredients["ingredients"]
    water = ingredients["water"]
    milk = ingredients["milk"]
    coffee = ingredients["coffee"]
    if resources["water"] < water or resources["milk"] < milk or resources["coffee"] < coffee:
        return False
    else:
        resources["water"] = resources["water"] - water
        resources["milk"] = resources["milk"] - milk
        resources["coffee"] = resources["coffee"] - coffee
        return f"Here's your {coffee1}"
def adder(coffee1):
    ingredients = MENU[coffee1]
    ingredients = ingredients["ingredients"]
    water = ingredients["water"]
    milk = ingredients["milk"]
    coffee = ingredients["coffee"]
    resources["water"] = resources["water"] + water
    resources["milk"] = resources["milk"] + milk
    resources["coffee"] = resources["coffee"] + coffee
