# U02_EX09_ConvertFtoC.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 28 Aug 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 9
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#  A program that takes user input in the form of degrees Fahrenheit
# and prints out the equivalent temperature in degrees Celsius
#
#
# Algorithm (pseudocode)
# 1. Print Introduction
# 2. Ask user for choice Fahrenheit temperature and store value in <fahrenheit>
# 3. Assign <celsius> to: 5/9 * (fahrenheit - 32)
# 4. print out celsius


def main():
    print("\nThis program converts degrees in Fahrenheit to degrees in Celsius.\nEnter a Fahrenheit temperature below!")
    fahrenheit = eval(input("\nEnter Fahrenheit temperature: "))
    celsius = 5/9 * (fahrenheit - 32)

    print(fahrenheit, "degrees Fahrenheit is equal to", celsius, "degrees Celsius.")


main()
