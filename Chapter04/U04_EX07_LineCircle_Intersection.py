# U04_EX07_LineCircle_Intersection.py
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
#  This program takes the input of the radius of a circle centered at (0,0) and the y intercept of a horizontal line
# and outputs a graph of where that line will intersect with the circle if it intersects at all. It will display the
# point(s) where the circle and the line meet in red, and show the x value(s) of the meeting place(s) to the side
#
# Algorithm (pseudocode)
"""
- from graphics import *
- from math import *

- define main function
    - initialize <width> and <height> at 600 and 600 respectively
    - create a new window <win> titled "Circle and Line Intersection" with width of 600 and a height of 600
    - set coordinates of <win> to (-10,-10, 10, 10)

    - draw introduction at (0, 4) with a size of 16 double spaced

    - draw "Circle Radius:" text at (-7.5, -8)
    - draw radius entry box at (-5.2, -8) with a width of 3
        - set default value of radius entry to 0.0

    - draw "Line Y-Intercept:" text at (5.5, -8)
    - draw y_intercept entry box at (8, -8) with a width of 3
        - set default value of radius entry to 0.0

    - wait for mouse click and clear the screen

    - set radius to float(<value of radius entry box>)
    - set line_y to float(<value of y intercept entry box>)

    - draw grid lines
    - draw mid labels for grid lines

    - draw line in black from (-10, line_y) to (10, line_y)
    - draw circle in black at (0,0) with a radius of <radius>

    - If abs(line_y) > <radius>:
        - Text in center of 4th quadrant (not the 5th) that says "The line does not intersect with the circle"

    - Else If abs(line_y) = <radius>:
        - line_x = 0
        - draw point <p> (in red) at (line_x, line_y)
        - draw text "(" + string(line_x) + ", " + string(line_y) + ")" at (line_x - .25, line_y +.5)

    - Else:
        - left_x = -1 *(sqrt((radius ** 2) - (line_y ** 2))
        - right_x = sqrt((radius ** 2) - (line_y ** 2)

        - draw point <left> (in red) at (left_x, line_y)
        - draw point <right> (in red) at (right_x, line_y)

        - draw text "(" + string(round(left_x, 2)) + ", " + string(line_y) + ")" at (left_x - .5, line_y +.5)
        - draw text "(" + string(round(right_x, 2)) + ", " + string(line_y) + ")" at (right_x + .5, line_y +.5)

    - draw exit dialogue in bottom right corner
    - wait for mouse click and close the window

- define other functions
- run main()
"""
from graphics import *
from math import *


def main():
    width, height = 600, 600
    win = GraphWin("Circle and Line Intersection", width, height)
    win.setCoords(-10, -10, 10, 10)

    intro = return_introduction(0, 4, 16)
    intro.draw(win)

    circle_text = Text(Point(-7.5, -8), "Circle Radius:")
    circle_entry = Entry(Point(-5.2, -8), 3)
    circle_entry.setText(0.0)

    circle_text.draw(win)
    circle_entry.draw(win)

    line_y_text = Text(Point(5.5, -8), "Line Y-Intercept:")
    line_y_entry = Entry(Point(8, -8), 3)
    line_y_entry.setText(0.0)

    line_y_text.draw(win)
    line_y_entry.draw(win)

    win.getMouse()  # Transition to next scene

    intro.undraw()
    circle_text.undraw()
    circle_entry.undraw()
    line_y_text.undraw()
    line_y_entry.undraw()

    radius = float(circle_entry.getText())
    line_y = float(line_y_entry.getText())

    draw_grid_lines(win)
    draw_grid_labels(win)

    Circle(Point(0, 0), radius).draw(win)
    Line(Point(-10, line_y), Point(10, line_y)).draw(win)

    if abs(line_y) > radius:
        Text(Point(5, -5), "The line does not\n" +
                           "intersect with the circle.").draw(win)
    elif abs(line_y) == radius:
        line_x = 0

        p = Point(line_x, line_y)
        p.setOutline("red")
        p.draw(win)

        Text(Point(line_x - .25, line_y + .5), "(" + str(line_x) + ", " + str(line_y) + ")").draw(win)
    else:
        left_x = -1 * (sqrt((radius ** 2) - (line_y ** 2)))
        right_x = sqrt((radius ** 2) - (line_y ** 2))

        left = Point(left_x, line_y)
        left.setOutline("red")
        left.draw(win)

        right = Point(right_x, line_y)
        right.setOutline("red")
        right.draw(win)

        Text(Point(left_x - .5, line_y + .5), "(" + str(round(left_x, 2)) + ", " + str(line_y) + ")").draw(win)
        Text(Point(right_x + .5, line_y + .5), "(" + str(round(right_x, 2)) + ", " + str(line_y) + ")").draw(win)

    exit_gate(5, -9, 5, win)
    win.close


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


def return_introduction(x, y, size):
    """
    - Function Description: returns Text object intro to be drawn into window

    - initialize intro as a Text object at point (<x>, <y>) with program description
    - set size of <intro> to <size>
    """
    intro = Text(Point(x, y),
                 "This program takes the input of the radius of a circle centered\n\n" +
                 "at (0,0) and the y intercept of a horizontal line\n\n" +
                 "and outputs a graph of where that line will intersect\n\n" +
                 "with the circle if it intersects at all. It will display the\n\n" +
                 "point(s) where the circle and the line meet in red, and show the\n\n" +
                 "coordinates of the meeting place(s) to the side. To start, enter\n\n" +
                 "the radius and y intercept below and click anywhere to begin!")
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
