# TODO prompt the user to find what they want
# TODO check user input and decide what do to next
# TODO are resources sufficient?
# TODO prompt should show after every action

# TODO keep an inventory of coffee, money, milk, and water
# TODO coin operated money system

# menu items: latte, espresso, cappuccino: kv of ingredients, cost
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

# water milk coffee
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

accepted_coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05
}


def print_report(resources, profit):
    ### prints a report of resources and profit ###

    for k in resources:
        print(f'{k}:\t {resources[k]}')
    print(f'money:\t ${profit}')


def check_resources(drink, resources, menu):
    have_resources = True
    for ingredient in resources:
        qty_req = menu[drink]["ingredients"][ingredient]
        qty_have = resources[ingredient]

        print(f'You require {qty_req} and have {qty_have} {ingredient}.')

        if qty_have < qty_req:
            print(f'Sorry, there is not enough {ingredient}.')
            have_resources = False

    return have_resources


def collect_money(accepted_coins):
    money_received = 0
    for coin in accepted_coins:
        c = int(input(f"How many {coin}s?: "))
        money_received += c * accepted_coins[coin]
    return money_received


def make_drink(drink, resources, menu):
    for ingredient in resources:
        resources[ingredient] -= menu[drink]["ingredients"][ingredient]
    print(f"Here is your {drink}. Enjoy!")


profit = 0

is_on = True

while is_on:
    have_resources = False
    choice = input("What would you like? (espresso/latte/cappuccino)\n").lower()

    # admin commands
    if choice == "off":
        is_on = False
    if choice == "report":
        print_report(resources, profit)

    # drink making
    if choice in MENU:
        have_resources = check_resources(drink=choice, resources=resources, menu=MENU)

    if have_resources:
        money_input = collect_money(accepted_coins)
        drink_price = MENU[choice]["cost"]
        if money_input >= drink_price:
            profit += drink_price

            if money_input > drink_price:
                overage = money_input - drink_price
                print(f"Here is your change of ${overage}.")
            make_drink(drink=choice, resources=resources, menu=MENU)
        else:
            print("Sorry that's not enough money. Money refunded.")
