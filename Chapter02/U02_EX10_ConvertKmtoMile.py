# U02_EX10_ConvertKmtoMile.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 28 Aug 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 10
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#  A program that converts a user's input of kilometers into a distance in miles.
#
#
#
# Algorithm (pseudocode)
# 1. Print introduction to program
# 2. Ask user for a distance in kilometers
# 3. Assign user input to <km> (kilometers)
# 4. Assign <mi> (miles) = km/1.609 (1.609 is how many kilometers in a mile)
# 5. print mi


def main():
    print("\nThis program converts a distance in kilometers into miles."
          + "\nYou can choose what distance you would like to convert by entering it below.")

    km = eval(input("\nEnter a number of kilometers: "))
    mi = km/1.609
    print()
    print(km, "kilometers is equal to", mi, "miles.")


main()

