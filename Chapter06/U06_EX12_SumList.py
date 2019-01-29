# U06_EX12_SumList.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 12
#     Source: Python Programming
#    Chapter: 06
#
# Program Description
#  This program allows the user
# to enter values in a list.
# The program will return the sum
# of all the numbers in the list.
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

- print output with original list and sumList(list)
"""


def sumList(numlist):
    """
    This function returns the sum of each number in a list

    - set accumulator to 0 so it can be added to later

    - start a loop for each term in list
        - add the term to accumulator

    - return the accumulator
    """
    acc = 0

    for i in numlist:
        acc += i

    return acc


def main():
    print("\nThis program allows the user" +
          "\nto enter values in a list." +
          "\nThe program will return the sum " +
          "\nof all the numbers in the list.\n")

    numlist = int(input("length of list: ")) * [None]

    for i in range(len(numlist)):
        numlist[i] = float(
            input(
                "\nEnter a number in entree #{0} of the list: ".format(i + 1)
                 ))

    print("\nThe sum of all numbers in {0} is {1}.".format(numlist, sumList(numlist)))


if __name__ == '__main__':
    main()
