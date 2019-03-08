# U07_EX17_BouncingBall.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 05 Mar 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 17
#     Source: Python Programming
#    Chapter: 07
#
#
# Program Description
#  This program animates a bouncing circle
# in a square area with 4 walls. The circle
# will move randomly.
#
# Algorithm (pseudocode)
"""
- from graphics import *
- import random

- define Speed class
- define other functions

- define main
    - run drawscreen() function
"""
from graphics import *
import random


class Speed:
    """
    This class holds modifiers for speed:
        - the rate of change in the x axis
        - the rate of change in the y axis

    This class holds methods:
        - it's constructor
            - get x and y speed from method args
            - set specific object's x and y rate of change to x and y method args
        - ability to write rate of x axis change
            - set specific object's x rate of change to method arg
        - ability to write rate of y axis change
            - set specific object's y rate of change to method arg
        - ability to read rate of x axis change
                - return specific object's x rate of change
        - ability to read rate of y axis change
                - return specific object's y rate of change

    """
    def __init__(self, xpseed, yspeed):
        self.xspeed = xpseed
        self.yspeed = yspeed

    def setxspeed(self, newspeed):
        self.xspeed = newspeed

    def setyspeed(self, newspeed):
        self.yspeed = newspeed

    def getXSPEED(self):
        return self.xspeed

    def getYSPEED(self):
        return self.yspeed


def drawintro(win, width, height):
    """
    This function draws the introduction and is immutable

    ALG:
    - create a text object with the introduction in it, set the font to times roman and the style to bold
    - set the size to whatever fits the most on the screen
    - draw it to the window, wait for the mouse to continue and undraw it
    """
    intro = Text(Point(width/2, height/2),
                 'This program animates a bouncing circle' +
                 '\n\nin a square area with 4 walls. The circle' +
                 '\n\nwill move randomly.')
    intro.setFace('times roman')
    intro.setStyle('bold')
    intro.setSize(20)
    intro.draw(win)
    win.getMouse()
    intro.undraw()


def drawcircle(cx, cy):
    """
    This program draw the initial circle object, but it will also return the object after it sets it up

    ALG:
    - create a Circle object at the x and y coordinates provided in the function args
    - fill the circle black
    - return the Circle object to where it was called
    """
    c = Circle(Point(cx, cy), .5)
    c.setFill('black')
    return c


def check_box_clicked(box, pt):
    """
    This function is mutable for any rectangle object as long as that object's p1 is the lower left corner
    of the rectangle and it's p2 is the upper right corner. The function checks if the area inside a rectangle
    object has been clicked

    ALG:
    - set intermediate x and y values to mouse x and mouse y
    - check if the x and y are inside the box using the box's outer coordinate values
        -return True if True, return False is False
    """
    x, y = pt.getX(), pt.getY()
    if (box.getP1().getX() <= x <= box.getP2().getX()) and (box.getP1().getY() <= y <= box.getP2().getY()):
        return True
    else:
        return False


def colorchange(win, ball):
    """
    This function changes the color of the circle every time it collides with a wall

    ALG:
    - create 3 variables that each hold a random number from  1 to 255 <r>, <g>, <b>
    - set the fill of ball object to the rgb status of the 3 variables
    - set the outline of the ball object to the same status as the fill
    = set the background color of the window to the same status as the fill
    """
    r = random.randrange(1, 255)
    b = random.randrange(1, 255)
    g = random.randrange(1, 255)
    ball.setFill(color_rgb(r, g, b))
    ball.setOutline(color_rgb(r, g, b))
    win.setBackground(color_rgb(r, g, b))


def checky(win, ball, dy):
    """
    The most important function in the program, checky serves the purpose of not only always
    defining the direction of the ball on the y axis, but also checking if the ball has hit
    either the top or bottom wall and returning an opposite direction to the caller

    ALG:
    - check if the ball object's upper right bounding point y value plus 1 pixel (rounded to three decimal points)
    is >= 9 (y coordinate of the top wall) or if the ball object's lower left bounding point minus 1 pixel (rounded to
    three decimal points) is <= 1 (y coordinate of bot wall)
        - run colorchange because the ball hit
        - switch direction to opposite so that it goes away from the wall
    """
    if round(ball.getP2().getY(), 3) + .001 >= 9 or round(ball.getP1().getY(), 3) - .001 <= 1:
        colorchange(win, ball)
        return -1 * dy

    else:
        return dy


def checkx(win, ball, dx):
    """
    The most important function in the program, checkx serves the purpose of not only always
    defining the direction of the ball on the x axis, but also checking if the ball has hit
    either the left or right wall and returning an opposite direction to the caller

    ALG:
    - check if the ball object's upper right bounding point x value plus 1 pixel (rounded to three decimal points)
    is >= 9 (x coordinate of right wall) or if the ball object's lower left bounding point minus 1 pixel (rounded to
    three decimal points) is <= 1 (x coordinate of left wall)
        - run colorchange because the ball hit
        - switch direction to opposite so that it goes away from the wall
    """
    if round(ball.getP2().getX(), 3) + .001 >= 9 or round(ball.getP1().getX(), 3) - .001 <= 1:
        colorchange(win, ball)
        return -1 * dx
    else:
        return dx


def drawscreen():
    """
    This is the graphic version of main(). It runs all functions

    ALG:
    - Initialize variables at the start of function
        - create a Speed object <ballspeed> constructed with a random x axis speed and y axis speed
        (random as in .001 pixels/loop to .010 pixels/loop for both)
        - create two direction variables that are either in a negative or positive state (-1 or 1)

    # create window
    - make a new window with title 'Target Practice' and width 500 by 500
    - set window coordinates to (0.0, 0.0, 10.0, 10.0)

    # first introduction scene
    - run intro function

    # main area scene initialization
    - fill the screen with black
    - create the bounding box rectangle for the ball
    - create the quit box (the graphic box and text that let the user quit)
        - create the outer rectangle object from 4,0 to 6,1 (lower left corner to upper right corner)
        - fill the rectangle white (so that it sticks out from the background)
        - create the text at the midpoint of the rectangle, saying "Click here to quit"
        - draw both objects to the window
    - create the increase box (the graphic box and text that let the user increase the speed of the ball)
        - create the outer rectangle object from 6,0 to 8,1 (lower left corner to upper right corner)
        - fill the rectangle white (so that it sticks out from the background)
        - create the text at the midpoint of the rectangle, saying "Click here to increase ball speed"
        - draw both objects to the window
    - create the decrease box (the graphic box and text that let the user decrease the speed of the ball)
        - create the outer rectangle object from 2,0 to 4,1 (lower left corner to upper right corner)
        - fill the rectangle white (so that it sticks out from the background)
        - create the text at the midpoint of the rectangle, saying "Click here to decrease ball speed"
        - draw both objects to the window

    - create a Circle object using drawcircle() in the center of screen and draw it to window

    # Animation state
    - Start while True loop:
        - check for a mouse click and assign it to an object <pt> if click happens
        - If <pt> is not empty (the mouse clicked)
            - Check if it clicked in the quit box and break the loop if it did
        - else if <pt> is in the increase box:
            - create two variables to represent the new
            x and y speed (calculated by getting the old speed and adding .001)
            - set the <ballspeed> x and y speeds to corresponding variables
        - else if <pt> is in the decrease box:
            - create two variables to represent the new
            x and y speed (calculated by getting the old speed and subtracting .001)
            - set the <ballspeed> x and y speeds to corresponding variables

        - to figure out which direction to go, and to check if the ball is touching a wall,
        set the variables dx and dy (d for direction) to checkx and checky functions respectively

        - move the ball by it's velocity (direction, which -1 or 1, times speed for x and y)

        - allow the while loop to run 60 times per second.

    # Program end state
    - close window
    """
    ballspeed = Speed(random.randrange(1, 10)/1000, random.randrange(1, 10)/1000)
    dx = random.choice([1, -1])
    dy = random.choice([1, -1])
    # debug: print(dx, dy)
    # debug: print(ballspeed.getXSPEED(), ballspeed.getYSPEED())
    win = GraphWin('Bouncing Circle', 1000, 1000)
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    drawintro(win, 10, 10)
    win.setBackground('black')
    boundary = Rectangle(Point(1, 9), Point(9, 1))
    boundary.setFill("white")
    boundary.draw(win)

    quit_box = Rectangle(Point(4, 0), Point(6, 1))
    quit_box.setFill("white")
    quit_text = Text(Point(5, .5), 'Click here to quit')
    quit_box.draw(win)
    quit_text.draw(win)

    increase_box = Rectangle(Point(6, 0), Point(8, 1))
    increase_box.setFill("white")
    increase_text = Text(Point(7, .5), 'Click here to\n\nincrease ball speed')
    increase_box.draw(win)
    increase_text.draw(win)

    decrease_box = Rectangle(Point(2, 0), Point(4, 1))
    decrease_box.setFill("white")
    decrease_text = Text(Point(3, .5), 'Click here to\n\ndecrease ball speed')
    decrease_box.draw(win)
    decrease_text.draw(win)

    ball = drawcircle(5, 5)
    ball.draw(win)

    while True:
        pt = win.checkMouse()
        if pt:
            if check_box_clicked(quit_box, pt):
                break
            elif check_box_clicked(increase_box, pt):
                changex = ballspeed.getXSPEED() + .001
                changey = ballspeed.getYSPEED() + .001
                ballspeed.setxspeed(changex)
                ballspeed.setyspeed(changey)
                # debug: print(ballspeed.getXSPEED(), ballspeed.getYSPEED())
            elif check_box_clicked(decrease_box, pt):
                changex = ballspeed.getXSPEED() - .001
                changey = ballspeed.getYSPEED() - .001
                ballspeed.setxspeed(changex)
                ballspeed.setyspeed(changey)
                # debug: print(ballspeed.getXSPEED(), ballspeed.getYSPEED())

        dy = checky(win, ball, dy)
        dx = checkx(win, ball, dx)

        ball.move(dx * ballspeed.getXSPEED(), dy * ballspeed.getYSPEED())
        update(60)

    win.close()


def main():
    drawscreen()


if __name__ == '__main__':
    main()


