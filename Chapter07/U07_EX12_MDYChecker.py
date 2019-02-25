# U07_EX12_MDYChecker.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 19 Feb 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 12
#     Source: Python Programming
#    Chapter: 07
#
# Program Description
#  This program will check if a specific date is valid.
# It will check if the month is below 12, if the day of
# the month is below the amount of days in the month, and
# if the year is a leap year.
#
# Algorithm (pseudocode)
"""
- import calcleap from ex 11

- print introduction

- get date as input

- if checkdate(date) returns True:
    - print that the date is correct
- if checkdate(date) is False:
    - print that the date is incorrect
"""
from Chapter07.U07_EX11_LeapYear import calcleap


def checkdate(date):
    """
    - set date equal to the date split into the three different numbers

    - set month, day, and year equal to date[0], date[1], and date[2] respectively

    - check if calcleap(year) is a leap year:
        - if it is then the list of days only changes
        for February from 28 ro 29 (the rest stay the same)

    - if it is not:
        - still define a list with 12 entrees, each
        entree representing the max days in each month (feb having 28)

    - attempt to do the following:
        - check if the day is less than the specific max value of the month in the list
            - if it is then return true, else return false
    - if there is an error where the month is greater than the list index (the month doesn't exist), return false

    """
    date = date.split('/')
    month, day, year = int(date[0]), int(date[1]), int(date[2])

    if calcleap(year):
        maxdays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        maxdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    try:
        if day <= maxdays[month - 1]:
            return True
        else:
            return False
    except IndexError:
        return False


def main():
    print('\nThis program will check if a specific date is valid.' 
          '\nIt will check if the month is below 12, if the day of'
          '\nthe month is below the amount of days in the month, and'
          '\nif the year is a leap year.')

    date = input("\nEnter the date in format mm/dd/yyyy: ")

    if checkdate(date):
        print("\nThe date, {0}, is a valid date".format(date))
    else:
        print("\nThe date, {0}, is not a valid date".format(date))


if __name__ == '__main__':
    main()

"""
RESULTS:
========
checkdate("2/29/2012")    -->       1 |       1 | [ Pass ]
checkdate("2/29/2013")    -->       0 |       0 | [ Pass ]
checkdate("2/28/2013")    -->       1 |       1 | [ Pass ]
checkdate("12/31/2019")   -->       1 |       1 | [ Pass ]
checkdate("12/32/2019")   -->       0 |       0 | [ Pass ]
checkdate("18/3/2009")    -->       0 |       0 | [ Pass ]
checkdate("6/3/2017")     -->       1 |       1 | [ Pass ]
========
"""
