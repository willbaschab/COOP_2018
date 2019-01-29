# U06_EX13_ToNumbers.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 13
#     Source: Python Programming
#    Chapter: 06
#
# Program Description
#  This program allows the user
# to enter numbers into a list
# where the numbers are strings.
# The program will return the
# list as numbers instead of
# strings.
#
# Algorithm (pseudocode)
"""
- print introduction

- get user input of length of list
- set the list to have nothing in it but has the length
of what the user put in

- start a for loop using the list with i
    - set i equal to user input (as string)

- print output with original list
- use toNumbers function on list
- print output with the new list

"""


def toNumbers(numlist):
    """
    - begin a loop for i in the length of the list
        - set list[i] equal to itself as a float
    """

    for i in range(len(numlist)):
        numlist[i] = float(numlist[i])


def main():
    print("\n This program allows the user" +
          "\nto enter numbers into a list" +
          "\nwhere the numbers are strings." +
          "\nThe program will return the" +
          "\nlist as numbers instead of" +
          "\nstrings.\n")

    numlist = int(input("length of list: ")) * [None]

    for i in range(len(numlist)):
        numlist[i] = str(
            input(
                "\nEnter a number in entree #{0} of the list: ".format(i + 1)
                 ))

    print("\nfor each string in the list {0},".format(numlist,), end=" ")
    toNumbers(numlist)
    print("is numbers: {0}.".format(numlist))


if __name__ == '__main__':
    main()
