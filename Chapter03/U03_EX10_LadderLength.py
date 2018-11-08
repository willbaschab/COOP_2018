# U03_EX10_LadderLength.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 10
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#  This program determines the length of a ladder leaning against a wall given the
# height of the ladder, and the angle of the ladder (between 1 and 90). The length is calculated
# based on teh height divided by the sin of the angle of the ladder and the ground.
#
# Algorithm (pseudocode)
# 1. import math
# 2. print introduction
# 3. get user input for height and angle
# 4. convert angle to radians (radians = pi/180 * degrees)
# 5. use height over sin(angle) to find length
# 6. print length in complete sentence
#
import math


def main():
    print("\nThis program determines the length of a ladder leaning against a wall given the",
          "\nheight of the ladder, and the angle of the ladder (between 1 and 90).",
          "\nThe length is calculated based on teh height",
          "\ndivided by the sin of the angle of the ladder and the ground.")

    height = float(input("\nWhat is the height of the ladder against the wall: "))
    degrees = float(input("\nWhat is the angle between the ladder and the ground: "))

    angle = math.pi/180 * degrees

    length = height/math.sin(angle)

    print("\nThe length of a ladder at a", degrees, "degree angle with the ground and a",
          "\nheight of", height, "is", round(length, 2))


main()
