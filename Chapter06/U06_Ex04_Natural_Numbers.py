# U06_Ex04_Natural_Numbers.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 13 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 04
#     Source: Python Programming
#    Chapter: 05
#
# Program Description
#  This program uses two functions to
# return the sum of the first n natural numbers
# and sum of the cubes of the first n natural numbers
# with n being user input
#
# Algorithm (pseudocode)
"""
- def other two functions

- def main()
    - print introduction

    - Ask user for how many of the first natural numbers to sum

    - print out the results in a sentence using the two functions
"""


def sumN(n):
    """
    - returns the sum of the first n natural numbers

    - set accumulator to 0

    - start a for loop for i in range(n)
        - accumulator += (i + 1)

    - return accumulator
    """

    nsum = 0

    for i in range(n):
        nsum += (i + 1)

    return nsum


def sumNcubes(n):
    """
    - returns the sum of the cubes of the first n natural numbers

    - set accumulator to 0

    - start a for loop for i in range(n)
        - accumulator += (i + 1) ** 3

    - return accumulator
    """

    cube_sum = 0

    for i in range(n):
        cube_sum += (i + 1) ** 3

    return cube_sum


def main():
    print("\nThis program uses two functions to\n" +
          "return the sum of the first n natural numbers\n" +
          "and sum of the cubes of the first n natural numbers\n" +
          "with n being user input\n")

    n = int(input("Enter how many of the first natural numbers to sum: "))

    print("\nthe first {0} natural numbers have\n".format(n) +
          "a sum of {0} and their cubes sum to {1}.".format(sumN(n), sumNcubes(n)))

main()
