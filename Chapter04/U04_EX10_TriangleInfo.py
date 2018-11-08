# U04_EX10_TriangleInfo.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 07 Nov 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 10
#     Source: Python Programming
#    Chapter: 04
#
# Program Description
#  This program allows the user to click on the screen
# to draw the vertices of a triangle. The program
# will draw this triangle and output the perimeter and area
# of the triangle. The perimeter will be calculated by
# adding all the sides together, and the area
# will be calculated by using Heron's Formula.
# Click anywhere to begin.
#
# Algorithm (pseudocode)
"""
- from graphics import *
- from math import *

- define main function
    - initialize <width> and <height> at 600 and 600 respectively
    - create a new window <win> titled "Triangle Information" with width of 600 and a height of 600
    - set coordinates of <win> to (-10,-10, 10, 10)

    - draw introduction at (0, 2) with a size of 16 double spaced

    - wait for mouse click

    - draw instruction "click to place first vertex" at (-5, 8)

    - set <p1> to mouse click

    - set x1 to mouse click x
    - set y1 to mouse click y
    - draw a point <p1>

    - un-draw first instruction
    - draw instruction "click to place second vertex" at (-5, 8)

    - set <p2> to mouse click
    - un-draw second instruction

    - set x2 to mouse click x
    - set y2 to mouse click y
    - draw a point <p2>


    - un-draw second instruction
    - draw instruction "click to place third vertex" at (-5, 8)

    - set <p3> to mouse click
    - un-draw third instruction

    - set x3 to mouse click x
    - set y3 to mouse click y
    - draw a point <p3>


    - draw Polygon(p1, p2, p3)
    - un-draw 3 points

    - length1= sqrt((x2 - x1) ** 2 + (y2 - y1)** 2)
    - length2 = sqrt((x2 - x3) ** 2 + (y2 - y3)** 2)
    - length3 = sqrt((x1 - x3) ** 2 + (y1 - y3)** 2)

    - perimeter = length1 + length2 + length3
    - s = perimeter/2
    - area = sqrt(s * (s - length1) * (s - length2) * (s - length3))

    - draw Text(Point(-5,8), "Area: " + str(round(area, 2)) + "\nPerimeter: " + str(round(perimeter,2)))

    - draw exit dialogue in bottom right corner
    - wait for mouse click and close the window

- define other functions
- run main()
"""
from graphics import *
from math import *


def main():
    width, height = 600, 600
    win = GraphWin("Triangle Information", width, height)
    win.setCoords(-10, -10, 10, 10)

    intro = return_introduction(0, 2, 16)
    intro.draw(win)

    win.getMouse()
    intro.undraw()

    instruction_1 = Text(Point(-5, 8), "Click to place first vertex")
    instruction_1.draw(win)

    p1 = win.getMouse()
    instruction_1.undraw()

    x1, y1 = p1.getX(), p1.getY()

    p1.draw(win)
    instruction_2 = Text(Point(-5, 8), "Click to place second vertex")
    instruction_2.draw(win)

    p2 = win.getMouse()
    instruction_2.undraw()

    x2, y2 = p2.getX(), p2.getY()

    p2.draw(win)

    instruction_3 = Text(Point(-5, 8), "Click to place third vertex")
    instruction_3.draw(win)

    p3 = win.getMouse()
    instruction_3.undraw()

    x3, y3 = p3.getX(), p3.getY()

    p3.draw(win)

    Polygon(p1, p2, p3).draw(win)
    p2.undraw()
    p1.undraw()
    p3.undraw()

    length1 = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    length2 = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    length3 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

    perimeter = length1 + length2 + length3
    s = perimeter / 2
    area = sqrt(s * (s - length1) * (s - length2) * (s - length3))

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
                 "This program allows the user to click on the screen\n\n" +
                 "to draw the vertices of a triangle. The program\n\n" +
                 "will draw this triangle and output the perimeter and area\n\n" +
                 "of the triangle. The perimeter will be calculated by\n\n" +
                 "adding all the sides together, and the area\n\n" +
                 "will be calculated by using Heron's Formula.\n\n" +
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
