# U07_EX11_LeapYear.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 18 Feb 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 11
#     Source: Python Programming
#    Chapter: 07
#
# Program Description
#  This program will figure out if a year entered by the user is a leap year or not
# A year is a leap year if it divisible by 4, unless it is a century year that
# is not divisible by 400.
#
# Algorithm (pseudocode)
"""
- print introduction

- get year as input

- check if calcleap is true
    - tell use that the year is a leap year
    - if it is not tell user that the year is not a leap year
"""


def calcleap(year):
    """
    - this function will return true or false based on if the year is a leap year

    - first check if the year is divisible by 100, but also if it is divisble by 400 and return true if it is
    - also check if it divisble by 4, but not 100 and return true if it is
    - if both these fail the year is not a leap year and should return false
    """
    if year % 400 == 0 and year % 100 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


def main():
    print('\nThis program will figure out if a year entered by the user is a leap year or not'
          '\nA year is a leap year if it divisible by 4, unless it is a century year that'
          '\nis not divisible by 400.\n')

    year = int(input("Enter the year to check if it is a leap year: "))

    if calcleap(year):
        print('\nThe year, {0}, is a leap year.'.format(year))
    else:
        print('\nThe year, {0}, is not a leap year.'.format(year))


if __name__ == '__main__':
    main()

"""
RESULTS:
========
calcleap(2012)   -->       1 |       1 | [ Pass ]
calcleap(2013)   -->       0 |       0 | [ Pass ]
calcleap(2019)   -->       0 |       0 | [ Pass ]
calcleap(2016)   -->       1 |       1 | [ Pass ]
calcleap(1600)   -->       1 |       1 | [ Pass ]
calcleap(1700)   -->       0 |       0 | [ Pass ]
calcleap(2000)   -->       1 |       1 | [ Pass ]
========
"""