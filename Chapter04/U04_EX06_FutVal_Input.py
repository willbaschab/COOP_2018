# U04_EX06_FutVal_Input.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 05 Nov 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 06
#     Source: Python Programming
#    Chapter: 04
#
# Program Description
#
# This program plots the growth of a 10-year investment with a bar graph
# from 0.0k to 10.0k. Input the initial principal value and the apr in the boxes below
# to see the principal compounded (principal * (1 + apr)) over ten years on a graph.
#
# Algorithm (pseudocode)
"""
- from graphics import *
- define main function
    - initialize width and height at 1024/32 and 576/32 respectively
    - create a new graphics window, <win>, named "Investment Growth Chart" with width 1024 and height 576
        - set background to white
    - draw introduction in center of screen with double space with appropriate size text
    - set coordinates to (0.0, 0.0, width, height)
    - draw text "Initial Principal Amount:" with appropriate size at (6, 6)
    - draw entry box for principal with initial value 0.0 at (10, 6)
    - do the same process for apr except that it is symmetrical to the the principal inputs
    - wait for mouse click to run program and un-draw all things
    - store value from entry boxes as floats in <principal> and <apr> respectively
    - set coordinates to (-1.75, -200, 11.5, 10400)
    - draw labels function
    - initialize first green bar at principal amount
    - begin for loop from 1 to 11 (10 years)
        - principal = principal * (1 + apr)
        - draw bar at new points with new principal and next year
    - create exit dialogue at top left of screen and wait for click to exit.
    - close window
- define other functions
- run main
"""
from graphics import *


def main():
    width, height = 1024/32, 576/32
    win = GraphWin("Investment Growth Chart", 1024, 576)

    intro = Text(Point(width/2, height - height/3),
                 "This program plots the growth of a 10-year investment with a bar graph\n\n" +
                 "from 0.0k to 10.0k. Input the initial principal value and the apr in the boxes below\n\n "
                 "to see the principal compounded (principal * (1 + apr)) over ten years on a graph.\n\n" +
                 "After you input the values, please click anywhere to begin the program.")
    intro.setSize(19)
    intro.draw(win)
    win.setCoords(0.0, 0.0, width, height)

    principal_text = Text(Point(5, 6), "Initial Principal Amount:")
    principal_entry = Entry(Point(9, 6), 5)
    principal_entry.setText("0.0")
    principal_text.draw(win)
    principal_entry.draw(win)

    apr_text = Text(Point(22, 6), "                     APR:")
    apr_entry = Entry(Point(26, 6), 5)
    apr_entry.setText("0.0")
    apr_text.draw(win)
    apr_entry.draw(win)

    win.getMouse()
    intro.undraw()
    principal_text.undraw()
    principal_entry.undraw()
    apr_entry.undraw()
    apr_text.undraw()

    principal = float(principal_entry.getText())
    apr = float(apr_entry.getText())

    win.setCoords(-1.75, -200, 11.5, 10400)
    draw_labels(win)

    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.draw(win)

    Text(Point(0.25, 8750), "Click anywhere to close window").draw(win)
    win.getMouse()
    win.close()


def draw_labels(win):
    """
    - (This function draws the labels for the graph based on the coordinates defined in the main function)
    - draw label at 0 and -1 with 0.0k
    - draw label at 2500 and -1 with 2.5k
    - draw label at 5000 and -1 with 5.0k
    - draw label at 7500 and -1 with 7.5k
    - draw label at 10000 and -1 with 10.0k
    """
    Text(Point(-1, 0), " 0.0K").draw(win)
    Text(Point(-1, 2500), " 2.5K").draw(win)
    Text(Point(-1, 5000), " 5.0K").draw(win)
    Text(Point(-1, 7500), " 7.5K").draw(win)
    Text(Point(-1, 10000), " 10.0K").draw(win)


main()
