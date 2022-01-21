import turtle

torq = turtle.Turtle()
screen = turtle.Screen()

screen.listen()


def move_forward():
    torq.forward(10)


def move_backward():
    torq.backward(10)


def turn_left():
    torq.left(5)


def turn_right():
    torq.right(5)


def clear_torq():
    torq.penup()
    torq.clear()
    torq.home()
    torq.pendown()


screen.onkey(fun=move_forward, key="Up")
screen.onkey(fun=move_backward, key="Down")
screen.onkey(fun=turn_left, key="Left")
screen.onkey(fun=turn_right, key="Right")
screen.onkey(fun=clear_torq, key="c")

screen.exitonclick()