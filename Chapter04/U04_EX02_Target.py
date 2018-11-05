# U04_EX02_Target.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 22 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 02
#     Source: Python Programming
#    Chapter: 04
#
# Program Description
#  This program will draw an archery target that consists
# of a yellow central circle surrounded by concentric rings of
# red, blue, black, and white. Each ring has the same width.
#
# Algorithm (pseudocode)
# - from graphics import *
# - <width> and <height> = 1536 and 864
# - point <center> is at half width and half height
# - create a new window <win> titled "archery target" with width and height being <width> and <height>
# - print introduction in center of screen with double space with appropriate size text
# - wait for mouse signal and remove box when received
# - create a list <colors> with colors white, black, blue, red, and yellow
# - <thickness> set to 25
# - <radius> set to colors length plus one times <thickness>
# - begin for loop in range of length of <colors>
#   - <radius> = radius - thickness
#   - <c> = Circle at center point with radius <radius>
#   - <c> filled and outlined to colors.i
#   - draw <c> to window
# - create textbox with "click again to quit" at (width/2, 40)
# - wait for user click
# - close window
from graphics import *


def main():
    width, height = 1536, 864
    center = Point(width/2, height/2)

    win = GraphWin("Archery Target", width, height)

    intro = Text(center,
                 "This program will draw an archery target that consists of\n\n" +
                 "a yellow central circle surrounded by concentric rings of\n\n" +
                 "red, blue, black, and white. Each ring has the same width.\n\n" +
                 "Click to begin.")
    intro.setSize(20)
    intro.draw(win)
    win.getMouse()
    intro.undraw()

    colors = ["white", "black", "blue", "red", "yellow"]
    thickness = 50
    radius = (len(colors) + 1) * thickness

    for i in range(len(colors)):
        radius = radius - thickness
        c = Circle(center, radius)
        c.setFill(colors[i])
        c.setOutline(colors[i])
        c.draw(win)

    end = Text(Point(width/2, 40), "Click again to exit")
    end.setSize(20)
    end.draw(win)
    win.getMouse()
    win.close()


main()

