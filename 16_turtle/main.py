# import turtle
#
# torq = turtle.Turtle()
# torq.shape('turtle')
# torq.color('Coral')
#
# my_screen = turtle.Screen()
# print(my_screen.canvheight, my_screen.canvwidth)
#
# #torq.forward(100)
#
# turtle.color('red', 'yellow')
# turtle.begin_fill()
# while True:
#     torq.forward(200)
#     torq.left(170)
#     if abs(torq.pos()) < 1:
#         break
# torq.end_fill()
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon', ['Pikachu', 'Charmander', 'Squirtle'])
table.add_column('Type', ['Electric', 'Fire', 'Water'])
print(table)
table.align = 'l'
print(table)

