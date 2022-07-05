from turtle import Turtle, Screen 
import random

screen = Screen()
screen.setup(1000, 800)
screen.bgcolor("green")

my_turtle = Turtle("turtle")
my_turtle.color("red")
my_turtle.shapesize(3,3)
my_turtle.penup()
my_turtle.goto(600, 0)
my_turtle.position(10,5)
my_turtle.speed(random.randint(1, 10))

my_turtle_2 = Turtle("turtle")
my_turtle_2.color("yellow")
my_turtle_2.shapesize(3,3)
my_turtle_2.penup()
my_turtle_2.goto(700,0)
my_turtle_2.position()
my_turtle_2.speed(random.randint(1, 10))
screen.exitonclick()






#SHAPES- arrow, turtle, circle, sauare, triangle, classic, blank 