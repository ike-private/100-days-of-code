from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu = Menu()
money = MoneyMachine()


def main():
    while True:
        order = input(f"What would you like? {menu.get_items()}? ").lower()
        if order == "report":
            machine.report()
            money.report()
        elif order == "off":
            exit()
        elif order in menu.get_items():
            coffee = menu.find_drink(order)
            if machine.is_resource_sufficient(coffee):
                if money.make_payment(coffee.cost):
                    machine.make_coffee(coffee)
        else:
            print("Drink is not on the menu")


main()
