from turtle import Turtle, Screen 
import random


screen = Screen()
screen.setup(1000, 800)
screen.bgcolor("green")

turtlelist=[ Turtle("turtle", visible=False), 
Turtle("turtle", visible=False),
Turtle("turtle", visible=False),
Turtle("turtle", visible=False),
Turtle("turtle", visible=False),
Turtle("turtle", visible=False),
Turtle("turtle", visible=False),
Turtle("turtle", visible=False)
]
    


for i in range(0, len(turtlelist)):
    turtlelist[i].penup()
    turtlelist[i].color("maroon")
    turtlelist[i].shapesize(2,2)
    turtlelist[i].goto(0, i * 50)
    turtlelist[i].speed(random.randint(1, 10))
    turtlelist[i].showturtle()
    turtlelist[i].setx(200)
    

    print(turtlelist[i])

screen.exitonclick()






#SHAPES- arrow, turtle, circle, sauare, triangle, classic, blank 