import turtle

# constants for turtle to draw the
SHORT_LENGTH = 25  # height of half bar
LONG_LENGTH = 50  # height of full bar
STEP = 15  # distance between bars
T_SPEED = 20  # draw speed of turtle
T_SIZE = 5  # pen size of turtle

# setting turtle starting states and conditions
draw = turtle
draw.hideturtle()  # make turtle no visible
draw.speed(T_SPEED)  # set turtle speed
draw.pensize(T_SIZE)  # set turtle pen size
draw.penup()
draw.goto(-400, 0)  # move the turtle's starting location
draw.pendown()


# print a short, half bar on the screen
# turtle initially faces right with pen down
def short(t):
    # draw bar
    t.left(90)
    t.forward(SHORT_LENGTH)

    # lift pen to stop drawing
    t.penup()

    # go back to previous location
    t.backward(SHORT_LENGTH)

    # turn to the right and move forward to create space between bars
    t.right(90)
    t.forward(STEP)

    # set pen down for next bar
    t.pendown()


# print a long, full bar on the screen
# turtle initially faces right with pen down
def long(t):
    # draw bar
    t.left(90)
    t.forward(LONG_LENGTH)

    # lift pen to stop drawing
    t.penup()

    # go back to previous location
    t.backward(LONG_LENGTH)

    # turn to the right and move forward to create space between bars
    t.right(90)
    t.forward(STEP)

    # set pen down for next bar
    t.pendown()


# prints barcode for digit 0
def print_zero():
    long(draw)
    long(draw)
    short(draw)
    short(draw)
    short(draw)


# prints barcode for digit 1
def print_one():
    short(draw)
    short(draw)
    short(draw)
    long(draw)
    long(draw)


# prints barcode for digit 2
def print_two():
    short(draw)
    short(draw)
    long(draw)
    short(draw)
    long(draw)


# prints barcode for digit 3
def print_three():
    short(draw)
    short(draw)
    long(draw)
    long(draw)
    short(draw)


# prints barcode for digit 4
def print_four():
    short(draw)
    long(draw)
    short(draw)
    short(draw)
    long(draw)


# prints barcode for digit 5
def print_five():
    short(draw)
    long(draw)
    short(draw)
    long(draw)
    short(draw)


# prints barcode for digit 6
def print_six():
    short(draw)
    long(draw)
    long(draw)
    short(draw)
    short(draw)


# prints barcode for digit 7
def print_seven():
    long(draw)
    short(draw)
    short(draw)
    short(draw)
    long(draw)


# prints barcode for digit 8
def print_eight():
    long(draw)
    short(draw)
    short(draw)
    long(draw)
    short(draw)


# prints barcode for digit 9
def print_nine():
    long(draw)
    short(draw)
    long(draw)
    short(draw)
    short(draw)


# prints barcode for start and stop, which is just one full bar
def print_start_stop():
    long(draw)
