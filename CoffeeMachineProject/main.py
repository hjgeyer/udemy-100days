MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def calc_cost(beverage_cost, quarters, dimes, nickels, pennies) -> float:
    """This method takes in the beverage cost and number of nickels, dimes, quarters and pennies and determines 
       if enough money was supplied by the customer.  This will return a value.  Positive numbers means enough was
       given by the customer, negative numbers means that the customer did not give enough money."""
    total_cost = ((quarters * 25) + (dimes * 10) + (nickels * 5) + pennies) / 100
    return total_cost - beverage_cost

def has_enough_ingredients(beverage_ingredients: dict, available_resources: dict) -> bool:
    for ingredient in beverage_ingredients:
        if beverage_ingredients[ingredient] > available_resources[ingredient]:
            print(f"There is not enough {ingredient}")
            return False
    return True

def consume_resources(beverage_ingredients: dict, available_resources: dict) -> dict:
    for ingredient in beverage_ingredients: 
        available_resources[ingredient] -= beverage_ingredients[ingredient]

    return available_resources

more_drinks = True
total_money = 0
while more_drinks:
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if option == 'report':
        for ingredient in resources: 
            print(f"{ingredient}: {resources[ingredient]}ml")
        print(f"Money: ${total_money}")
    elif option in ('espresso','latte','cappuccino'):
        num_quarters = int(input("how many quarters?: "))
        num_dimes = int(input("how many dimes?: "))
        num_nickels = int(input("how many nickles?: "))
        num_pennies = int(input("how many pennies?: "))

        beverage = MENU[option]
        option_resources = beverage['ingredients']

        change = calc_cost(beverage["cost"], num_quarters, num_dimes, num_nickels, num_pennies)

        if change < 0:
            print(f"You did not give enough money. You are short: {change}")
        elif not has_enough_ingredients(beverage["ingredients"], resources):
            print("There is not enough ingredients to make the {option}. Sorry.")
        else:
            total_money += beverage["cost"]
            print(f"You have ${change} in change.")
            print(f"Here is your {option}. Enjoy!")
            resources = consume_resources(option_resources, resources)
    else:
        more_drinks = False