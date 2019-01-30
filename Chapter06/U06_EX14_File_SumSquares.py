# U06_EX14_File_SumSquares.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 14
#     Source: Python Programming
#    Chapter: 06
#
# Program Description
#  This program will take a file name
# as input and return the sum of the squares
# of numbers read from the file. It uses
# previous programs and functions to
# do this.
# Algorithm (pseudocode)
"""
- import sumlist(), squareEach(), and toNumbers() from past three
exercises.

- print introduction

- ask for file name as input and save into <name>

- set <file> to open(name, "r")

- set filelines to file.readlines()
- close file

- initialize a variable for storing the original
characters of the file (this is the only way to do this)

- strip newline character from each line
    - append the current character about to be stripped to the original line list

- save original characters in list

- use toNumbers() on filelines
- use squareEach() on file lines

- print output with original file and the sum of each entree in filelines
"""

from Chapter06.U06_EX12_SumList import sumList
from Chapter06.U06_EX11_SquareList import squareEach
from Chapter06.U06_EX13_ToNumbers import toNumbers


def main():
    print("\nThis program will take a file name" +
          "\nas input and return the sum of the squares" +
          "\nof numbers read from the file. It uses" +
          "\nprevious programs and functions to" +
          "\ndo this.\n")

    filename = input('Enter name of file as well as .txt extension on end: ')
    file = open(filename, 'r')

    filelines = file.readlines()
    file.close()

    original_file_lines = []

    for i in filelines:
        original_file_lines.append(i)
        i.strip('\n')

    toNumbers(filelines)
    squareEach(filelines)

    print('\nthe file with characters {0}, made into numbers,'.format(original_file_lines) +
          '\nsquared, and each entree added is the number: {0}'.format(sumList(filelines)))


if __name__ == '__main__':
    main()
