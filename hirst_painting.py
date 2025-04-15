import turtle as t
import random
# import colorgram

# colors = colorgram.extract('image.jpg', 81)

# rgb_colors=[]

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     rgb = (r,g,b)


#     rgb_colors.append(rgb)

# print(rgb_colors)
t.colormode(255)
tim = t.Turtle()

color_list = [(249, 245, 238), (240, 250, 246), (241, 246, 251), (251, 243, 248), (197, 146, 122), (35, 18, 15), (38, 100, 146), (234, 212, 95), (132, 89, 64), (9, 24, 52), (212, 89, 73), (195, 139, 161), (116, 170, 195), (37, 124, 83), (173, 162, 42), (13, 50, 32), (149, 65, 93), (195, 83, 114), (124, 187, 160), (13, 58, 134), (142, 18, 33), (63, 16, 21), (26, 196, 175), (20, 94, 60), (149, 218, 205), (25, 167, 213), (221, 174, 194), (124, 34, 28), (125, 219, 232), (234, 172, 163), (239, 203, 8), (102, 124, 163), (24, 81, 90), (174, 190, 214), (74, 71, 48)]

# print(random_color)


for _ in range(10):
    random_color = random.choice(color_list)
        # tim.home()/
    tim.dot(20,random_color)
    tim.forward(50)

draw_dots(random_color)        
Screen = t.Screen()
Screen.exitonclick()        
                