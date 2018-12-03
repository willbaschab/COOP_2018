# U05_EX01_better_datecovert.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Nov 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 01
#     Source: Python Programming
#    Chapter: 05
#
# Program Description
#  This program will take a day, month, and year as integer inputs
# and return the dates in the form of mm/dd/yy and Month Day, Year.
#
#
# Algorithm (pseudocode)
# - print introduction
# - get day, month, and year as input
# - set <date1> to be formatted inputs in format mm/dd/yy
# - set <months> to a list of all months in order from the 1st to 12th month of the year
# - set <monthsStr> to be <months>[<month> - 1]
# - set date2 to be formatted day, <monthsStr>, and year in format Month Day, Year
# - print output in a sentence that provides the inputs given, and then the two dates as output. (using string format)


def main():
    # introduction
    print("\nThis program will take a day, month, and year as integer inputs" +
          "\nand return the dates in the form of mm/dd/yy and Month Day, Year.\n")

    # get the day month and year as numbers
    day = int(input("Enter the day number: "))
    month = int(input("Enter the month number: "))
    year = int(input("Enter the year: "))

    # original: date1 = str(month)+"/"+str(day)+"/"+str(year)
    date1 = "{0}/{1}/{2}".format(month, day, year)

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    monthStr = months[month - 1]

    # original: date2 = monthStr+" " + str(day) + ", " + str(year)
    date2 = "{0} {1}, {2}".format(monthStr, day, year)

    # original: print("The date is", date1, "or", date2 + ".")
    print('\nFrom inputs "day number = {0}", "month number = {1}", and "year = {2}", '.format(day, month, year) +
          '\nthe date is {0} or {1}.'.format(date1, date2))


main()
