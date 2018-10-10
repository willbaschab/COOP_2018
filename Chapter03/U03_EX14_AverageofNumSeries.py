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
# 3. create a list and total variable with the list being empty and the the total initialized at 0
# 4. create for loop in the range of the amount user entered
#   5. check if place in series is 0, 1, 2 or anything else.
#       6. if 0, ask for user input of number and appended to list with message "Enter 1st number: "
#       7. if 1, ask for user input of number and appended to list with message "Enter 2nd number: "
#       8. if 2, ask for user input of number and appended to list with message "Enter 3rd number: "
#       9. for anything else, ask for user input of number and appended to list with message "Enter xth number: "
#   10. total amount is added to total + number in position i of the series
# 11. average of numbers is the total over the amount rounded to the 2nd decimal place
# 12. print out sentence with total


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
