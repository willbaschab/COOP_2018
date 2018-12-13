# U05_EX12_FutVal_NiceTable.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 12 Dec 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 12
#     Source: Python Programming
#    Chapter: 05
#
# Program Description
#  a program that takes user input for a future investment and calculates
# over user inputted years what the investment will be and formats it
# into a table for every year
#
#
# Algorithm (pseudocode)
"""
 - Print introduction
 - Assign <principal>, <initial> to user input
 - Assign <apr> to user input
 - Assign <years> to user input

 - print title of table so that each title is roughly centered over the values below it
 - print dashes for the amount of space the title area takes up
 - begin 'for' loop from 0 to <years>
    - print each year with 4 spaces after it and two behind, a $ sign, and the value with
    1 space in front of it and a precision of 6
    - Assign <principal> to <principal> times (1 + apr)
"""


def main():
    print("\na program that takes user input for a future investment and calculates" +
          "\nover user inputted years what the investment will be and formats it" +
          "\ninto a table for every year.")

    principal = float(input("Enter initial principal amount: "))
    apr = eval(input("\nEnter the annual interest rate as a decimal: "))
    years = eval(input("\nEnter the amount of years investing: "))

    print("\n{0:^4}     {1:^5}".format("Year", "Value"))
    print("-" * 14)
    for i in range(years):
        print("  {0:<4}${1:>1.6}".format(i, principal))
        principal = principal * (1 + apr)


main()
