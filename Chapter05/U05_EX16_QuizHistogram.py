# U05_EX16_QuizHistogram.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 05 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 16
#     Source: Python Programming
#    Chapter: 05
#
# Program Description
#  This program will draw a quiz score histogram. The program
# will read data from a file where each line of the file contains
# a number in the range 0 - 10. The program will return the number
# of occurrences of each score as a bar in a vertical bar graph.
#
# Algorithm (pseudocode)
"""
- import everything from graphics
- print introduction

- ask for file name as input and save into <name>

- set <file> to open(name, "r")

- set <numlist> to a list with eleven 0s

- set string to file.read()
- close file

- start for loop for i in range of 11:
    - numlist[i] = string.count("{0}\n".format(i))

"""
from graphics import *


def main():
    print("\nThis program will draw a quiz score histogram. The program\n" +
          "will read data from a file where each line of the file contains\n" +
          "a number in the range 0 - 10. The program will return the number\n" +
          "of occurrences of each score as a bar in a vertical bar graph.\n")

    filename = input('Enter name of file as well as .txt extension on end: ')
    file = open(filename, "r")

    numlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    string = file.read()
    file.close()

    for i in range(11):
        numlist[i] = string.count("{0}\n".format(i))

    draw_graph(numlist)


def largestnumber(numlist):
    """
    - this function returns the largest number from a list of numbers

    - accumulator starts at 0

    - for loop for i in list
        - if accumulator is less than i:
            - accumulator gets value of i

    - return accumulator
    """
    num = 0
    for i in numlist:
        if num < i:
            num = i
    return num


def draw_graph(numlist):
    """
        - This function contains and carries out the graphical component
        of the program. It creates a new widow with a height based of
        the largest number in the list.

        - set width to 34 * 20
        - set height to (largestnumber(numlist) + 10) * 20

        - create new window with title "Quiz Score Histogram", and with a width of <width> and a height of <height>
        - set window coords to (0, 0, 34, 10 + largestnumber(numlist))

        - draw "Quiz Score Histogram:" at (17, largestnumber(numlist) +7)

        - for i in range(11):
            - textnumber = Text(Point(i * 3 + 2, 4), "{0}".format(i))
            - textnumber.draw(win)

            - score = Rectangle(Point(i * 3 + 1, 5),
                                Point(i * 3 + 3, 5 + numlist[i]))
            - score.setFill("green")
            - score.draw(win)

        - exitbox = Text(Point(17, 1), "Click to exit")
        - exitbox.draw(win)
        - win.getMouse()
        - win.close()
    """
    width = 34 * 20
    height = (largestnumber(numlist) + 10) * 20

    win = GraphWin("Quiz Score Histogram", width, height)
    win.setCoords(0, 0, 34, 10 + largestnumber(numlist))

    Text(Point(17, largestnumber(numlist) + 7), "Quiz Score Histogram:").draw(win)

    for i in range(11):
        textnumber = Text(Point(i * 3 + 2, 4), "{0}".format(i))
        textnumber.draw(win)

        score = Rectangle(Point(i * 3 + 1, 5),
                          Point(i * 3 + 3, 5 + numlist[i]))
        score.setFill("green")
        score.draw(win)

    exitbox = Text(Point(17, 1), "Click to exit")
    exitbox.draw(win)
    win.getMouse()
    win.close()


main()
