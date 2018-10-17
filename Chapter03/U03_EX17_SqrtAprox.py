# U03_EX17_SqrtAprox.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 17
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#  This program approximates the square root of a number with the number as input,
# and the number of tries to improve the guessed square root as input. It uses Newtons method of
# adding the guessed value to the number to be squared divided by the guess and dividing all of this by two.
#
# Algorithm (pseudocode)
# 1. import math
# 2. print introduction
# 3. get number to sqrt from user
# 4. get number of times to guess from user
# 4. set ans to math.sqrt(num)
# 5. set guess to num/2
# 5. start for loop in the range of <tries>
#   6. guess = (guess + (num/guess))/2
# 7. print out guess, deviation from answer, and amount
import math


def main():
    print("\nThis program approximates the square root of a number with the number as input",
          "\nand the number of tries to improve the guessed square root as input. It uses Newton's method of",
          "\nadding the guessed value to the number to be squared divided by the guess and dividing all of this by two.")

    number = float(input("\nEnter the number to find the approximate square root of: "))
    tries = int(input("\nEnter amount of times to improve guess on square root: "))
    ans = math.sqrt(number)
    guess = number/2

    for i in range(tries):
        guess = (guess + (number/guess))/2

    print("\nThe approximation of the square root of", number, "is", str(round(guess, 4)) + ", which",
          "\ndeviates", abs(ans - guess), "from the actual square root,", ans,
          "\nIt took", tries, "tries to find this approximation.")


main()

