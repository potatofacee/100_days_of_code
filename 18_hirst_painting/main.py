import colorgram
import turtle
import random


colors = colorgram.extract("image.jpg", 16)


def draw_dot_and_move(lilturtle, color, next_heading, next_distance):
    lilturtle.dot(9, color)
    lilturtle.seth(next_heading)
    lilturtle.forward(next_distance)


def choose_color(list_of_colors):
    color = random.choice(list_of_colors).rgb
    color_list = [color[0], color[1], color[2]]
    return tuple(color_list)


def position_startup(lilturtle, dots_horizontally, dots_vertically, dot_distance):
    lilturtle.seth(180)
    lilturtle.forward(int(dot_distance * dots_horizontally / 2))
    lilturtle.seth(270)
    lilturtle.forward(int(dot_distance * dots_vertically / 2))
    lilturtle.seth(0)


def determine_heading(dots_horizontally, step, prev_heading):
    next_step = step + 1
    if (next_step % dots_horizontally) == 0:
        return 90
    elif (next_step % (2 * dots_horizontally)) == 1:
        return 0
    elif (next_step % dots_horizontally) == 1:
        return 180
    else:
        return prev_heading


# print(colors[0])
dots_horizontally = 50
dots_vertically = 20
dot_distance = 30

screen = turtle.Screen()
torq = turtle.Turtle()
turtle.colormode(255)
torq.shape("triangle")
torq.penup()
torq.speed(0)

step = 0


def draw(lilturtle, dots_horizontally, dots_vertically, dot_distance, step):
    position_startup(torq, dots_horizontally, dots_vertically, dot_distance)

    for i in range(dots_horizontally * dots_vertically):
        color = choose_color(colors)
        prev_heading = lilturtle.heading()
        heading = determine_heading(dots_horizontally, step, prev_heading)
        draw_dot_and_move(lilturtle, color, heading, dot_distance)
        step += 1


draw(torq, dots_horizontally, dots_vertically, dot_distance, step)

screen.exitonclick()
