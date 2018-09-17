# U02_EX04_ConvertCtoF_Loop.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 02 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 4
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#  This program will convert a user inputted temperature from Celsius to Fahrenheit.
# in a loop 5 times.
#
#
# Algorithm (pseudocode)
#  1. Print introduction
#  2. Begin 'for' loop set to go 5 times
#  3. Ask user for choice Celsius temperature and store value in <celsius>
#  4. Assign <fahrenheit> to: 9/5 * celsius + 32
#  5. print out fahrenheit


def main():

    print("\nHaving trouble converting Celsius to Fahrenheit on your own?\nNo Worry!",
          "Just enter a Celsius temperature below to see it in Fahrenheit!\n")

    for i in range(5):
        celsius = eval(input("Enter Celsius temperature: "))
        fahrenheit = 9/5 * celsius + 32;

        print(celsius, "degrees Celsius is equal to", fahrenheit, "degrees Fahrenheit.\n")


main()
