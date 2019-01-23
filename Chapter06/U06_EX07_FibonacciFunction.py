# U06_EX07_FibonacciFunction.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 22 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 07
#     Source: Python Programming
#    Chapter: 06
#
# Program Description
#  Determines the nth term in the Fibonacci sequence with n being given by user input
# using a function to determine the term.
#
# Algorithm (pseudocode)
# 1. print introduction
# 2. get term from user input
# 3. use function fibonacci to return number to total
# 3. Check if term is equal to 1, 2, 3, or anything else and say that the 1st, 2nd, 3rd, or xth term in the
# sequence is equal to total.


def fibonacci(term):
    """
    - set values total, a, b to 0

    - If we are at the start of the fibonacci sequence, (a and b being 0) set the total to 1
        - a is set to b
        - b is set to total

    - if at any other term in fibonacci sequence, total is equal to b + a
        - a is set to b
        - b = total

    - return the total
    """
    total, a, b = 0, 0, 0

    for i in range(term - 1):
        if a == 0 and b == 0:
            total = 1
            a = b
            b = total
        else:
            total = b + a
            a = b
            b = total

    return total


def main():

    print("\nThis program determines the nth term in the Fibonacci sequence",
          "\nwith n being given by user input using a function to determine the term.")

    term = int(input("\nEnter term in the fibonacci sequence to see: "))

    total = fibonacci(term)

    if term == 1:
        print("\nthe 1st term in the fibonacci sequence is", total)
    elif term == 2:
        print("\nthe 2nd term in the fibonacci sequence is", total)
    elif term == 3:
        print("\nthe 3rd term in the fibonacci sequence is", total)
    else:
        print("\nthe", str(term) + "th term in the fibonacci sequence is", total)


main()
