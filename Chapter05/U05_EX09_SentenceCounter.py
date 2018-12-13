# U05_EX09_SentenceCounter.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 12 Dec 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 09
#     Source: Python Programming
#    Chapter: 05
#
# Program Description
#  This program allows the user to enter a sentence
# and see how many words are in the sentence. This
# is done using string manipulation and for loops.
#
#
#
#
#
#
#
# Algorithm (pseudocode)
"""
- set up intro function

- set up main function
    - start while loop for TRUE
        - print introduction and menu
        - set choice variable to user input

        - if choice is 2:
            - exit program with exit message

        - else if choice is 1:
            - get user input as sentence
            - print output using len(sentence.split()) in a complete sentence

        - else
            - tell user that choice was invalid

- run main
"""


def print_intro():
    """
    - This function just prints the introduction  with a couple of separate print statements
    """
    print("\nSENTENCE COUNTER PROGRAM\n")

    print("This program allows the user to enter a sentence" +
          "\nand see how many words are in the sentence. This" +
          "\nis done using string manipulation and for loops." +
          "\n Select a menu choice by entering the number to" +
          "\nthe left of your choice.\n")
    print("1. Count words in sentence")
    print("2. Exit\n")


def main():
    while True:
        print_intro()

        a = int(input("Enter a number that corresponds with your choice: "))

        if a == 2:
            print("\nYou have exited the program!")
            break

        elif a == 1:
            sentence = input("Enter the sentence to count all the words in: ")

            print('\nThe sentence "{0}" has {1} word(s) in it.'.format(sentence, len(sentence.split())))

        else:
            print("Please choose a valid number choice!")


main()

