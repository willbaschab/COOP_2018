# U07_EX16_ArcheryTarget.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 27 Feb 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 16
#     Source: Python Programming
#    Chapter: 07
#
# Program Description
#  This program will draw an archery target and allow the user
# to click 5 points on the target representing shots fired at the target
# Using five-band scoring, a bulls-eye (yellow) is worth 9 points and
# each successive ring is worth 2 fewer points down to 1 for white.
# The program will display the score for each shot and will return
# the sum of all 5 shots.
#
# Algorithm (pseudocode)
"""
- import math
- from graphics import all

- define other functions

- define main
    -use drawscreen function (which is just main when dealing with graphics
"""
import math
from graphics import *


def drawtarget(center, layerwidth, win):
    """
    - This function draws the target with 5 different colors onto the window. It was copied from  4.2
    and is not mutable (originally it was, but this program is 5 band scoring, so adding a color to the
    list will destroy the program.

    ALG (copied from 4.2):
    - create a list <colors> with colors white, black, blue, red, and yellow
    - <thickness> set to 25
    - <radius> set to colors length plus one times <thickness>

    - begin for loop in range of length of <colors>
        - <radius> = radius - thickness
        - <c> = Circle at center point with radius <radius>
        - <c> filled and outlined to colors.i
        - draw <c> to window
    """
    colors = ["white", "black", "blue", "red", "yellow"]
    thickness = layerwidth/100
    radius = (len(colors) + 1) * thickness

    for i in range(len(colors)):
        radius = radius - thickness
        c = Circle(center, radius)
        c.setFill(colors[i])
        c.setOutline(colors[i])
        c.draw(win)


def calcdistance(p1, p2):
    """
    This function will return the distance between two points using the distance formula.

    ALG:
    - get x and y values of both points as variables
    - return result of distance formula with variables
    """
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def drawkey(win, p):
    """
    This function simplifies the drawing of the score key that tells the user the values of
    the target bands. It is mutable in the sense that you can change the argument that
    determines where the text is placed.

    ALG:
    - create text with formatting for point values,
    and edit the size of the text to be large enough for the window
    - draw to window
    """
    text = Text(p, "Point Values:" +
                   "\nYellow: 9"
                   "\nRed:    7"
                   "\nBlue:   5"
                   "\nBlack:  3"
                   "\nWhite:  1")
    text.setSize(15)
    text.draw(win)


def calcscore(p1, p2):
    """
    This function returns the correct score of each shot by using the distance between
    the shot and the center of the target as variables in the decision structure.

    ALG:
    - set variable equal to the distance between the two points

    - The window has a scale of 10 to 0, whereas the target function was not coded around this scale.
    In order to improvise, I made the target function and this function immutable (the arguments must
    stay the same). The width of each band in the target is .5 (50 originally), and the total radius
    is 2.5.
    - The decision structure should be based off of the knowledge above, using the distance as a
    variable in order to check which band the shot is in.
        - if in bullseye, return 9 points
        - if in red band, return 7 points
        - if in blue band, return 5 points
        - if in black band, return 3 points
        - if in white band, return 1 point
        - if the shot is not any of these, the user didn't hit the target and should not get any points
    """
    distance = calcdistance(p1, p2)
    if distance < .5:  # in yellow
        return 9
    elif distance < 1:  # in red
        return 7
    elif distance < 1.5:  # in blue
        return 5
    elif distance < 2:  # in black
        return 3
    elif distance < 2.5:  # in white
        return 1
    else:  # Not hitting the target
        return 0


def drawpoint(win):
    """
    This function draws the point where the user clicks, if in a certain area it is a different color,
    and returns the point object

    ALG:
    - set the point object equal to where the mouse clicked
    - create a larger circle around the point

    - check if the point is in the black band, and fill the circle purple if it is.
    If it is not then fill it black
    - draw the circle to the window
    - return the original point object
    """
    p = win.getMouse()
    c = Circle(p, .05)
    if 1.5 < calcdistance(p, Point(5, 5)) < 2:
        c.setFill('purple')
    else:
        c.setFill("black")
    c.draw(win)
    return p


def drawintro(win):
    """
    This function draws the introduction and is immutable

    ALG:
    - create a text object with the introduction in it, set the font to times roman and the style to bold
    - set the size to whatever fits the most on the screen
    - draw it to the window, wait for the mouse to continue and undraw it

    """
    intro = Text(Point(5, 5),
                 '\n\nThis program will draw an archery target and allow the user'
                 '\n\nto click 5 points on the target representing shots fired at the target'
                 '\n\nUsing five-band scoring, a bulls-eye (yellow) is worth 9 points and'
                 '\n\neach successive ring is worth 2 fewer points down to 1 for white.'
                 '\n\nThe program will display the score for each shot and will return'
                 '\n\nthe sum of all 5 shots. Click anywhere to start.')
    intro.setFace('times roman')
    intro.setStyle('bold')
    intro.setSize(11)
    intro.draw(win)
    win.getMouse()
    intro.undraw()


def drawscreen():
    """
    - make a new window with title 'Target Practice' and width 500 by 500
    - set window coordinates to (0.0, 0.0, 10.0, 10.0)

    - run intro function
    - draw the target at 5, 5 with a width of 50 pixels
    - draw the key at the top left of the screen

    - create a placeholder variable to hold the score
    - (very caveman of me) set a text object to act as the
    initial score of 0 and draw it to bottom right of window

    - start a for loop for each of the 5 shots the user gets
        - run the drawpoint function and store the result in
        a variable called p (p is for point)
        - undraw the original score as it is no longer correct
        - add the result of calcscore function between center and p to current score
        - recreate text display of score with new score and draw it to win

    - once the loop is over undraw the current score display and create a new object
    to hold the final score and draw it to the window

    - get the mouse and close the window

    """

    win = GraphWin('Target Practice', 500, 500)
    win. setCoords(0.0, 0.0, 10.0, 10.0)

    drawintro(win)
    drawtarget(Point(5, 5), 50, win)
    drawkey(win, Point(1.5, 8.5))
    currentscore = 0
    textscore = Text(Point(8, 1), "Current Score: {0}".format(0))
    textscore.draw(win)
    for i in range(5):
        p = drawpoint(win)
        textscore.undraw()
        currentscore += calcscore(p, Point(5, 5))
        textscore = Text(Point(8, 1), "Current Score: {0}".format(currentscore))
        textscore.draw(win)
    textscore.undraw()
    finalscore = Text(Point(5, 1), "Your final score was: {0}".format(currentscore) +
                                   "\nClick to Exit")
    finalscore.draw(win)
    win.getMouse()
    win.close()


def main():
    drawscreen()


if __name__ == '__main__':
    main()

"""
For calcscore:
RESULTS:
========
calcscore(Point(5, 5), Point(5.3, 5))   -->   9 |   9 | [ Pass ]
calcscore(Point(5, 5), Point(5.7, 5))   -->   7 |   7 | [ Pass ]
calcscore(Point(5, 5), Point(6.3, 5))   -->   5 |   5 | [ Pass ]
calcscore(Point(5, 5), Point(6.7, 5))   -->   3 |   3 | [ Pass ]
calcscore(Point(5, 5), Point(7.3, 5))   -->   1 |   1 | [ Pass ]
calcscore(Point(5, 5), Point(7.8, 5))   -->   0 |   0 | [ Pass ]
========
"""
