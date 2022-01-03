# from turtle import Turtle, Screen
# timmy=Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# timmy.circle(100)
# print(timmy)
# x=Screen()
# print(x.canvheight)
# x.exitonclick()


from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Charmander","Squirtle"])
table.add_column("Type",["Electric","Fire","Water"])
print(table)