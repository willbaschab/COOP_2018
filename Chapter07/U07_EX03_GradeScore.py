# U07_EX03_GradeScore.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 08 Feb 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 03
#     Source: Python Programming
#    Chapter: 07
#
# Program Description
#  This program accepts a grade score from 0 to 100 as input.
# It will return the letter grade using the scale:
# 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F.
#
# Algorithm (pseudocode)
"""
- print introduction

- get grade as input
    - also make sure to catch users who don't understand the requirement

- for whatever score range grade is, print output of correct letter and score
using the function to get letter


"""


def letter_convert(score):
    """
    This function will return the correct grade of a score

    - begin from greatest to least grade to check
    if the grade is lower than an A, B, C... and if the grade is valid

    """
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 100:
        return 'B'
    elif 70 <= score <= 100:
        return 'C'
    elif 60 <= score <= 100:
        return 'D'
    elif 0 <= score <= 100:
        return 'F'
    else:
        return 'Invalid score'


def main():
    print('\nThis program accepts a grade score from 0 to 100 as input.' +
          '\nIt will return the letter grade using the scale:' +
          '\n90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F.\n')

    try:
        score = int(input("Enter the exam score: "))
    except ValueError:
        score = int(input("\nThis program grades integer values only\n"
                          "as the requirements only allow POINT values\n"
                          "from 0 to 100. Please enter the exam score: "))

    print("\nA {0} on the exam is the letter {1}".format(score, letter_convert(score)))


if __name__ == '__main__':
    main()

"""
RESULTS:
========
letter_convert(110)   -->   Invalid score |   Invalid score | [ Pass ]
letter_convert(100)   -->               A |               A | [ Pass ]
letter_convert(95)    -->               A |               A | [ Pass ]
letter_convert(90)    -->               A |               A | [ Pass ]
letter_convert(89)    -->               B |               B | [ Pass ]
letter_convert(80)    -->               B |               B | [ Pass ]
letter_convert(79)    -->               C |               C | [ Pass ]
letter_convert(70)    -->               C |               C | [ Pass ]
letter_convert(69)    -->               D |               D | [ Pass ]
letter_convert(60)    -->               D |               D | [ Pass ]
letter_convert(59)    -->               F |               F | [ Pass ]
letter_convert(0)     -->               F |               F | [ Pass ]
letter_convert(-1)    -->   Invalid score |   Invalid score | [ Pass ]
========
"""

