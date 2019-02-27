# U07_EX13_ DayCalculator.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Feb 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 13
#     Source: Python Programming
#    Chapter: 07
#
# Program Description
#  This program will accept a date in mm/dd/yyyy format
# and check if it is valid. It will also return the corresponding
# number of days out of 365 days in the year.
#
#
# Algorithm (pseudocode)
"""
- import calcleap
- import checkdate from ex12

- print introduction

- get date as input

- if checkdate(date) is true, continue on, but if it is false, print that the date is invalid

- send output of day out of 365 or 366 days (using function) as well as the original date
"""

from Chapter07.U07_EX11_LeapYear import calcleap
from Chapter07.U07_EX12_MDYChecker import checkdate


def getdaynum(date):
    """
    - make sure date is valid, if it is not return message saying so
        - separate the date into month, day, and year variables

        - The first equation to find the day number withstands all conditions,
        so set variable to return equal to it (equation is 31(m - 1) + d)

        - if the day is after February, subtract the second equation from variable to return
        (equation is (4m + 23)//10)

            - if the year is a leapyear and after February (but this has already been checked, so this
            if statement should be nested in the last one) add one to return variable

        - return (variable used in previous equations)
    """
    if checkdate(date):
        date = date.split("/")
        m, d, y = int(date[0]), int(date[1]), int(date[2])

        daynum = 31 * (m - 1) + d
        if m > 2:
            daynum -= (4 * m + 23)//10
            if calcleap(y):
                daynum += 1

        return daynum
    else:
        return "not valid date"


def main():
    print('\nThis program will accept a date in mm/dd/yyyy format'
          '\nand check if it is valid. It will also return the corresponding'
          '\nnumber of days out of 365 days in the year.')

    date = input("\nEnter date in mm/dd/yyyy format: ")

    if checkdate(date):
        print('\nthe date, {0}, is day {1} of the year'.format(date, getdaynum(date)))
    else:
        print("\nThe date, {0}, is not a valid date".format(date))


if __name__ == '__main__':
    main()

"""
RESULTS:
========
getdaynum("1/31/2019")    -->               31 |               31 | [ Pass ]
getdaynum("1/32/2019")    -->   not valid date |   not valid date | [ Pass ]
getdaynum("2/29/2020")    -->               60 |               60 | [ Pass ]
getdaynum("2/29/2019")    -->   not valid date |   not valid date | [ Pass ]
getdaynum("12/31/2019")   -->              365 |              365 | [ Pass ]
getdaynum("12/31/2020")   -->              366 |              366 | [ Pass ]
getdaynum("06/05/2019")   -->              156 |              156 | [ Pass ]
getdaynum("03/16/2019")   -->               75 |               75 | [ Pass ]
========
"""