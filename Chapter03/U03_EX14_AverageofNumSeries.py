# U03_EX14_AverageofNumSeries.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 14
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#  This program calculates the average from a series of numbers
# inputted by the user of how many numbers there are and what each number is.
#
#
# Algorithm (pseudocode)
# 1. Print introduction
# 2. get amount of numbers in series from user input
# 3. create for loop in the range of the amount user entered
#   4. total amount is added to total + inputted number
# 5. print out sentence with total


def main():
    print("\nThis program calculates the average from a series of numbers",
          "\ninputted by the user of how many numbers there are in the series and what each number is.")

    amount = int(input("\nEnter amount of numbers in series: "))
    total = 0
    series = []

    for i in range(amount):
        if i == 0:
            series.append(float(input("\nEnter the 1st number: ")))
        elif i == 1:
            series.append(float(input("\nEnter the 2nd number: ")))
        elif i == 2:
            series.append(float(input("\nEnter the 3rd number: ")))
        else:
            series.append(float(input("\nEnter the " + str(i + 1) + "th number: ")))

        total = total + series[i]

    average = round(total/amount, 2)

    print("\nIn your series of", amount, "numbers, " + str(series) + ", the average is", str(average) + ".")


main()
