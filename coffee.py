user_choice = ''
Machine_is_off = False
coffee = {}
cup = {
    "espresso": {
        "price": 1.5,
        "Water": 50,
        "Coffee": 18,
        "Milk": 0,
    },
    "latte": {
        "price": 2.5,
        "Water": 200,
        "Coffee": 24,
        "Milk": 150,
    },
    "cappuccino": {
        "price": 3.0,
        "Water": 250,
        "Coffee": 24,
        "Milk": 100,
    }
}
report = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0,
}
while not Machine_is_off:
    
    while user_choice != "espresso" or "latte" or "cappuccino" or "off" or "report":
        user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
        if user_choice == "espresso":
            coffee = cup["espresso"]
            break
        elif user_choice == "latte":
            coffee = cup["latte"]
            break
        elif user_choice == "cappuccino":
            coffee = cup["cappuccino"]
            break
        elif user_choice == "off":
            Machine_is_off = True
        else:
            print("You've entered a wrong choice. Please try again...")
            user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    print("Please insert coins. ")
    quarters = float(input(" how many quarters?: "))
    dimes = float(input(" how many dimes?: "))
    nickles = float(input(" how many nickles?: "))
    pennies = float(input(" how many pennies?: "))

    cash = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    change = cash - coffee["price"]
    if change >= 0:
        report["Water"] -= coffee["Water"]
        report["Coffee"] -= coffee["Coffee"]
        report["Milk"] -= coffee["Milk"]
        report["Money"] += coffee["price"]
        print(f"Here is your {change} in change.")
        print(f"Here is your {user_choice} ☕. Enjoy!")
