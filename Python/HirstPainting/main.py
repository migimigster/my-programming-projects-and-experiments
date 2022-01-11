###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import turtle as turtle
import random

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), 
        (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),(233, 175, 164),
        (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), 
        (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
hirst = turtle.Turtle()
turtle.colormode(255)
hirst.speed("fastest")
hirst.hideturtle()
hirst.width(10)
hirst.setheading(225)
hirst.penup()
hirst.fd(300)
hirst.setheading(0)
dots = 100
for i in range(1,dots+1):
    hirst.dot(20,random.choice(color_list))
    hirst.penup()
    hirst.fd(50)
    hirst.pendown()
    if i%10==0:
        hirst.penup()
        hirst.setheading(90)
        hirst.fd(50)
        hirst.setheading(180)
        hirst.fd(500)
        hirst.setheading(0)

screen = turtle.Screen()
screen.exitonclick()