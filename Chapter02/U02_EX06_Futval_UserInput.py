# U02_EX06_Futval_UserInput.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 02 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 6
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#  a program that takes user input for a future investment and calculates
# over user inputted years what the investment will be
#
#
# Algorithm (pseudocode)
# 1. Print introduction
# 2. Assign <principal>, <initial> to user input
# 3. Assign <apr> to user input
# 4. Assign <years> to user input
# 5. begin 'for' loop from 0 to <years>
#   6. Assign <principal> to <principal> times (1 + apr)
# 7. Print out <principal>


def main():
    print("\nThis program calculates the future value of an investment."
          + "\nYou can enter your initial investment, how many years you "
          + "\nare investing, and the annual interest rate below.\n")

    principal = eval(input("Enter initial principal amount: "))
    initial = principal
    apr = eval(input("\nEnter the annual interest rate as a decimal: "))
    years = eval(input("\nEnter the amount of years investing: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("\nAn initial investment of $" + str(initial), "over", years, "years with an annual interest rate of", apr,
          "will return $" + str(principal) + ".")


main()
