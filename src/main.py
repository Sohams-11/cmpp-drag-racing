from turtle import Turtle, Screen 
import random


screen = Screen()
screen.setup(1000, 800)
screen.bgcolor("green")

finish_line= Turtle("turtle", visible=False)
finish_line.color("white")
finish_line.penup()
finish_line.goto(500,-400)
finish_line.pendown()
finish_line.goto(500,400)


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
    turtlelist[i].showturtle()
    turtlelist[i].speed(random.randint(1, 10))
    turtlelist[i].setx(200)
    

  

screen.exitonclick()






#SHAPES- arrow, turtle, circle, sauare, triangle, classic, blank 