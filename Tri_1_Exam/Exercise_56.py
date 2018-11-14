# Exercise_56.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 14 Nov 2018
#     IDE: PyCharm
#
# Assignment Info:
#   Trimester 1 Exam
#
# Program Description
#  This program will take 3 side lengths as input,
# and determine whether or not those side lengths can create a triangle
# by testing if any side is greater than the sum of the other two.
#
# Algorithm (pseudocode)
# - define is_triangle with arguments <a>, <b>, <c>
#   - if c > a + b or a > c + b or b > c + a
#       - return False
#   - else, return True
#
# - define main function with no arguments
#   - print introduction (which is the description)
#
#   - get <a> as a float conversion of input from prompt "Enter first side length: "
#   - get <b> as a float conversion of input from prompt "Enter second side length: "
#   - get <c> as a float conversion of input from prompt "Enter third side length: "
#
#   - if is_triangle(<a>, <b>, <c>) is True:
#       - print("The side lengths", a, b, c, "will create a triangle.")
#   - else:
#       - print("The side lengths", a, b, c, "will not create a triangle.")
#
# - run main (second option)
#


def is_triangle(a, b, c):
    # check if any side is greater than the sum of the other two and return False if they do not
    if c > a + b or a > c + b or b > c + a:
        return False
    else:
        return True


def main():
    # introduction (which is the description)
    print("\nThis program will take 3 side lengths as input,\n" +
          "and determine whether or not those side lengths can create a triangle\n" +
          "by testing if any side is greater than the sum of the other two.\n")

    # get user input for each side
    a = float(input("\nEnter first side length: "))
    b = float(input("\nEnter second side length: "))
    c = float(input("\nEnter third side length: "))

    # use function to determine True or False and print coherent results
    if is_triangle(a, b, c):
        print("\nThe side lengths", a, b, c, "will create a triangle.")
    else:
        print("\nThe side lengths", a, b, c, "will not create a triangle.")


if __name__ == '__main__':
    main()
