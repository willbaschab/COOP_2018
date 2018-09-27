# U03_EX15_ApproximatePI.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 26 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 15
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#   This program will approximate the value of PI by using user input
# to add and subtract that amount of terms from a series. It will also
# see how accurate the input is by telling the difference between the output
# and PI defined by Python.
#
# Algorithm (pseudocode)
# 1. import math
# 2. Print introduction
# 3. get amount of terms from user input
# 4. initialize switch and total as variables with 1 and 0
# 5. begin 'for' loop with i in range of twice the amount of terms
#   6. check if i is not 0 and and odd
#       7. check if switch variable is 1
#           8. set total to total + 4/i
#           9. set switch to 2
#       10. if step 7 is false, check if switch variable is 2
#           11. set total to total - 4/i
#           12. set switch to 1
# 13. print total and deviation from PI in sentence
#
import math


def main():
    print("\nThis program will approximate the value of PI by using user input",
          "\nto add and subtract that amount of terms from a series. It will also",
          "\nsee how accurate the input is by telling the difference between the output",
          "\nand PI defined by Python.")

    amount = int(input("\nEnter amount of numbers in series to add and subtract: "))
    switch = 1
    total = 0

    for i in range(amount*2):
        if i != 0 and i % 2 != 0:
            if switch == 1:
                total = total + 4/i
                switch = 2
            elif switch == 2:
                total = total - 4/i
                switch = 1

    print("\nWith", amount, "terms in the equation, your total,\n" + str(total) + ", deviates",
          abs(math.pi - total), "away from PI.")


main()
