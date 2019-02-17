# U07_EX06_SpeedTicketCalc.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 17 Feb 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 06
#     Source: Python Programming
#    Chapter: 07
#
# Program Description
#   Because this program is for Pondunksville PD, the fine policy is
# $50 plus $5 for each mph over the limit plus a penalty of $200
# for any speed over mph. The program will take a speed limit and
# a clocked speed as input. It will return whether or not the speed
# is legal or if it is above the speed limit and what the fine is for
# that speed.
#
# Algorithm (pseudocode)
"""
- Print introduction

- get clocked speed and speed limit as input

- set fine = to fine(clockspeed, speedlimit)

- check if fine is equal to 0:
    - print the speed, the speed limit, the difference between the speed limit and the speed
    and that the speed is legal (because the fine is $0)
- else the fine is anything else:
    - print the speed, the speed limit, the difference between the speed limit and the speed,
    the fine needed to be charged, and that the speed is illegal

"""


def getfine(clockspeed, speedlimit):
    """
    - first check if the speed is legal and return a fine of 0 if it is

    - else since the clockspeed is over the fine:
        - set the amount to add to the fine based on subtracting the speedlimit from the speed and multiplying by
        5 dollars

        - make sure that if the speed is over 90 than there is a fine of $200 + the $50 and the miles over time 5

        - if it isn't return only $50 and the added miles times 5 fine
    """
    if clockspeed <= speedlimit:

        return 0
    else:
        plusfine = (int(clockspeed) - speedlimit) * 5  # if it's less than 1.0 mile above than it doesn't count

        if clockspeed > 90:
            return 250 + plusfine
        else:
            return 50 + plusfine


def main():
    print('\nBecause this program is for Pondunksville PD, the fine policy is'
          '\n$50 plus $5 for each mph over the limit plus a penalty of $200'
          '\nfor any speed over mph. The program will take a speed limit and '
          '\na clocked speed as input. It will return whether or not the speed'
          '\nis legal or if it is above the speed limit and what the fine is for'
          '\nthat speed.')

    speedlimit = float(input("\nEnter the speed limit (without mph): "))
    clockspeed = float(input("\nEnter the speed of the vehicle (without mph): "))

    fine = getfine(clockspeed, speedlimit)

    if fine == 0:
        print('\nThe vehicle is obeying the speed limit,'
              '\n{0}mph, and is under it by {1:2.1f}mph going at a speed of {2}mph'.format(speedlimit,
                                                                              speedlimit - clockspeed,
                                                                              clockspeed))
    else:
        print('\nThe vehicle is BREAKING the speed limit,'
              '\n{0}mph, and is over it it by {1:2.1f}mph going at a speed of {2}mph. The fine is ${3}.'.format(speedlimit,
                                                                                                  clockspeed-speedlimit,
                                                                                                  clockspeed,
                                                                                                  fine))


if __name__ == '__main__':
    main()

"""
RESULTS:
========
getfine(29, 30)     -->     0 |     0 | [ Pass ]
getfine(30, 30)     -->     0 |     0 | [ Pass ]
getfine(33, 30)     -->    65 |    65 | [ Pass ]
getfine(30.5, 30)   -->    50 |    50 | [ Pass ]
getfine(80, 75)     -->    75 |    75 | [ Pass ]
getfine(90, 75)     -->   125 |   125 | [ Pass ]
getfine(100, 75)    -->   375 |   375 | [ Pass ]
========
"""