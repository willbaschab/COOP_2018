# U05_EX03_ExamGrades.py.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 02 Dec 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 03
#     Source: Python Programming
#    Chapter: 05
#
# Program Description
#  This program takes an exam score as integer input
# and will return the letter grade of that score
# on the scale that 90-100 is an A, 80-89 is a B,
# 70-79 is a C, 60-69 is a D, and below 60 is an F.
#
# Algorithm (pseudocode)
"""
- print introduction

- get <raw_score> as input
- divide <raw_score> by 10 and save it into <exam_score> as an integer

- set <letter_grades> to "f" * 5 + "DCBAA"
- set <letter_score> to <letter_grades>[<exam_score - 1]

- print output in a complete sentence listing the input(s)
and stating what was returned and what it means (using string format)
"""


def main():
    # introduction
    print("\nThis program takes an exam score as integer input"
          "\nand will return the letter grade of that score"
          "\non the scale that 90-100 is an A, 80-89 is a B,"
          "\n70-79 is a C, 60-69 is a D, and below 60 is an F.\n")

    # get score from user
    raw_score = int(input("Enter exam score as integer input: "))
    exam_score = raw_score // 10

    letter_grades = "f" * 5 + "DCBAA"
    letter_score = letter_grades[exam_score - 1]

    # print out original score and letter grade
    print("\nThe exam score {0} is the letter grade {1}".format(raw_score, letter_score))


main()
