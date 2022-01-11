import turtle as t
import random
# colors = ["red","yellow","orange","green","blue","violet"]
t.colormode(255)
too=t.Turtle()
too.shape("classic")
def random_colors():
    a=random.randint(0,255)
    b=random.randint(0,255)
    c=random.randint(0,255)
    colors=(a,b,c)
    return colors
def spirograph(size_gap):
    for i in range(int(360/size_gap)):
        too.speed("fastest")
        too.color(random_colors())
        too.circle(100)
        current = too.heading()
        too.setheading(current+size_gap)
spirograph(10)

x = t.Screen()
x.exitonclick()
 
 