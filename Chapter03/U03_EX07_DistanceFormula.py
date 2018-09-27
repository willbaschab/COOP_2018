# U03_EX07_DistanceFormula.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 07
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#  This program accepts the x and y values of two points as input
# and calculates the distance between those points as output.
#
#
# Algorithm (pseudocode)
# 1. import math library
# 2. print introduction
# 3. get point one x and y values from user input
# 4. get point two x and y values from user input
# 5. calculate distance formula with the two points
# 6. print distance value and points in a sentence
import math


def main():
    print("\nThis program accepts the x and y values of two points as input",
          "\nand calculates the distance between those points as output.")

    x1 = float(input("\nWhat is the x value of the first point: "))
    y1 = float(input("\nWhat is the y value of the first point: "))
    x2 = float(input("\nWhat is the x value of the second point: "))
    y2 = float(input("\nWhat is the y value of the second point: "))

    distance = math.sqrt( ((x2 - x1) ** 2) + ((y2 - y1) ** 2) )

    print("\nThe distance between points (" + str(x1) + ",", str(y1) + ") and ("
          + str(x2) + ",", str(y2) + ") is", round(distance, 2))


main()
