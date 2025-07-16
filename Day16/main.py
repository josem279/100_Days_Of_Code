# Intermediate - beginning with OOP


################## Intro to OOP
# from turtle import Turtle, Screen

# # Class constuctor
# timmy = Turtle()
# print(timmy)

# # Attributes
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)

# # Functions
# my_screen.exitonclick()

################## Intro to python packages + Pypi
# from prettytable import PrettyTable
# table = PrettyTable()

# table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])

# print(table.align)
# table.align = "l"

# print(table)

################## Coffee Machine Challenge in OOP

from menu import Menu
from coffee_machine import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}:\n")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)








