# U03_EX03_MolecularWeight.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 03
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#  This program calculates the molecular weight of a carbohydrate with the amount of
# Hydrogen, Carbon, and Oxygen atoms in the molecule inputted.
#
#
# Algorithm (pseudocode)
# 1. print introduction
# 2. get user input for 3 amounts of atoms
# 3. calculate weight for each atom by multiplying amount by mass with three variables
# 4. calculate total mass with one variable
# 5. print out total mass in a sentence


def main():
    print("\nThis program calculates the molecular weight of a carbohydrate with the amount of\n" +
          "Hydrogen, Carbon, and Oxygen atoms in the molecule inputted.")

    hamount = int(input("\nEnter the number of Hydrogen atoms: "))
    camount = int(input("\nEnter the number of Carbon atoms: "))
    oamount = int(input("\nEnter the number of Oxygen atoms: "))

    hmass, cmass, omass = hamount * 1.00794, camount * 12.0107, oamount * 15.9994

    totalmass = hmass + cmass + omass

    print("\nThe total mass of a carbohydrate with", hamount, "Hydrogen atoms,", camount, "Carbon atoms, and", oamount,
          "Oxygen atoms is", totalmass, "grams per mole.")


main()
