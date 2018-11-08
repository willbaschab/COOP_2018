# U04_EX05_StraightDice.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 05 Nov 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 05
#     Source: Python Programming
#    Chapter: 04
#
# Program Description
#  This program will draw five dice depicting a straight (1, 2, 3, 4, 5) or (2, 3, 4, 5, 6)
# in this instance, it depicts a straight of (1, 2, 3, 4, 5)
#
#
# Algorithm (pseudocode)
"""
- from graphics import *

- define necessary functions

- define main function
    - create new window with title "Straight Dice", and with a width of 600 and a size of 600
    - set the window coordinates for <win> to (0.0, 0.0) for left point and (16.0, 16.0) for right point
    - define variables width, height, and center (as the center point)

    - Print introduction textbox, double spaced in middle of window, and wait for click to close it

    - set background to green

    - draw_side1(2, height/2, win)
    - draw_side2(5, height/2, win)
    - draw_side3(8, height/2, win)
    - draw_side4(11, height/2, win)
    - draw_side5(14, height/2, win)

    - Print exit textbox, with instruction "click again to exit" double spaced in top space of window,
 and wait for click to close it.
    - Close graphic window

- main()
"""
from graphics import *


def draw_die_face(x, y, window):
    """
    - (This function will draw the square face of a die given the center x and y of that square and the window
    to draw to. It does not draw the die, but only the square that the holes are placed on.)
    - create Rectangle object <d>
        - top left point is at (x - 1, y + 1)
        - bottom right point is at (x + 1, y - 1)
    - set fill of d to "white"
    - set width to 1 / 4
    """

    d = Rectangle(Point(x - 1, y + 1), Point(x + 1, y - 1))
    d.setFill("white")
    d.setWidth(1 / 4)
    d.draw(window)


def draw_die_hole(x, y, window):
    """
    - This function draws the hole or indent in the die for every face and number
    - create Circle object <h>
        - center is at (x,y)
        - radius is 1/8
    - set fill to "black"
    """

    c = Circle(Point(x, y), 1 / 8)
    c.setFill("black")
    c.draw(window)


def draw_side1(x, y, window):
    """
    - This function draws the side of a die with one dot in the center
    - draw_die_face(x, y, window)
    - draw_die_hole(x, y, window)
    """

    draw_die_face(x, y, window)
    draw_die_hole(x, y, window)


def draw_side2(x, y, window):
    """
    - This function draws the side of a die with two dots
    - draw_die_face(x, y, window)
    - draw_die_hole(x + 1/2, y - 1/2, window)
    - draw_die_hole(x - 1/2, y + 1/2, window)
    """

    draw_die_face(x, y, window)
    draw_die_hole(x + 1 / 2, y - 1 / 2, window)
    draw_die_hole(x - 1 / 2, y + 1 / 2, window)


def draw_side3(x, y, window):
    """
    - This function draws the side of a die with three dots
    - draw_die_face(x, y, window)
    - draw_die_hole(x, y, window)
    - draw_die_hole(x + 1 / 2, y - 1 / 2, window)
    - draw_die_hole(x - 1 / 2, y + 1 / 2, window)
    """

    draw_die_face(x, y, window)
    draw_die_hole(x, y, window)
    draw_die_hole(x + 1 / 2, y - 1 / 2, window)
    draw_die_hole(x - 1 / 2, y + 1 / 2, window)


def draw_side4(x, y, window):
    """
    - This function draws the side of a die with 4 dots
    - draw_side2(x, y, window)
    - draw_die_hole(x + 1 / 2, y + 1 / 2, window)
    - draw_die_hole(x - 1 / 2, y - 1 / 2, window)
    """

    draw_side2(x, y, window)
    draw_die_hole(x + 1 / 2, y + 1 / 2, window)
    draw_die_hole(x - 1 / 2, y - 1 / 2, window)


def draw_side5(x, y, window):
    """
    - This function draws the side of a die with 5 dots
    - draw_side4(x, y, window)
    - draw_die_hole(x, y, window)
    """

    draw_side4(x, y, window)
    draw_die_hole(x, y, window)


def main():
    win = GraphWin("Straight Dice", 600, 600)
    win.setCoords(0.0, 0.0, 16.0, 16.0)
    width, height = 16.0, 16.0
    center = Point(width / 2, height / 2)

    intro = Text(center,
                 "This program will draw five dice\n\n" +
                 " depicting a straight (1, 2, 3, 4, 5) or (2, 3, 4, 5, 6).\n\n" +
                 "In this instance, it depicts a straight of (1, 2, 3, 4, 5).")
    intro.setSize(19)
    intro.draw(win)
    win.getMouse()
    intro.undraw()

    win.setBackground("green")

    draw_side1(2, height/2, win)
    draw_side2(5, height/2, win)
    draw_side3(8, height/2, win)
    draw_side4(11, height/2, win)
    draw_side5(14, height/2, win)

    end = Text(Point(width / 2, height * 7 / 8), "Click again to exit")
    end.setSize(20)
    end.draw(win)
    win.getMouse()
    win.close()


main()
