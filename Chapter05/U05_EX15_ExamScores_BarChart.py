# U05_EX15_ExamScores_BarChart.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 19 Dec 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 15
#     Source: Python Programming
#    Chapter: 05
#
# Program Description
#  This program will take a text file as input with the number of students in the first
# line and the last name of the student followed by their score on the subsequent lines.
# It will return a graphical bar chart of the student's names and their scores out of 100.
#
#
# Algorithm (pseudocode)
"""
- import everything from graphics
- print introduction

- ask for file name as input and save into <name>

- set <file> to open(name + ".txt", "r")

- set <student_count> to int(file.readline(1)[:-1])
- set variables <students> and <grades> to empty lists

- set lines to file.readlines()
- close file

- begin for loop for line in file.readline()
    - students.append(line.split()[1])
    - grades.append(line.split()[2])

- draw graph of scores
"""
from graphics import *


def main():
    print("\nThis program will take a text file as input with the number of students in the first" +
          "\nline and the last name of the student followed by their score on the subsequent lines." +
          "\nIt will return a graphical bar chart of the student's names and their scores out of 100.\n")

    filename = input("Enter the name of the file to open with exam scores: ")
    file = open(filename, "r")

    studentcount = int(file.readline(1))
    students, scores = [], []

    lines = file.readlines()
    file.close()

    for line in lines[1:]:
        students.append(line.split()[0])
        scores.append(int(line.split()[1]))

    draw_graph(studentcount, students, scores)


def draw_graph(studentcount, students, scores):
    """
        - This function contains and carries out the graphical component
        of the program. It creates a new widow with a height based of
        the amount of students in the list.

        - set width to 480
        - set height to max height coordinate by a multiplier of 20

        - create new window with title "Exam Scores Bar Graph", and with a width of <width> and a height of <height>
        - set window coords to (0, studentcount * 3 + 5, 24, 0)

        - draw "Names:" at (6,1) and "Scores:" at (18, 1)

        - for i in range(studentcount):
            - name = Text(Point(6, i * 3.0 + 3.0), "{0}:".format(students[i]))
            - name.draw(win)

            - score = Rectangle(Point(12, i * 3 + 2), Point(scores[i]/10 + 12, i * 3 + 4))
            - score.setFill("green")
            - score.draw(win)

        - exitbox = Text(Point(6, studentcount * 3 + 3), "Click to exit")
        - exitbox.draw(win)
        - win.getMouse()
        - win.close()
    """

    width = 480
    height = (studentcount * 3 + 5) * 20.0
    win = GraphWin("Exam Scores Bar Graph", width, height)
    win.setCoords(0.0, studentcount * 3.0 + 5.0, 24, 0)

    Text(Point(6, 1), "Names:").draw(win)
    Text(Point(18, 1), "Scores:").draw(win)

    for i in range(studentcount):
        name = Text(Point(6, i * 3.0 + 3.0), "{0}:".format(students[i]))
        name.draw(win)

        score = Rectangle(Point(12, i * 3 + 2), Point(scores[i]/10 + 12, i * 3 + 4))
        score.setFill("green")
        score.draw(win)

    exitbox = Text(Point(6, studentcount * 3 + 3), "Click to exit")
    exitbox.draw(win)
    win.getMouse()
    win.close()


main()
