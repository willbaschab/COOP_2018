# U05_EX04_Acronymer.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 02 Dec 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 04
#     Source: Python Programming
#    Chapter: 05
#
# Program Description
#  This program takes a phrase as input entered by the user
# and will return an acronym (in CAPS) of the phrase.
#
# Algorithm (pseudocode)
"""
- print introduction

- set <phrase> to user input

- set <acronym> to ""

- start a for loop of <word> in <phrase>.split
    - set <first_letter> to <word>[0]
    - set <acronym> to (<acronym> + <first_letter>).upper

- print output with original phrase and acronym (with string formatting)
"""


def main():
    print("\nThis program takes a phrase as input entered by the user"
          "\nand will return an acronym (in CAPS) of the phrase.\n")

    phrase = input("Enter the phrase to make into an acronym: ")

    acronym = ""

    for word in phrase.split():
        first_letter = word[0]
        acronym = (acronym + first_letter).upper()

    print('\nThe phrase "{0}" has the acronym "{1}".'.format(phrase, acronym))


main()
