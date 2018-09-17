# U02_S00_ConvertCtoF.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Aug 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: n/a
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#  This program converts temperature from Celsius to Fahrenheit
#
#
#
# Algorithm (pseudocode)
#   Print program introduction
#   Get degrees Celsius from user and assign to celsius
#   Calculate degrees Fahrenheit using 9/5 * celsius + 32 and assign to fahrenheit
#   print degrees Fahrenheit


def main():
    #Introduction
    print("\nHaving trouble converting Celsius to Fahrenheit on your own?\nNo Worry!",
          "Just enter a Celsius temperature below to see it in Fahrenheit!\n")

    #Input and calculation
    celsius = eval(input("Enter Celsius temperature: "))
    fahrenheit = 9/5 * celsius + 32;

    #Output
    print(celsius, "degrees Celsius is equal to", fahrenheit, "degrees Fahrenheit.")

main()
