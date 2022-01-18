import turtle
import random


# torq = turtle.Turtle()
# torq.shape("triangle")
# torq.color("DarkOrchid4")
# torq.speed(3)
# torq.pensize(2)


#
# # draw a square
# torq.penup()
# torq.forward(100)
# torq.right(90)
# torq.pendown()
# torq.forward(100)
# torq.right(90)
# torq.forward(200)
# torq.right(90)
# torq.forward(200)
# torq.right(90)
# torq.forward(200)
# torq.right(90)
# torq.forward(100)
# torq.right(90)
# torq.penup()
# torq.forward(100)
#
# i = 0
# while i in range(15):
#     torq.pendown()
#     torq.forward(10)
#     torq.penup()
#     torq.forward(10)
#
# screen = turtle.Screen()
# screen.exitonclick()

# make a turtle draw from 3 to ten sided objects with top border aligned

def make_shape(lilturtle, num_sides, side_length, init_heading, color_tuple):
    """draws shape with num_sides of length side_length"""
    lilturtle.seth(init_heading)
    i = 0
    turning_angle = 360 / num_sides
    while i < num_sides:
        lilturtle.pendown()
        lilturtle.color(color_tuple)
        lilturtle.forward(side_length)
        lilturtle.right(turning_angle)
        i += 1


def pick_a_color():
    rgb_code = []
    for hue in range(0, 3):
        rgb_code.append(random.randint(1, 255))
    return tuple(rgb_code)


def choose_direction():
    poles = [0, 90, 180, 270]
    direction = random.choice(poles)
    return direction


# side_length = 50
# max_num_sides = 100
#
# torq = turtle.Turtle()
# screen = turtle.Screen()
#
# torq.shape("triangle")
# torq.speed(10)
# torq.pensize(2)
# torq.penup()
# screen.colormode(255)
#
# # move to starting point
# torq.seth(180)
# torq.forward((side_length / 2))
# torq.seth(90)
# torq.forward(500)
# torq.seth(0)
#
# for num_sides in range(3, max_num_sides + 1):
#     color = pick_a_color()
#     print(num_sides)
#     make_shape(lilturtle=torq, num_sides=num_sides, side_length=side_length, init_heading=0, color_tuple=color)

# torq = turtle.Turtle()
#
# turtle.bgcolor("black")
# torq.shape("triangle")
# torq.speed(0)
# torq.pensize(2)
# turtle.colormode(255)
#
# walking_distance = 30
#
# for _ in range(500):
#     torq.seth(choose_direction())
#     torq.pendown()
#     torq.color(pick_a_color())
#     torq.forward(walking_distance)

turtle.colormode(255)
torq = turtle.Turtle()

#turtle.bgcolor("black")
torq.shape("triangle")
torq.speed(0)
torq.pensize(2)
torq.pendown()

initial_heading = 90
turtle.seth(initial_heading)
gap_size = 1

for _ in range(0,360,gap_size):
    torq.color(pick_a_color())
    torq.circle(200)
    torq.left(gap_size)

screen = turtle.Screen()
screen.exitonclick()
