# U06_Ex06_TriangleArea.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 14 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 06
#     Source: Python Programming
#    Chapter: 06
#
# Program Description
#  This program allows the user to draw a triangle on the graphics window
# by clicking with the mouse. The program returns the area and perimeter of
# the triangle using a distance function.
#
# Algorithm (pseudocode)
"""
- import math and graphics

- define functions: square(x), distance(p1, p2),
area(p1, p2, p3), perimeter(p1, p2, p3)

- define main():
    - set new window with title "Draw a Triangle"
    - set coordinates (0.0, 0.0, 10.0, 10.0)

    - put introduction on screen
    - put message "Click on Three Points" at Point(5, .05)

    - Get and draw three vertices of triangle
    - Use Polygon object to draw the triangle

    - Calculate the perimeter using perimeter(p1, p2, p3)
    - Calculate the area using area(p1, p2, p3)

    - Wait for another click to exit
-run main()
"""
from graphics import *
import math


def distance(p1, p2):
    # uses distance formula and 2 point objects
    return math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)


def perimeter(p1, p2, p3):
    # adds the distances up
    return distance(p1, p2) + distance(p2, p3) + distance(p3, p1)


def area(p1, p2, p3):
    """
    - define sides and s in heron's formula
    - return heron's formula
   """
    s = perimeter(p1, p2, p3) / 2
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)

    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def main():
    win = GraphWin("Draw a Triangle", 1000, 1000)
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    intro = Text(Point(5, 5), "This program allows the user to\n\n" +
                 "draw a triangle on the graphics window\n\n" +
                 "by clicking with the mouse. The\n\n" +
                 "program returns the area and perimeter of\n\n" +
                 "the triangle using a distance function.\n\n" +
                 "To start, click anywhere.")

    intro.draw(win)

    win.getMouse()
    intro.undraw()

    message = Text(Point(5, .5), "Click on three points")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    message.setText(
        "The Perimeter is: {0:0.2f} and the Area is: {1:0.2f}".format(perimeter(p1, p2, p3), area(p1, p2, p3)))

    win.getMouse()
    win.close()


main()
