# U04_EX08_LineSegment_Info.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 07 Nov 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 07
#     Source: Python Programming
#    Chapter: 04
#
# Program Description
#  This program allows the user to draw a line segment with two clicks
# and then displays its midpoint, its length, and its slope. The midpoint
# will be a cyan dot in the middle of the segment, and the length and slop will
# be printed as text near the top of the window. This program uses the formula (dy/dx)
# and for length it uses sqrt( dx ** 2 + dy ** 2). Click anywhere to begin!
#
# Algorithm (pseudocode)
"""
- from graphics import *
- from math import *

- define main function
    - initialize <width> and <height> at 600 and 600 respectively
    - create a new window <win> titled "Line Segment Information" with width of 600 and a height of 600
    - set coordinates of <win> to (-10,-10, 10, 10)

    - draw introduction at (0, 2) with a size of 16 double spaced

    - wait for mouse click

    - draw grid lines
    - draw mid labels for grid lines
    - draw instruction "click to place first point" at (-5, 8)

    - set <p1> to mouse click

    - set x1 to mouse click x
    - set y1 to mouse click y
    - draw a point <p1>

    - un-draw first instruction
    - draw instruction "click to place second point" at (-5, 8)

    - set <p2> to mouse click
    - un-draw second instruction

    - set x2 to mouse click x
    - set y2 to mouse click y
    - draw a point <p2>

    - draw line from p1 to p2

    - draw midpoint <m> at Point((x1 + x2)/2, (y1 + y2)/2)
    - set <m> color to cyan

    - set dx = x2 - x1
    - set dy = y2 - y1
    - set slope = dy / dx
    - set length = sqrt(dx ** 2 + dy ** 2)

    - draw Text(Point(-5,8), "Line length: " + str(round(length, 2)) + "\nSlope: " + str(round(slope,2)))

    - draw exit dialogue in bottom right corner
    - wait for mouse click and close the window

- define other functions
- run main()
"""
from graphics import *
from math import *


def main():
    width, height = 600, 600
    win = GraphWin("Line Segment Information", width, height)
    win.setCoords(-10, -10, 10, 10)

    intro = return_introduction(0, 2, 16)
    intro.draw(win)

    win.getMouse()
    intro.undraw()

    draw_grid_lines(win)
    draw_grid_labels(win)

    instruction_1 = Text(Point(-5, 8), "Click to place first point" )
    instruction_1.draw(win)

    p1 = win.getMouse()
    instruction_1.undraw()

    x1, y1 = p1.getX(), p1.getY()

    p1.draw(win)
    instruction_2 = Text(Point(-5, 8), "Click to place second point" )
    instruction_2.draw(win)

    p2 = win.getMouse()
    instruction_2.undraw()

    x2, y2 = p2.getX(), p2.getY()

    p2.draw(win)
    Line(p1, p2).draw(win)

    m = Point((x1 + x2)/2, (y1 + y2)/2)
    m.setOutline("cyan")
    m.draw(win)

    dx = x2 - x1
    dy = y2 - y1
    slope = dy / dx
    length = sqrt(dx ** 2 + dy ** 2)

    Text(Point(-5, 8), "Line length: " + str(round(length, 2)) + "\n        Slope: " + str(round(slope, 2))).draw(win)

    exit_gate(5, -9, 5, win)
    win.close


def return_introduction(x, y, size):
    """
    - Function Description: returns Text object intro to be drawn into window

    - initialize intro as a Text object at point (<x>, <y>) with program description
    - set size of <intro> to <size>
    """
    intro = Text(Point(x, y),
                 "This program allows the user to draw\n\n" +
                 "a line segment with two clicks\n\n" +
                 "and then displays its midpoint, its\n\n" +
                 "length, and its slope. The midpoint\n\n" +
                 "will be a cyan dot in the middle of the segment,\n\n" +
                 "and the length and slope will\n\n" +
                 "be printed as text near the top of the window.\n\n" +
                 "This program uses the formula (dy/dx)\n\n" +
                 "and for length it uses sqrt( dx ** 2 + dy ** 2).n\n\n" +
                 "Click anywhere to begin!")

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


def draw_grid_labels(window):
    """
    - Function Description: draws the middle of graph labels for 5 and 0 on each axis

    - draw text 5 at (-.25, 5)
    - draw text -5 at (-.25, -5)
    - draw text 5 at (5, -.3)
    - draw text -5 at (-5, -.3)
    - draw text 0 at (-.25, -.3)
    """
    Text(Point(-.25, 5), "5").draw(window)
    Text(Point(-.25, -5), "-5").draw(window)
    Text(Point(5, -.3), "5").draw(window)
    Text(Point(-5, -.3), "-5").draw(window)
    Text(Point(-.25, -.3), "0").draw(window)


def draw_grid_lines(window):
    """
    - Function Description: draws the lines on the grid as described in the main algorithm

    - initialize grid line <y_axis> going from (0,10) to (0, -10)
        - set color to blue
    - initialize grid line <x_axis> going from (-10, 0) to (10, 0)
        - set color to blue

    """
    y_axis = Line(Point(0, 10), Point(0, -10))
    y_axis.setOutline("blue")

    x_axis = Line(Point(-10, 0), Point(10, 0))
    x_axis.setOutline("blue")

    y_axis.draw(window)
    x_axis.draw(window)


main()
