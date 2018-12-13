# U05_EX08_CaeserCipherWheel.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 09 Dec 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 08
#     Source: Python Programming
#    Chapter: 05
#
# Program Description
#  Using this program, the user can choose from the menu,
# with each number choice corresponding to each action.
# The program uses a Caesar cipher to encrypt
# or decrypt a phrase without special characters.
# The Caesar cipher is a simple substitution cipher
# based on the idea of shifting each letter of
# the plaintext message a fixed number (called the key)
# of the positions in the alphabet.
#
# Algorithm (pseudocode)
"""
- set up decrypt, encrypt, and intro functions

- set up main function
    - start while loop for TRUE
        - print introduction and menu
        - set choice variable to user input

        - if choice is 3:
            - exit program with exit message

        - else if choice is 2:
            - get key and phrase input
            - print output using encrypt(phrase, -key) in a complete sentence

        - else if choice is 1:
            - get key and phrase input
            - print output using encrypt(phrase, key) in a complete sentence

        - else
            - tell user that choice was invalid

- run main
"""


def print_intro():
    """
    - This function just prints the introduction  with a couple of separate print statements
    """
    print("\nCAESAR CIPHER PROGRAM\n")

    print("Using this program, the user can choose from the menu," +
          "\nwith each number choice corresponding to each action." +
          "\nThe program uses a Caesar cipher to encrypt" +
          "\nor decrypt a phrase without special characters." +
          "\nThe Caesar cipher is a simple substitution cipher" +
          "\nbased on the idea of shifting each letter of" +
          "\nthe plaintext message a fixed number (called the key)" +
          "\nof the positions in the alphabet.\n")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit\n")


def encrypt(phrase, key):
    """
    - This is the encryption function, which only differs from the
    decryption function by going forward (+) in the Caesar cipher
    rather than backward (-)

    - set the alphabet as a variable
    - turn the user input into a lowercase list of strings and store in a variable for easy use
    - set accumulator variable to empty string

    - begin for loop for <word> in <lowercase list of strings>
        - begin for loop for <letter> in <word>:
            - set accumulator to itself plus alpha[(alpha.find(letter) + key) % 26]

        - if the word is not equal to the last item in the list of the phrase,
            - add a space to the end of the accumulator

    - return the accumulator
    """

    alpha = "abcdefghijklmnopqrstuvwxyz"
    phrase_list = (phrase.lower()).split()
    encrypted_string = ""

    for word in phrase_list:
        for letter in word:
            encrypted_string += alpha[(alpha.find(letter) + key) % 26]

        if word != phrase_list[len(phrase_list) - 1]:
            encrypted_string += " "

    return encrypted_string


def main():
    while True:
        print_intro()

        a = int(input("Enter a number that corresponds with your choice: "))

        if a == 3:
            print("\nYou have exited the program!")
            break

        elif a == 2:
            phrase = input("\nEnter the phrase to decrypt using the " +
                           "Caesar Cipher Wheel (only letters and spaces): ")
            key = int(input("\nEnter the key (as an integer) to decrypt the phrase by: "))

            print('\nThe encrypted phrase "{0}" using the key {1} is "{2}"'.format(phrase, key, encrypt(phrase, -key)))

        elif a == 1:
            phrase = input("\nEnter the phrase to encrypt using the " +
                           "Caesar Cipher Wheel (only letters and spaces): ")
            key = int(input("\nEnter the key (as an integer) to encrypt the phrase by: "))

            print('\nThe phrase "{0}" encrypted with the key {1} is "{2}"'.format(phrase, key, encrypt(phrase, key)))

        else:
            print("Please choose a valid number choice!")


main()
