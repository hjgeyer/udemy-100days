from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

beverage_menu = Menu()
beverage_maker = CoffeeMaker()
money_maker = MoneyMachine()

def print_full_report():
    beverage_maker.report()
    money_maker.report()

more_orders = True

while more_orders:
    print(print_full_report())
    drink = input(f"What drink would you like to order?: ({beverage_menu.get_items()}) ").lower()

    if drink not in ('espresso', 'latte', 'cappuchino', 'report'):
        more_orders = False
        break
    elif drink == 'report':
        print_full_report()
    else:
        drink = beverage_menu.find_drink(order_name=drink)

        if beverage_maker.is_resource_sufficient(drink):
            if money_maker.make_payment(drink.cost):
                beverage_maker.make_coffee(drink)