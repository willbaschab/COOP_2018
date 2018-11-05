# U04_EX04_WinterScene.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 04
#     Source: Python Programming
#    Chapter: 04
#
# Program Description:
#  This program will draw a Winter scene comprised of 4 trees, snow, and a snow man.
# The snowman is made from three balls of snow, which are circles in the program,
# an orange orange carrot nose (a rectangle), and two black coal eyes (circles).
# The 4 Fir trees in the picture are drawn with a rectangular stump, and triangular leaves
# that get smaller and small towards the tip of the tree. Each tree is different.
# Enjoy the scene, left click to view it and click again to exit.
#
# Algorithm (pseudocode)
#   - from graphics import *
#   - define other functions
#   - Define main function:
#       - define variables width, height, and center (as the center point)
#       - create new window with title "Winter Scene", and with width and height variables
#       - Print introduction textbox, double spaced in middle of window, and wait for click to close it
#       - set background to cyan
#       - draw white horizon rectangle starting at 1/3 of the height down, and completely covering that part of screen
#       - set a treesize and leaf_amount variable for all four trees to use that the program will draw
#       - draw four trees, each at the same y (below the horizon) and with x positions symmetrical to the center
# of the screen
#       - draw snowman using function drawsnowman() at center of screen on window with a nice size
#       - Print exit textbox, with instruction "click again to exit" double spaced in middle of window,
# and wait for click to close it.
#       - Close graphic window
#

from graphics import *


def main():
    width, height = 1024, 576
    center = Point(width / 2, height / 2)

    win = GraphWin("Winter Scene", width, height)

    intro = Text(center,
                 "This program will draw a Winter scene comprised of 4 trees, snow, and a snow man.\n\n" +
                 "The snowman is made from three balls of snow, which are circles in the program,\n\n" +
                 "an orange orange carrot nose (a rectangle), and two black coal eyes (circles).\n\n" +
                 "The 4 Fir trees in the picture are drawn with a rectangular stump, and triangular leaves\n\n" +
                 "that get smaller and small towards the tip of the tree. Each tree is different.\n\n" +
                 "Enjoy the scene, left click to view it and click again to exit.")
    intro.setSize(19)
    intro.draw(win)
    win.getMouse()
    intro.undraw()

    win.setBackground("cyan")

    horizon = Rectangle(Point(0 , height * 1/3), Point(width, height))
    horizon.setFill("white")
    horizon.setOutline("white")
    horizon.draw(win)

    treesize, leaf_amount = 60, 16
    drawtree(width * 2 / 3, height * 2 / 3, treesize, leaf_amount, win)
    drawtree(width * 1 / 3, height * 2 / 3, treesize, leaf_amount, win)
    drawtree(width * 1 / 8, height * 2 / 3, treesize, leaf_amount, win)
    drawtree(width * 7 / 8, height * 2 / 3, treesize, leaf_amount, win)

    drawsnowman(center.getX(), center.getY(), 50, win)

    end = Text(Point(width / 2, height * 7 / 8), "Click again to exit")
    end.setSize(20)
    end.draw(win)
    win.getMouse()
    win.close()


def drawsnowman(xpos, ypos, size, window):
    """
    ALGORITHM:
  - set <centerpoint> as a point at xpos, ypos
  - set bottom to Circle at <centerpoint> with a radius of size
  - set middle to circle at xpos, and ypos minus a portion of the size with a radius of a portion of the size
  - set top to Circle at xpos, and ypos minus a small portion of the size with a radius of a smaller
portion of the size
  - create arm that goes straight through y of middle circle, and has a length proportional to the figure.
  - set the width of the arm to a tenth of <size>
  - set the fill of the arm to brown
  - set fill of each circle "white"
  - set lefteye to circle with same y position as <top>, but with x being xpos minus portion of size, and have a
radius of a portion of the size. Fill is black.
  - right eye is a clone of left moved 2 times what value is subtracted from xpos in the left eye
  - nose is a rectangle drawn with points porportional to figure
      - first point is to left of center by some portion of the size, and its y is the sum between the
top circle's y and the size times some portion
      - second point is to right of center by some portion of size, and its y is the sum between the
top circle's y and the size times some portion
  - draw each shape to <window> in order: bottom, arm, middle, top, lefteye, right eye, nose
    """
    centerpoint = Point(xpos, ypos)

    bottom = Circle(centerpoint, size)
    middle = Circle(Point(xpos, ypos - (1 * size)), size * .75)
    top = Circle(Point(xpos, ypos - (2 * size)), size * .5)

    arm = Line(Point(middle.getCenter().getX() + size * 2, middle.getCenter().getY()),
               Point(middle.getCenter().getX() - size * 2, middle.getCenter().getY()))
    arm.setWidth(size/10)
    arm.setFill("brown")

    top.setFill("white")
    middle.setFill("white")
    bottom.setFill("white")

    lefteye = Circle(Point(xpos - (size * .2),  ypos - (2 * size)), size/10)
    lefteye.setFill("Black")

    righteye = lefteye.clone()
    righteye.move(2 * (size * .2), 0)

    nose = Rectangle(Point(xpos - (size * .05), top.getCenter().getY() + (size * .2)),
                     Point(xpos + (size * .05), top.getCenter().getY() + (size * .6)))
    nose.setFill("orange")
    nose.setOutline("white")

    bottom.draw(window)
    arm.draw(window)
    middle.draw(window)
    top.draw(window)
    lefteye.draw(window)
    righteye.draw(window)
    nose.draw(window)


def drawleaf(xpos, ypos, base, height, window):
    """
    - (This function draws an isosceles triangle that faces up (its base is below its center)
    given the x and y of the point when equidistant from each vertex;
    the length of the base; the height of the triangle; and what window it will be drawn to.
     It will be used in this instance to draw the leaves of a christmas tree)
    - define vertex point having same x, but with a y above the center by half the height
    - define the left most point to have an x to the left of the center by half of the base, and a y below the center
    by half f the height (so that it is on the base line of the triangle)
    - define the right most point similar to left with the exception of it being to the right of the center by half
    the height.
    - initialize a new polygon object with the points of the vertex, left, and right
    - set the fill and outline of this object to green
    - draw the polygon to <window> as defined in function arguments
    """
    vertex = Point(xpos, ypos - 1/2 * height)
    left = Point(xpos - 1/2 * base, ypos + 1/2 * height)
    right = Point(xpos + 1/2 * base, ypos + 1/2 * height)
    t = Polygon(vertex, left, right)
    t.setFill("green")
    t.setOutline("green")
    t.draw(window)


def drawtree(xpos, ypos, size, leaf_amount, window):
    """
    - (This function draws a christmas tree with an x, y representing the center of the small base (a rectangle); a size
    argument for how large the tree is; the amount of leaves the tree will have, and the window which the function draws
    objects to)
    - initialize <base> as rectangle object
        - top left point is half the size to the left of <xpos>, and minus <size> from <ypos>
        - top right point is half the size to the right of <xpos>, and plus <size> from <ypos>
    - set fill to brown
    - draw to window (as defined in args>

    - set variable of a leaf's y position to the <ypos> - size so that the center is on the base
    - set variable of the leaf's base to be 3 times <size>
    - set variable of a a leaf's height to be the size / (leaf_amount/size + .35) (aka, proportional)
    - drawleaf() at <xpos>, leaf_y with a base of <leaf_base> and a height of <leaf_height> in window <window>
    - begin a 'for' loop in the range of <leaf_amount>
        - set <leaf_base> to <leaf_base> divided by 1.08
        - set <leaf_height> to <leaf_height> divided by 1.08
        - set <leaf_y> to <leaf_y> - <leaf_amount>
        - drawleaf(xpos, leafy_y, leaf_base, leaf_height, window)
    """
    base = Rectangle(Point(xpos - 1/2 * size, ypos - size),
                     Point(xpos + 1/2 * size, ypos + size))
    base.setFill("brown")
    base.draw(window)

    leaf_y = ypos - size
    leaf_base = size * 3
    leaf_height = size / (leaf_amount/size + .35)
    drawleaf(xpos, leaf_y, leaf_base, leaf_height, window)

    for i in range(leaf_amount):
        leaf_base = leaf_base/1.08
        leaf_height = leaf_height/1.08
        leaf_y -= leaf_amount
        drawleaf(xpos, leaf_y, leaf_base, leaf_height, window)


main()
