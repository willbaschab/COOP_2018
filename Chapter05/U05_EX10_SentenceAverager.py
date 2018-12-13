# U05_EX10_SentenceAverager.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 12 Dec 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 10
#     Source: Python Programming
#    Chapter: 05
#
# Program Description
#  This program takes a sentence as input
# and will return the average word length
# of that sentence.
#
#
# Algorithm (pseudocode)
"""
- set up intro and sent_average functions

- set up main function
    - start while loop for TRUE
        - print introduction and menu
        - set choice variable to user input

        - if choice is 2:
            - exit program with exit message

        - else if choice is 1:
            - get user input as sentence
            - print output using sent_average(sentence)
            in a complete sentence with input stated.

        - else
            - tell user that choice was invalid

- run main
"""


def print_intro():
    """
    - This function just prints the introduction  with a couple of separate print statements
    """
    print("\nSENTENCE WORD AVERAGE PROGRAM\n")

    print("This program takes a sentence as input" +
          "\nand will return the average word length" +
          "\nof that sentence. Select a menu choice by" +
          "\nentering the number to the left of your choice.\n")

    print("1. Average the length of word in a sentence")
    print("2. Exit\n")


def sent_average(sentence):
    """
        - set a variable that is the amount of words in the sentence
        - set up accumulator of total characters (a-z or A-Z) in the sentence

        - start a for loop for each word in the sentence.split()
            - start a for loop for every letter in the word
                - if the letter is between a-z or A-Z (using ord), add one to the accumulator

        - return the accumulator divided by the amount of words in the sentence
        to the second decimal place
    """
    sentence_words = len(sentence.split())
    total_chars = 0

    for word in sentence.split():
        for letter in word:
            if (96 < ord(letter) < 123) or (64 < ord(letter) < 91):
                total_chars += 1

    return round(total_chars/sentence_words, 2)


def main():
    while True:
        print_intro()

        a = int(input("Enter a number that corresponds with your choice: "))

        if a == 2:
            print("\nYou have exited the program!")
            break

        elif a == 1:
            sentence = input("\nEnter the sentence to see its average word length: ")

            print('\nThe sentence "{0}" has {1} word(s) in it.'.format(sentence, len(sentence.split())) +
                  '\nand the average word length is {0}'.format(sent_average(sentence)))

        else:
            print("Please choose a valid number choice!")


main()

