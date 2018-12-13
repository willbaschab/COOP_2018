# U05_EX06_Numerology.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 07 Dec 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 06
#     Source: Python Programming
#    Chapter: 05
#
# Program Description
#  This program will take a full name as input,
# and will return the numeric value of that name.
# This value is determined by summing up the
# values of the letters of the name where "a"
# is 1, "b" is 2, "c" is 3, up to "z" being 26.
#
# Algorithm (pseudocode)
"""
- print introduction

- get <name> as input from user

- set accumulator <total> to 0

- start a for loop for <word> in (<name>.lower()).split()
    - start a for loop for <letter> in <word>
        - <accumulator> = <accumulator> + (ord(<letter>) - 96)

- print output in complete sentence stating original name and numeric value

"""


def main():
    print('\nThis program will take a full name as input,' +
          '\nand will return the numeric value of that name.' +
          '\nThis value is determined by summing up the' +
          '\nvalues of the letters of the name where "a"' +
          '\nis 1, "b" is 2, "c" is 3, up to "z" being 26.\n')

    name = input("Enter your full name: ")

    total = 0

    for word in (name.lower()).split():
        for letter in word:
            total = total + (ord(letter) - 96)

    print('\nThe name, "{0}", has the numeric value of {1}.'.format(name, total))



main()
