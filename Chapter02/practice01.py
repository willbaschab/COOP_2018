# practice01.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 01 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 11
#     Source: Python Programming
#    Chapter: 02
#
# Program Description
#   This program converts jewels to Calories.
#
# Algorithm (pseudocode)
#  print introduction
#  Loop until exit requested
#   get jewels as input from user (with 0 to quit)
#   Test for exit condition (break if true)
#   calculate jewels to Calories (1 jewel = 0.239 calories)
#       Calories = jewels * 0.239
#   Print calories in complete sentence.


def main():
    print('\nThis program converts jewels to Calories.')

    # Loop until exit requested
    while True:
        jewels = float(input("\nEnter amount of jewels to convert (0 to quit): "))

        # Test for exit condition (break if true)
        if jewels == 0:
            break

        Calories = jewels * 0.239

        print()
        print(jewels, "jewels is equal to", Calories, "Calories.")


main()
