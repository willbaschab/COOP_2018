# U05_EX14_FileWordCount.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 17 Dec 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 14
#     Source: Python Programming
#    Chapter: 05
#
# Program Description
#  This program accepts a file name as input, and searches inside
# the file to return the number of words, number of lines, and
# and number of characters. This is done using string methods
# such as .split(), len(), and others.
#
# Algorithm (pseudocode)
"""
- print introduction

- get file name as input and store in <name>
- set <file> to open(name, "r")

- initialize accumulators line_count, word_count, character_count

- begin a for loop for line in file.readlines()
    - being a for loop for word in (line[:-1].split())
        - add 1 to word_count
        - add len(word.strip("\n") to character_count
    - add 1 to line_count

- print output in complete sentence with filename, line_count, word_count,
and character_count.

- close the file
"""


def main():
    print("This program accepts a file name as input, and searches inside" +
          "\nthe file to return the number of words, number of lines, and" +
          "\nand number of characters. This is done using string methods" +
          "\nsuch as .split(), len(), and others.\n")

    name = input('Enter name of file as well as .txt extension on end: ')
    file = open(name, "r")

    line_count, word_count, character_count = 0, 0, 0

    for line in file.readlines():
        for word in (line[:-1].split()):
            word_count += 1
            character_count += len(word.strip("\n"))

        line_count += 1
    print("The file {0}.txt has {1} lines, {2} words, and {3} characters.".format(name, line_count, word_count,
                                                                                  character_count))
    file.close()


main()
