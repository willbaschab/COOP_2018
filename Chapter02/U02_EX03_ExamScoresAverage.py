# U02_EX03_ExamScoresAverage.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 31 Aug 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 3
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#  This program takes in three exam grades as input and averages the scores
#
#
#
# Algorithm (pseudocode)
# 1. Print Introduction
# 2. Take 3 inputs simultaneously and save them to 3 score variables
# 3. Assign <average> to sum of scores divided by 3
# 4. Print out <average> of <scores>
#


def main():
    print("\nThis program takes three test scores, 0 to 100, and prints out their average.\n")

    score1, score2, score3 = eval(input("Enter three scores separated by 2 commas: "))

    average = (score1 + score2 + score3)/3

    print("\nThe average of", str(score1) + "%", str(score2) + "% and", str(score3) + "% is", str(average) + "%.")

main()