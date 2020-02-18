
import turtle as t
import string
import random

from tkinter import simpledialog, messagebox

askingforspeed = True

t.hideturtle
t.fillcolor('green')
t.bgcolor('black')
t.pendown()
t.width('10')

randcolor = ['red', 'blue', 'green', 'yellow','lime',]

while askingforspeed == True:
    askspeed = simpledialog.askstring('enter speed','how fast? s = slow | m = medium | f = fast')
    if askspeed == 's':
        a_speed = 3
        askingforspeed = False
    elif askspeed == 'm':
        a_speed = 5
        askingforspeed = False
    elif askspeed == 'f':
        a_speed = 8
        askingforspeed = False
    else:
        messagebox.showwarning('Error!', 'That is not "s", "m", or "f". Please type the speed again')

t.speed(a_speed)

while True:


    colour = random.choice(randcolor)

    t.color(colour)

    x = random.randrange(-300, 300)
    y = random.randrange(-300, 300)

    print(' ')

    print('x = ', x)

    print('y = ', y)

    t.goto(int(y), int(x))