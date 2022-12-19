#First we import the packages or modules
#If a specific class from a package will be used better to specify as is below
from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
"""here we created an object of screen class, 
used the object to access canvas height attribute and print it out
also we used exitonclick method to display screen"""
# my_screen = Screen()

# print(my_screen.canvheight)
# my_screen.exitonclick()

"""Installing Pretty table package 
from the file option in the navbar I went to settings
from the project drop own went to python interpreter
searched for PrettyTable package, selected and installed it"""
table = PrettyTable()

#I used the add_column method to create the columns
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])

#Here I use an attribute to set the table content alignment
table.align = "l"
print(table)