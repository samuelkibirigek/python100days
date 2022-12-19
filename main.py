from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


coffee = menu.get_items()
is_on = True

while is_on:
  choice = input(f"What would you like? ({coffee}):")
  drink = menu.find_drink(choice)
  if choice == "off":
    is_on = False
  elif choice == "report":
    print(coffee_maker.report())
    print(money_machine.report())     
  elif coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
    coffee_maker.make_coffee(drink)
    