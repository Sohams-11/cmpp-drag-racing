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

turtle_color=["red","blue","yellow","brown","pink","cyan","purple","orange","maroon"]


for i in range(0, len(turtlelist)):
    turtlelist[i].penup()
    turtlelist[i].color(turtle_color[i])
    turtlelist[i].shapesize(2,2)
    turtlelist[i].goto(0, i * 50)
    turtlelist[i].showturtle()
    
       
    
while True:
    for i in range(0, len(turtlelist)):
        turtlelist[i].forward(random.randint(1,10))
        if turtlelist[i].pos()[0]>500:
            screen.exitonclick()

  













#SHAPES- arrow, turtle, circle, sauare, triangle, classic, blank 