# U06_Ex03_Spheres.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 13 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 03
#     Source: Python Programming
#    Chapter: 06
#
# Program Description
#  This program takes in the radius of a hypothetical sphere, and will give the
# surface area and volume of that sphere using functions to return the answers.
#
#
#
# Algorithm (pseudocode)
"""
- import math library

- define other two functions

- def main():
    - Print introduction

    - Ask user for radius

    - print out the results in a sentence using the two functions

"""

from math import *


def sphereArea(radius):
    """
    - return equation for area with radius
    """
    return round(4 * pi * (radius ** 2), 2)


def sphereVolume(radius):
    """
    - return equation for volume with radius
    """
    return round((4/3) * pi * (radius ** 3), 2)


def main():
    print("\nThis program takes in the radius of\n" +
          "a hypothetical sphere, and will give the\n" +
          "surface area and volume of that sphere\n" +
          "using functions to return the answers.\n")

    radius = float(input("Enter the radius of the sphere: "))

    print("\nA sphere with a radius of", radius, "has a volume of", sphereVolume(radius), "and a surface area of",
          sphereArea(radius))


main()
