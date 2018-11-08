# U03_EX09_TriangleSideArea.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 27 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 09
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#  Determines the area of a triangle given the side lengths inputted by the user.
#
#
#
# Algorithm (pseudocode)
# 1. import math
# 2. print introduction
# 3. get a, b, and c from user input
# 4. assign s to (a + b + c)/2
# 5. calculate area using formula: (sqrt(s * (s - a) * (s - b) * (s - c))
# 6. print area in complete sentence
#
import math


def main():
    print("This program determines the area of a triangle",
          "\ngiven the side lengths inputted by the user.")

    a = float(input("\nEnter first side length of triangle: "))
    b = float(input("\nEnter second side length of triangle: "))
    c = float(input("\nEnter third side length of triangle: "))

    s = (a + b + c)/2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("\nThe area of a triangle with side lengths", str(a) + ",", str(b) + ",", c, "is", area)


main()

