from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


is_on = True
while is_on:
    drink_input = input(f"What would you like to drink? {menu.get_items()}")
    drink = " "
    if drink_input == "off":
        is_on = False
    elif drink_input == "report":
        money_machine.report()
        coffee_maker.report()
    elif drink_input == "add":
        menu.add_item()
    else:
        drink = menu.find_drink(drink_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)





