# U04_EX11_FiveClickHouse.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 08 Nov 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 11
#     Source: Python Programming
#    Chapter: 04
#
# Program Description
#  This program allows the user to build a house in
# five easy clicks! in the first to clicks, the user
# draws a rectangle (the clicks representing the corners)
# that represents the house's frame. In the next click,
# the user places down the center point of the door into
# the house. The door's width is 1/5 of the whole house's
# width. The door is drawn from this point, and the user
# can place the center point of the window, which is half
# as wide as the door. The final click will represent the
# peak of the roof, and from that point lines will be drawn
# to the top edges of the house's frame in order to make the
# roof... well, look like a roof! The user should not feel
# the need to go over this introduction again as instructions
# will be provided and explained during the program!
# To begin, click anywhere.
#
# Algorithm (pseudocode)
"""
- from graphics import *

- define main function
    - initialize <width> and <height> at 600 and 600 respectively
    - create a new window <win> titled "5-Click House" with width of 600 and a height of 600
    - set coordinates of <win> to (-10,-10, 10, 10)

    - draw introduction at (0, 2) with a size of 16 double spaced

    - wait for mouse click

    - draw instruction "click to place top right corner of frame" at (-5, 8)

    - set <r1> to mouse click

    - set rx1 to mouse click x
    - set ry1 to mouse click y
    - draw a point <r1>

    - reset instruction to "click to place bottom left corner of frame
    - set <r2> to mouse click

    - set rx2 to mouse click x
    - set ry2 to mouse click y
    - draw a point <r2>

    - draw Rectangle(r1, r2)
    - un-draw points r1, r2

    - reset instruction to "click inside the frame to place center of top edge of door"

    - set <dc> to mouse click
    - set door_width = 1/5 * abs(rx2 - rx1)

    - <dl> = clone <dc>
    - move dl (-1/2 * door_width, 0)

    - <dr> = clone <dc>
    - move dr (1/2 * door_width, ry2 - dc.getY())

    - draw Rectangle(dl, dr)

    - reset instruction to "click inside the frame to draw the center of the window (and the window)"

    - set <wc> to mouse click
    - set window_width = 1/2 * door_width

    - set <wl> to clone of <wc>
    - move <wl> (-1/2 * window_width, 1/2 * window_width)

    - set <wr> to clone of <wc>
    - move <wr> (1/2 * window_width, -1/2 * window_width)

    - draw Rectangle(wl, wr)

    - reset instruction to "click to place peak of roof, which is above the top of the frame"

    - <pk> = mouse click

    - draw Line(pk, r1)
    - draw Line(pk, Point(r2.getX(), r1.getY())

    - reset instruction to "Your house is complete!"

    - draw exit dialogue in bottom right corner
    - wait for mouse click and close the window

- define other functions
- run main()
"""
from graphics import *


def main():
    width, height = 600, 600
    win = GraphWin("Triangle Information", width, height)
    win.setCoords(-10, -10, 10, 10)

    intro = return_introduction(0, 0, 12)
    intro.draw(win)

    win.getMouse()
    intro.undraw()

    instruction = Text(Point(-5, 8), "click to place top right corner of frame")
    instruction.draw(win)

    r1 = win.getMouse()

    rx1, ry1 = r1.getX(), r1.getY()
    r1.draw(win)

    instruction.setText("click to place bottom left corner of frame")

    r2 = win.getMouse()
    rx2, ry2 = r2.getX(), r2.getY()
    r2.draw(win)

    Rectangle(r1, r2).draw(win)
    r1.undraw()
    r2.undraw()

    instruction.setText("click inside the frame to place\nthe center of top edge of door")

    dc = win.getMouse()
    door_width = 1 / 5 * abs(rx2 - rx1)

    dl = dc.clone()
    dl.move(-1/2 * door_width, 0)

    dr = dc.clone()
    dr.move(1/2 * door_width, ry2 - dc.getY())

    Rectangle(dl, dr).draw(win)

    instruction.setText("click inside the frame to draw\nthe center of the window (and the window)")

    wc = win.getMouse()
    window_width = 1/2 * door_width

    wl = wc.clone()
    wl.move(-1/2 * window_width, 1/2 * window_width)

    wr = wc.clone()
    wr.move(1/2 * window_width, -1/2 * window_width)

    Rectangle(wl, wr).draw(win)

    instruction.setText("click to place peak of roof,\nwhich is above the top of the frame")

    pk = win.getMouse()

    Line(pk, r1).draw(win)
    Line(pk, Point(r2.getX(), r1.getY())).draw(win)

    instruction.setText("Your house is now complete!")

    exit_gate(5, -9, 5, win)
    win.close


def return_introduction(x, y, size):
    """
    - Function Description: returns Text object intro to be drawn into window

    - initialize intro as a Text object at point (<x>, <y>) with program description
    - set size of <intro> to <size>
    """
    intro = Text(Point(x, y),
                 "This program allows the user to build a house in\n\n" +
                 "five easy clicks! in the first to clicks, the user\n\n" +
                 "draws a rectangle (the clicks representing the corners)\n\n" +
                 "that represents the house's frame. In the next click,\n\n" +
                 "the user places down the center point of the door into\n\n" +
                 "the house. The door's width is 1/5 of the whole house's\n\n" +
                 "width. The door is drawn from this point, and the user\n\n" +
                 "can place the center point of the window, which is half\n\n" +
                 "as wide as the door. The final click will represent the\n\n" +
                 "peak of the roof, and from that point lines will be drawn\n\n" +
                 "to the top edges of the house's frame in order to make the\n\n" +
                 "roof... well, look like a roof! The user should not feel\n\n" +
                 "the need to go over this introduction again as instructions\n\n" +
                 "will be provided and explained during the program!\n\n" +
                 "To begin, click anywhere.")
    intro.setSize(size)
    return intro


def exit_gate(x, y, size, window):
    """
     - Function Description: returns Text object intro to be drawn into window as the exit dialogue and waits for
mouse to click
    - initialize exit as a Text object at point (<x>, <y>) with exit dialogue
    - set size of <exit> to <size>
    - draw <exit> to <window>
    - wait for mouse
    """
    exit_text = Text(Point(x, y), "click anywhere to close/exit")
    exit_text.size = size
    exit_text.draw(window)

    window.getMouse()


main()
