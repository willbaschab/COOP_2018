# U02_EX05_ConvertCtoF_Table.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 28 Aug 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 5
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#  This program prints a table of Celsius temperatures converted
# to Fahrenheit from 0 degrees Celsius to 100 degrees Celsius.
#
#
# Algorithm (pseudocode)
# 1. print introduction
# 2. print out table header
# 3. Create a 'for' loop with a range from 0 to 101 with index <i>
#   4. Check if <i> is greater than 10 and is divisible by 10
#       5. Set <celsius> to be equal to i (this means that celsius will print from 0 to 100)
#       6. Assign <fahrenheit> to: 9/5 * celsius + 32
#       7. print out table in fashion: <celsius> | <fahrenheit>
#                                      -------------------------


def main():
    print("\nThis program prints a table of degrees in Celsius converted to Fahrenheit every "
            + "\n10 degrees from 0 to 100 degrees Celsius.")
    print("\nDegrees Celsius | Degrees Fahrenheit")
    print("------------------------------------")

    for i in range(101):
        if i % 10 == 0:
            celsius = i
            fahrenheit = 9/5 * celsius + 32;

            print("       ", celsius, " | ", fahrenheit)
            print("------------------------------------")


main()
