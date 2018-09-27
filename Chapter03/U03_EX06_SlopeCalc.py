# U03_EX06_SlopeCalc.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 06
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#  This program calculates the slope of a line
# with the x and y values of two points in the line inputted by the user
#
#
# Algorithm (pseudocode)
# 1. print introduction
# 2. get point one x and y values from user input
# 3. get point two x and y values from user input
# 4. calculate slope formula with the two points
# 5. print slope and points in a sentence


def main():
    print("\nThis program calculates the slope of a line",
          "\nwith the x and y values of two points in the line inputted below.",
          "\nIt cannot calculate the slope of a vertical line.")

    x1 = float(input("\nWhat is the x value of the first point: "))
    y1 = float(input("\nWhat is the y value of the first point: "))
    x2 = float(input("\nWhat is the x value of the second point: "))
    y2 = float(input("\nWhat is the y value of the second point: "))

    slope = (y2 - y1)/(x2 - x1)

    print("\nThe slope of a line with points (" + str(x1) + ",", str(y1) + ") and ("
          + str(x2) + ",", str(y2) + ") is", round(slope, 2))


main()
