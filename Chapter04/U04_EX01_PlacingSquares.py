# U04_EX01_PlacingSquares.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 22 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 01
#     Source: Python Programming
#    Chapter: 04
#
# Program Description
# This program allows you to place 11 red squares that are 20 by 20 pixels
# To begin, left click with the mouse to close this text, and place
# red squares with left click. Remember, you can only draw 10 including the
# first square already drawn, so choose wisely.
#
#
#
# Algorithm (pseudocode)
# - Import everything from graphics
# - Import random.py
# - set <width> and <height> to 768 and 480 respectively (This is a ratio of length to width for screen resolution)
# - create new Graphics window titled "draw circles" with width and height set as <width> and <height>
# - set rectangle width and height to 20 (because it is a square)
# - Print introduction text in center screen with double spaces and reasonable size (draw variable text to window)
# - Wait for mouse input to move on with program, then un-draw introduction
# - set point values for corners of square
#   - p1 is original point, so it gets values 50 for x and 50 for y
#   - p2 is the x and y of p1 decreased (because of coordinate system) by rectangle width and height variables
# respectively.
# - create shape variable as a rectangle set at p1 and p2 with red outline and fill. Draw this to window.
# - begin for loop in range of 10 (because original program only lets user go 10 times at placing squares)
#   - <p> set to mouse location when mouse is clicked on window (we get p's x and y)
#   - <c> set to center of shape
#   - <dx> set to mouse x minus shape center x
#   - <dy> set to mouse y minus shape center y
#   - create new shape that is clone of original square
#   - move this shape by <dx> in the x  direction and <dy> in the  direction
#   - draw this to window
# - Create textbox with text "click again to quit" in center of screen at a reasonable size
# - wait for mouse click from user, and close program

from graphics import *


def main():

    width, height = 768, 480
    win = GraphWin("draw circles", width, height)

    rectwidth = 20
    rectheight = 20

    t1 = Text(Point(width/2, height/2), "This program allows you to place 11 red squares that are 20 by 20 pixels\n\n" +
                                        "To begin, left click with the mouse to close this text, and place\n\n" +
                                        "red squares with left click. Remember, you can only draw 10 including the\n" +
                                        "\nfirst square already drawn, so choose wisely.")
    t1.setSize(17)
    t1.draw(win)
    win.getMouse()
    t1.undraw()

    p1 = Point(50, 50)
    p2 = Point(p1.getX() - rectwidth, p1.getY() - rectheight)

    shape = Rectangle(p1, p2)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        newshape = shape.clone()
        newshape.move(dx, dy)
        newshape.draw(win)

    t = Text(Point(width/2, height/2), "Click again to quit")
    t.setSize(25)
    t.draw(win)
    win.getMouse()
    win.close()


main()
