# U02_EX08_PeriodicCompounding.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 02 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 8
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
# 3. Assign <apr>, <periods> to user input
# 4. Assign <years> to 10
# 5. begin 'for' loop with <years> * <periods>
#   6. Assign <principal> to <principal> times (1 + apr)
# 7. Print out <principal>


def main():
    print("\nThis program calculates the future value of an investment over 10 years."
          + "\nYou can enter your initial investment you "
          + "\nare investing, and the yearly rate and number of times that rate is compounded each year.\n")

    principal = eval(input("Enter initial principal amount: "))
    initial = principal
    apr = eval(input("\nEnter the annual interest rate as a decimal: "))
    years = 10
    periods = eval(input("\nEnter number of periods per year the value will be compounded: "))

    for i in range(years * periods):
        principal = principal * (1 + apr)

    print("\nAn initial investment of $" + str(initial), "over 10 years with an annual interest rate of",
          str(int(apr*100))+ "%",  "compounded", periods, "times a year will return $" + str(principal) + ".")


main()
