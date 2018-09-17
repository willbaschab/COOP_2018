# U02_EX01_ConvertCtoF_Introduction.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 28 Aug 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 1
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#  This program converts temperature from Celsius to Fahrenheit.
#
# Algorithm (pseudocode)
# 1. Explain that program can convert a temperature of choice from Celsius to Fahrenheit
# 2. Ask user for choice Celsius temperature and store value in <celsius>
# 3. Assign <fahrenheit> to: 9/5 * celsius + 32
# 4. print out fahrenheit
#


def main():
    #Introduction
    print("\nHaving trouble converting Celsius to Fahrenheit on your own?\nNo Worry!",
          "Just enter a Celsius temperature below to see it in Fahrenheit!\n")

    #Input and calculation
    celsius = eval(input("Enter Celsius temperature: "))
    fahrenheit = 9/5 * celsius + 32;

    #Output
    #print("{:>5.2} degrees Celsius is equal to {:>5.2} degrees Fahrenheit.".format(celsius,fahrenheit))
    print(celsius, "degrees Celsius is equal to", fahrenheit, "degrees Fahrenheit.")


main()
