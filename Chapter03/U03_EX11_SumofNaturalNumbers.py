# U03_EX11_SumofNaturalNumbers.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 11
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#  This program determines the sum of the first n natural numbers
# with n being inputted by the user.
#
#
# Algorithm (pseudocode)
# 1. print introduction
# 2. get amount of terms from user input
# 3. initialize total at 0
# 4. begin for loop in range of terms
#   5. total = total + (i + 1)
# 6. print total in complete sentence
#


def main():

    print("\nThis program determines the sum of the first n natural numbers",
          "\nwith n being inputted by the user.")

    terms = int(input("\nEnter the number of first natural numbers to sum: "))

    total = 0

    for i in range(terms):
        total = total + (i + 1)

    print("\nThe total of the first", terms, "natural numbers is", str(total) + ".")


main()
