# U08_EX6_Prime_Numbers.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Mar 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 06
#     Source: Python Programming
#    Chapter: 08
#
# Program Description
#  This program will take a number as input and displays all the prime numbers equal to or
# below it.
#
#  A positive whole number n, which is greater than 2, is prime if no number between 2 and the square root of n
# (inclusive) evenly divides n.
#
# Algorithm (pseudocode)
"""
- print introduction

- get number as input and store in variable (called num)

- If the prime number function returns something:
    print out the original number and the sequence of prime numbers equal to or below it using
correct formatting (using a function to get equal and lower prime numbers under the input)
- If it does not, print out that the number is not prime
"""
import math


def is_prime(n):
    """
    This function returns true if argument is a prime but returns false if argument is composite

    ALG:
    - for loop does not work for 0 and 1, but neither are prime so check if n is less than 2
    (therefore 0 or 1) and return false

    - for every value between 2 (including 2) and the (square root of n)*
        - if the remainder of n and the value is equal to 0, n is composite

    - since we have gotten past the for loop, n has passed the prime test and is prime
    return true

    *for this to work:
        Most numbers have square roots that are decimals, however to use range(2, math.sqrt(n))
    2 and math.sqrt(n) must both be integers. math.sqrt(n) will return a float value for all values
    of n. The range function turns into range(2, int(math.sqrt(n))). There is a problem with this though.

        int(math.sqrt(3)) and int(math.sqrt(2)) will return 1, range(2, 1) is an empty list
        int(math.sqrt(5)) and int(math.sqrt(6)) will return 2  range(2, 2) is an empty list

        Well, noticing how 2, 3, and 5 are prime it does not matter if the for loop does not
    run because the function will return true after the for loop. 6 is not prime though, so
    it needs an exception inside the range() function so that it will return at least the factor
    2 in an empty list. Remembering that this method is inclusive to the square root of n as well as
    2, adding 1 to the integer value of a sqrt will include the sqrt as well as 2. This logic doesn't
    hold for 6, but it doesn't have to as range(2, int(math.sqrt(6)) + 1) returns [2]. Since 2 is a
    factor of 6 the function will return false once it runs through. This logic works for 9 the difference being:

        range(2, int(math.sqrt(9))) returning [2] (since 2 doesn't go into 9, it would think 9 is prime)
        range(2, int(math.sqrt(9)) + 1) returning [2, 3] (3 does go into 9, and so it returns false)

        This logic will allow the for loop to work for both the first several prime numbers and all after.



    """
    if n < 2:  # checks if n is 1 or 0, which the loop below will work for. 0 and
        return False

    for i in range(2, int(math.sqrt(n)) + 1):  # please refer to above 'rant' for explanation
        if n % i == 0:  # checks if potential factor is a factor and returns false
            return False

    return True  # if the loop ended without returning false, no composite was found and so function returns true


def prime_sequence(num):
    """
    This function will return an array of all numbers equal to or below the argument that are prime

    ALG:
    - initialize an array variable (called list)

    - for every number between the argument and 0:
        - check if number is prime using is_prime() and if the number is, append it to the array

    - return array
    """

    # very simple 1 line statement of intended algorithm
    return [i for i in range(num, 1, -1) if is_prime(i)]
    # simplified: return an array of ( numbers for every number between argument and 1 by an increment 1
    # only being added if is_prime(i) returns True)


def main():
    # Introduction:
    print("\nThis program will take a whole positive integer as input and displays " +
          "\nall the prime numbers equal to or below it." +
          "\n\nA positive whole number n, which is greater than 2, " +
          "\nis prime if no number between 2 and the square root of n (inclusive) evenly divides n.")

    # Initial Input:
    num = int(input("\nEnter a whole positive integer \nto find all prime numbers below or equal to: "))

    # End Message
    if prime_sequence(num):  # if the sequence returns something, the number has prime ones below it or is on itself
        print("The prime numbers equal to or below {0} are {1}".format(num,
                                                                       ' '.join("{0}".format(i)
                                                                                for i in prime_sequence(num))))

    else:  # if the number does not return anything, it is not prime and has nothing below it that is prime
        print("{0} is not a prime number and \nthere are no prime numbers below {0}".format(num))


if __name__ == '__main__':
    main()

"""
RESULTS:
========
is_prime(0)    -->       0 |       0 | [ Pass ]
is_prime(1)    -->       0 |       0 | [ Pass ]
is_prime(2)    -->       1 |       1 | [ Pass ]
is_prime(3)    -->       1 |       1 | [ Pass ]
is_prime(4)    -->       0 |       0 | [ Pass ]
is_prime(5)    -->       1 |       1 | [ Pass ]
is_prime(6)    -->       0 |       0 | [ Pass ]
is_prime(7)    -->       1 |       1 | [ Pass ]
is_prime(8)    -->       0 |       0 | [ Pass ]
is_prime(51)   -->       0 |       0 | [ Pass ]
is_prime(47)   -->       1 |       1 | [ Pass ]
========
"""