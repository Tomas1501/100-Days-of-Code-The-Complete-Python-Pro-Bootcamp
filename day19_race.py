from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[turtle_index])
    all_turtles.append(new_turtle)
    # print(all_turtles)
    
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color")
print(user_bet)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("Congratulations. You are winner")
            else:
                print(f"Sorry. You loose, {winning_color} turtle win")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        
                



screen.exitonclick()