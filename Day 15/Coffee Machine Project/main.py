MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
    "money": 0
}

# def is_resources_sufficient(order_ingredients):
#     for ingredient in order_ingredients:
#         if order_ingredients[ingredient] > resources[ingredient]:
#             print(f"Sorry, there is not enough {ingredient}")
#             return False
#         return True

def insert_coins():
    print("Please insert coins.")
    quarters_amount = int(input("How many quarters?: "))
    dimes_amount = int(input("How many dimes?: "))
    nickles_amount = int(input("How many nickles?: "))
    pennies_amount = int(input("How many pennies?: "))

    total_amount = (quarters_amount * 0.25) + (dimes_amount * 0.10) + (nickles_amount * 0.05) + (pennies_amount * 0.01)

    return total_amount

def check_transaction(inserted_money, drink_cost):
    if inserted_money >= drink_cost:
        change = round(inserted_money - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")

        resources["money"] += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_drink(drink_name, order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            return False
        else:
            resources[ingredient] -= order_ingredients[ingredient]
            print

coffee_machine_status = True

while coffee_machine_status:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "espresso".lower():
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            inserted_money = insert_coins()
            if inserted_money >= MENU["espresso"]["cost"]:
                resources["money"] += MENU["espresso"]["cost"]

                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]

                if inserted_money > MENU["espresso"]["cost"]:
                    change = inserted_money - MENU["espresso"]["cost"]
                    print(f"Here is ${change:.2f} dollars in change.")

                print("Here is your espresso. Enjoy!")
            else:


        elif resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")



    elif user_input == "latte".lower():
        pass



    elif user_input == "cappuccino".lower():
        pass



    elif user_input == "report".lower():
        print(f"Water: {resources["water"]}ml" + "\n" + f"Milk: {resources["milk"]}ml" + "\n" + f"Coffee: {resources["coffee"]}g" + "\n" + f"Money: ${resources["money"]}")



    elif user_input == "off".lower():
        break
