# U03_EX01_VandSA_Sphere.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 24 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 01
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#  This program takes in the radius of a hypothetical sphere, and will give the
# surface area and volume of that sphere.
#
#
# Algorithm (pseudocode)
# 1. import math library
# 2. Print introduction
# 3. Ask user for radius
# 4. calculate volume with 4/3 * pi * (r ** 3)
# 5. calculate the surface area with 4 * pi * (r ** 2)
# 6. print out the results in a sentence

import math


def main():
    print("\nThis program takes in the radius of a sphere as input, \nand will return the volume and surface area",
          "of that sphere.\n")

    radius = float(input("Enter the radius of the sphere: "))

    volume = (4/3) * math.pi * (radius ** 3)
    surfaceA = 4 * math.pi * (radius ** 2)

    print("\nA sphere with a radius of", radius, "has a volume of", round(volume, 2), "and a surface area of",
          round(surfaceA, 2))


main()
