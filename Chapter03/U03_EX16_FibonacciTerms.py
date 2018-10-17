# U03_EX16_FibonacciTerms.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 16
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#  Determines the nth term in the Fibonacci sequence with n being given by user input.
#
#
#
# Algorithm (pseudocode)
# 1. print introduction
# 2. get term from user input
# 3. initialize total, a, and b at 0
# 4. for i in range of term
#   5. If we are at the start of the fibonacci sequence, (a and b being 0) set the total to 1
#       6. a is set to b
#       7. b is set to total
#   8. if at any other term in fibonacci sequence, total is equal to b + a
#       9. a is set to b
#       10. b = total
# 11. Check if term is equal to 1, 2, 3, or anything else and say that the 1st, 2nd, 3rd, or xth term in the
# sequence is equal to total.


def main():

    print("\nThis program determines the nth term in the Fibonacci sequence",
          "\nwith n being given by user input.")

    term = int(input("\nEnter term in the fibonacci sequence to see: "))

    total, a, b = 0, 0, 0

    for i in range(term):
        if a == 0 and b == 0:
            total = 1
            a = b
            b = total
        else:
            total = b + a
            a = b
            b = total

    if term == 1:
        print("\nthe 1st term in the fibonacci sequence is", total)
    elif term == 2:
        print("\nthe 2nd term in the fibonacci sequence is", total)
    elif term == 3:
        print("\nthe 3rd term in the fibonacci sequence is", total)
    else:
        print("\nthe", str(term) + "th term in the fibonacci sequence is", total)


main()
