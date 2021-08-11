import turtle as t
import random
# import colorgram
#
#
# colors = colorgram.extract('hirst_spot_painting.jpg', 30)
# rgb_colors = []
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)
color_list = [(238, 245, 250), (249, 240, 244), (157, 76, 41), (211, 161, 93), (40, 108, 141), (12, 38, 61),
              (236, 200, 106), (215, 148, 21), (124, 175, 190), (72, 29, 16), (193, 142, 160), (65, 26, 40),
              (139, 66, 82), (13, 52, 34), (119, 35, 50), (131, 36, 25), (33, 169, 188), (201, 91, 124),
              (66, 113, 97), (141, 168, 161), (199, 87, 69), (134, 212, 226), (28, 86, 56), (90, 86, 15),
              (66, 157, 147), (15, 84, 100), (219, 175, 187), (223, 178, 167)]


timy = t.Turtle()
screen = t.Screen()
t.colormode(255)


timy.penup()
timy.speed("fastest")
timy.setpos(-180, -180)
timy.hideturtle()


vertical = -180
for _ in range(11):
    for _ in range(11):
        timy.dot(20, random.choice(color_list))
        timy.forward(50)
    timy.setpos(-180, vertical)
    vertical += 50


screen.exitonclick()