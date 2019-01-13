# U06_Ex01_Old_MacDonald.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 13 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 01
#     Source: Python Programming
#    Chapter: 06
#
# Program Description
#   This program will print the lyrics of the song "Old MacDonald"
# for five different animals using functions to reduce code.
#
#
# Algorithm (pseudocode)
"""
- print introduction

- def run_song(animal, noise)

- def main()
    - run_song('cow', 'moo')
    - run_song('pig', 'oink')
    - run_song('horse', 'neigh')
    - run_song('chicken', 'cluck')
    - run_song('duck', 'quack')

main()
"""


def run_song(animal, noise):
    """
    - This function will use the animal and noise as input
    to simplify the printing of "Old MacDonald"

    - set eeigh to ', Ee-igh, Ee-igh, Oh!'
    - set omd to 'Old Macdonald had a farm'

    - print(omd + eeigh)
    - print('And on that farm he had a {0}{1}'.format(animal, eeigh)
    - print('With a {0}, {0} here and a {0}, {0} there,'.format(noise))
    - print('Here a {0}, there a {0}, everywhere a {0}, {0}.'.format(noise))
    - print(omd + eeigh + "\n")
    """

    eeigh = ', Ee-igh, Ee-igh, Oh!'
    omd = 'Old Macdonald had a farm'

    print(omd + eeigh)
    print('And on that farm he had a {0}{1}'.format(animal, eeigh))
    print('With a {0}, {0} here and a {0}, {0} there,'.format(noise))
    print('Here a {0}, there a {0}, everywhere a {0}, {0}.'.format(noise))
    print(omd + eeigh + "\n")


def main():
    print('\nThis program will print the lyrics of the song "Old MacDonald"\n' +
          'for five different animals using functions to reduce code.\n')

    run_song('cow', 'moo')
    run_song('pig', 'oink')
    run_song('horse', 'neigh')
    run_song('chicken', 'cluck')
    run_song('duck', 'quack')


main()
