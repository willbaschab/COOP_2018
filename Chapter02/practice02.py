# practice02.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 01 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 12
#     Source: Python Programming
#    Chapter: 02
#
# Program Description
#  This program is an interactive calculator that accepts mathematical expressions
#
#
#
# Algorithm (pseudocode)
# Print introduction
# Begin while loop for true
#   get user input as a string and check for condition exit
#   check for "exit" and quit loop if true
#   expr is equal to evaluating expression
#   print evaluated expression
#


def main():
    print("\nThis program is an interactive calculator that accepts mathematical expressions.")

    while True:
        expression = str(input("\nEnter expression to calculate (type exit to exit): "))

        if expression == "exit":
            break

        expr = eval(expression)

        print()
        print(expression, "=", expr)

main()
