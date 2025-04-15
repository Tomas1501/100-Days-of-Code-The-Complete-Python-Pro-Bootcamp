from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


snake = Snake()
# segments = []
# for position in starting_positions: 
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     # print(position)
#     new_segment.goto(position)
#     segments.append(new_segment)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    # for seg_num in range(len(segments) -1, 0, -1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x,new_y)
    # segments[0].forward(20)
    

    

                
screen.exitonclick()