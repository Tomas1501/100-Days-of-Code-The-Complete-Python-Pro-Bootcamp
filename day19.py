from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_back():
    tim.back(10)

def counter_clockwise():
    tim.left(30) 

def clockwise():
    tim.right(30)

def clearscreen():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_back, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clearscreen, "c")
screen.exitonclick()