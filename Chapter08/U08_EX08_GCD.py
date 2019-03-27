# U08_EX08_GCD.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 26 Mar 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 08
#     Source: Python Programming
#    Chapter: 08
#
# Program Description
#  This program takes two integers as input and finds the greatest common divisor of both integers
# using Euclid's algorithm explained below.
#
#  Staring with the entered values, m and n the formula n, m, = m, n%m until m equals 0. the
# resulting value of n is the greatest common divisor of the two integers.
#
# Algorithm (pseudocode)
"""
- print introduction

- get both numbers as input

- print output of GCD of both numbers in formatted output
"""


def gcd(m, n):
    """
    This function returns the greatest common divisor of m and n

    ALG:
    - while m is not equal to 0:
        - using Euclid's algorithm: n, m = m, n%m

    - return n (result of Euclid's algorithm)
    """
    while m != 0:  # as long as m is not 0:
        n, m = m, n % m  # using Euclid's algorithm
    return n  # result of Euclid's algorithm


def main():
    # Introduction:
    print("\n\nThis program takes two integers as input and finds the greatest common divisor of both integers" +
          "\nusing Euclid's algorithm explained below." +
          "\n\nStaring with the entered values, m and n the formula n, m, = m, n%m until m equals 0." +
          "\nThe resulting value of n is the greatest common divisor of the two integers.")

    # Initial Input:
    m = int(input("\nEnter first integer to get GCD of with second number: "))
    n = int(input("\nEnter second integer to get GCD of with first number: "))

    # End Message:
    print("\nThe GCD of {0} and {1} is {2}".format(m, n, gcd(m, n)))


if __name__ == '__main__':
    main()

"""
RESULTS:
========
gcd(2, 2)     -->   2 |   2 | [ Pass ]
gcd(16, 56)   -->   8 |   8 | [ Pass ]
gcd(2, 8)     -->   2 |   2 | [ Pass ]
gcd(49, 56)   -->   7 |   7 | [ Pass ]
========
"""