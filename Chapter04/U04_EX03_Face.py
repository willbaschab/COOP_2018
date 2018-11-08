# U04_EX03_Face.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 22 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 03
#     Source: Python Programming
#    Chapter: 04
#
# Program Description
#  This program will draw a yellow face with two black eyes,
# an orange nose, and a blank expression. The eyes, face, and nose
# are circles. The mouth is a straight line. Every part of the face
# is proportional to the whole.
#
# Algorithm (pseudocode)
# - from graphics import *
# - <width> and <height> = 1024 and 576
# - point <center> is at half width and half height
# - create a new window <win> titled "face" with width and height being <width> and <height>
# - print introduction in center of screen with double space with appropriate size text
# - wait for mouse signal and un-draw text box
# - set fradius to 100
# - set eradius to 1/5 of fradius
# - draw yellow circle face with radius of fradius at center of screen
# - draw right eye (black circles) above the center by 1/3 of fradius and right by 1/2 fradius with a radius of eradius
# - left eye is clone of right eye moved 2/3 of fradius to the left
# - draw brown nose at center with radius of eradius
# - draw mouth line first point 1/2 of fradius down and to the left
# - draw mouth line second point 1/2 of fradius down and to the right
# - draw mouth line with a width of 5 to window
# - create textbox with "click again to quit" at (width/2, 40)
# - wait for user click
# - close window


from graphics import *


def main():
    width, height = 1024, 576
    center = Point(width / 2, height / 2)

    win = GraphWin("Archery Target", width, height)

    intro = Text(center,
                 " This program will draw a yellow face with two black eyes,\n\n" +
                 "an orange nose, and a blank expression. The eyes, face, and nose\n\n" +
                 "are circles. The mouth is a straight line. Every part of the face\n\n" +
                 "is proportional to the whole.\n\n" +
                 "Click to begin.")
    intro.setSize(20)
    intro.draw(win)
    win.getMouse()
    intro.undraw()

    fradius = 100
    eradius = 1/5 * fradius

    face = Circle(center, fradius)
    face.setFill(color_rgb(255, 211, 68))
    face.draw(win)

    reyep = Point(center.getX() + (1/3 * fradius), center.getY() - (1/2 * fradius))
    reye = Circle(reyep, eradius)
    reye.setFill("Black")
    reye.draw(win)

    leye = (reye.clone())
    leye.move(-2/3 * fradius, 0)
    leye.draw(win)

    nose = Circle(Point(center.getX(), center.getY()), eradius)
    nose.setFill(color_rgb(214, 147, 70))
    nose.draw(win)

    mouthp1 = Point(center.getX() - (1/2 * fradius), center.getY() + (1/2 * fradius))
    mouthp2 = Point(center.getX() + (1/2 * fradius), center.getY() + (1/2 * fradius))
    mouth = Line(mouthp1, mouthp2)
    mouth.setWidth(5)
    mouth.draw(win)

    end = Text(Point(width / 2, 40), "Click again to exit")
    end.setSize(20)
    end.draw(win)
    win.getMouse()
    win.close()


main()
