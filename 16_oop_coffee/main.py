from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
#menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})\n").lower()

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    elif choice in options:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            is_paid = money_machine.make_payment(drink.cost)
            if is_paid:
                coffee_maker.make_coffee(drink)
            else:
                print("sorry, pony up more cash")

        else:
            print("sorry, resources not sufficient")
    else:
        print("choose something reasonable, dingus")