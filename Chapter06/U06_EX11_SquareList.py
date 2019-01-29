# U06_EX11_SquareList.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 23 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 11
#     Source: Python Programming
#    Chapter: 06
#
# Program Description
#  This program will allow the user to create a list,
# and the program will use a function to square each term
# and return them to the the user.
#
#
# Algorithm (pseudocode)
"""
- print introduction

- get user input of length of list
- set the list to have nothing in it but has the length
of what the user put in

- start a for loop using the list with i
    - set i equal to user input

- print output with original list
- use squareEach function on list
- print output with the list

"""


def squareEach(numlist):
    """
    - begin a loop for i in the length of the list
        - set list[i] equal to itself squared and rounded to the second decimal place
    """

    for i in range(len(numlist)):
        numlist[i] = round(numlist[i] ** 2, 5)


def main():
    print("\nThis program will allow the user to create a list," +
          "\nand the program will use a function to square each term" +
          "\nand return them to the the user.\n")

    numlist = int(input("length of list: ")) * [None]

    for i in range(len(numlist)):
        numlist[i] = float(
            input(
                "\nEnter a number in entree #{0} of the list: ".format(i + 1)
                 ))

    print("\nfor each term in the list {0},".format(numlist,), end=" ")
    squareEach(numlist)
    print("squared is {0}.".format(numlist))


if __name__ == '__main__':
    main()
