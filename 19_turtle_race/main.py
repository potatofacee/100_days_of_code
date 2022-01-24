import turtle
import random

# user variables
width = 1000
height = 800

# spacing allows for 100 px on top and bottom, start and finish 50 px from LR
vertical_spacing = (height - 200) / 6
starting_x = -1 * (width / 2) + 50
starting_y0 = -1 * (height / 2) + 100 + ( vertical_spacing / 2)


screen = turtle.Screen()
screen.setup(width=width, height=height)

user_bet = turtle.textinput(title="Place your bets!",
                            prompt="Who do you think will win the race? ( red, orange, "
                                   "yellow, green, blue, purple )")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

for turtle_index in range(0,6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    y0 = starting_y0 + vertical_spacing * turtle_index
    new_turtle.goto(starting_x, y0)
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

list_of_dists = [2, 2, 2, 3, 4, 8]
while is_race_on:

    for turt in turtles:
        if turt.xcor() > (width/2) - 20:
            is_race_on = False
            winning_color = turt.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning color is {winning_color}.")
            else:
                print(f"You've lost. The winning color is {winning_color}.")
        turt.forward(random.choice(list_of_dists))



screen.exitonclick()
