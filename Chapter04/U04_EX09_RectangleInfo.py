# U04_EX09_RectangleInfo.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 07 Nov 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 09
#     Source: Python Programming
#    Chapter: 04
#
# Program Description
#  This program allows the user to click to points using the mouse
# and create a rectangle from those two points. The program will give
# the area (l * w) of the rectangle as well as the perimeter (2(l + w)).
# Click anywhere to begin.
#
# Algorithm (pseudocode)
"""
- from graphics import *

- define main function
    - initialize <width> and <height> at 600 and 600 respectively
    - create a new window <win> titled "Rectangle Information" with width of 600 and a height of 600
    - set coordinates of <win> to (-10,-10, 10, 10)

    - draw introduction at (0, 2) with a size of 16 double spaced

    - wait for mouse click

    - draw instruction "click to place first corner" at (-5, 8)

    - set <p1> to mouse click

    - set x1 to mouse click x
    - set y1 to mouse click y
    - draw a point <p1>

    - un-draw first instruction
    - draw instruction "click to place second corner" at (-5, 8)

    - set <p2> to mouse click
    - un-draw second instruction

    - set x2 to mouse click x
    - set y2 to mouse click y
    - draw a point <p2>

    - draw Rectangle(p1, p2)
    - un-draw 2 points

    - length = abs(x2 - x1)
    - width = abs(y2 - y1)
    - area = length * width
    - perimeter = 2 * (length + width)

    - draw Text(Point(-5,8), "Area: " + str(round(area, 2)) + "\nPerimeter: " + str(round(perimeter,2)))

    - draw exit dialogue in bottom right corner
    - wait for mouse click and close the window

- define other functions
- run main()
"""
from graphics import *


def main():
    width, height = 600, 600
    win = GraphWin("Rectangle Information", width, height)
    win.setCoords(-10, -10, 10, 10)

    intro = return_introduction(0, 2, 16)
    intro.draw(win)

    win.getMouse()
    intro.undraw()

    instruction_1 = Text(Point(-5, 8), "Click to place first corner")
    instruction_1.draw(win)

    p1 = win.getMouse()
    instruction_1.undraw()

    x1, y1 = p1.getX(), p1.getY()

    p1.draw(win)
    instruction_2 = Text(Point(-5, 8), "Click to place second corner")
    instruction_2.draw(win)

    p2 = win.getMouse()
    instruction_2.undraw()

    x2, y2 = p2.getX(), p2.getY()

    p2.draw(win)
    Rectangle(p1, p2).draw(win)
    p2.undraw()
    p1.undraw()

    length = abs(x2 - x1)
    width = abs(y2 - y1)
    area = length * width
    perimeter = 2 * (length + width)

    Text(Point(-5, 8), "Area: " + str(round(area, 2)) + "\nPerimeter: " + str(round(perimeter, 2))).draw(win)

    exit_gate(5, -9, 5, win)
    win.close


def return_introduction(x, y, size):
    """
    - Function Description: returns Text object intro to be drawn into window

    - initialize intro as a Text object at point (<x>, <y>) with program description
    - set size of <intro> to <size>
    """
    intro = Text(Point(x, y),
                 "This program allows the user to click\n\n" +
                 "to points using the mouse\n\n" +
                 "and create a rectangle from those\n\n" +
                 "two points. The program will give\n\n" +
                 "the area (l * w) of the rectangle as\n\n" +
                 "well as the perimeter (2(l + w)).\n\n" +
                 "Click anywhere to begin.")
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
