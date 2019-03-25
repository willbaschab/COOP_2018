# U08_EX4_Syracuse_Sequence.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Mar 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 04
#     Source: Python Programming
#    Chapter: 08
#
# Program Description
#  This program takes a integer value from the user as input,
# and returns the Syracuse sequence of that number.
#
#  The Syracuse sequence checks if a number is even or odd. If the number
# is odd it will multiply the number by 3 and add 1. If the number is even
# it will divide the number by two. This process repeats until the number reaches 1.
# Algorithm (pseudocode)
"""
 - print introduction

 - get the first entree of the complete sequence (call variable sequence)

 - start a while loop that will run as long as the last entree of the sequence is not equal to 1
    - append the result of syr() on the last entree of sequence to the sequence (It takes the previous
    entree and applies the function to get the next number)

 - print out complete output using the sequence and the first entree of the sequence
"""


def syr(x):
    """
    This function returns the result of the syr() function mentioned in
    Chapter 8, exercise 4 of John Zelle's Python Programming: An Introduction to Computer Science

    ALG:
     - check if number is even by checking if the number has a 0 remainder divided by 2
        - return the result of dividing the number by 2
     - use and else statement (if it is not even, it is odd) and return the result of 3 * x  + 1
    """
    if x % 2 == 0:
        return int(x/2)  # if no int() this will return a not so nice looking float
    else:
        return x * 3 + 1


def main():
    # Introduction:
    print("\n This program takes a integer value from the user as input," +
          "\nand returns the Syracuse sequence of that number." +
          # double space here "\n\n"
          "\n\n The Syracuse sequence checks if a number is even or odd. If the number" +
          "\nis odd it will multiply the number by 3 and add 1. If the number is even" +
          "\nit will divide the number by two. This process repeats until the number reaches 1." +
          "\nAlgorithm (pseudocode)")

    # Initial Input:
    sequence = [int(input("\nEnter an integer to see the syracuse sequence of: "))]

    # Program "active" state:
    while sequence[len(sequence) - 1] != 1:  # check if last number of sequence is not 1
        sequence.append(syr(sequence[len(sequence) - 1]))  # appends the result of syr(last entree) to the sequence

    # End Message:
    print("\nThe Syracuse sequence for {0} is {1}".format(sequence[0], ' '.join("{0}".format(i) for i in sequence)))
    # .join is used so that this: "[3] [5] [6]" turns into "3 5 6", which is nicer formatting
    # the formatting part goes through the sequence and converts each number into a string so that it can be used in
    # .join


if __name__ == '__main__':
    main()

"""
RESULTS:
========
syr(5)    -->   16 |   16 | [ Pass ]
syr(16)   -->    8 |    8 | [ Pass ]
syr(8)    -->    4 |    4 | [ Pass ]
syr(4)    -->    2 |    2 | [ Pass ]
syr(2)    -->    1 |    1 | [ Pass ]
syr(3)    -->   10 |   10 | [ Pass ]
syr(7)    -->   22 |   22 | [ Pass ]
syr(11)   -->   34 |   34 | [ Pass ]
syr(17)   -->   52 |   52 | [ Pass ]
========
"""