# U09_EX04_Volleyball_Rally_Simulation.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 20 Apr 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 04
#     Source: Python Programming
#    Chapter: 09
#
# Program Description
#  This program simulates n Volleyball games using rally scoring.
# the amount of games, n, is inputted by the user as well as the probability
# that either team will return the ball on an average rally. The program
# will return the amount of games won by each team as well as the probabilities
# that each team had to win a rally.
#
# Algorithm (pseudocode)
"""
Within main:
    print the introduction in a function called printIntro()
    get gamesTotal, probRallyA, probRallyB from function getinputs()
    get gamesWonA, gamesWonB from function simGames(gamesTotal, probRallyA, probRallyB)
    print the output in a function called summary(gamesWonA, gamesWonB, gamesTotal, probRallyA, probRallyB)
"""
from random import *

def printIntro():
    # prints introduction based on description above (I made lines roughly equal length)
    print("\nThis program simulates n Volleyball games using rally scoring." +
          "\nThe amount of games, n, is inputted by the user as well as the" +
          "\nprobability that either team will return the ball on an average" +
          "\nrally. The program will return the amount of games won by each team" +
          "\nas well as the probabilities that each team had to win a rally.")


def getInputs():
    # get total amount of games to be played:
    # Also, a \n is need at the start of every input line so that there is space between
    # them and the intro and eachother.
    n = int(input("\nEnter the total number of games teams A and B will play: "))

    # get Team A's chance at winning a rally:
    probA = float(input("\nEnter the chance, as a decimal, that team A" +
                        "\nwill return the ball on an average rally: "))

    # get Team B's chance at winning a rally:
    probB = float(input("\nEnter the chance, as a decimal, that team B" +
                        "\nwill return the ball on an average rally: "))

    # return all three variables in order they are called by
    return n, probA, probB


def simGames(n, probA, probB):
    #  Simulates n games of Volleyball with both Team A and Team B. Because it is based off rallying,
    # probA and probB are the chances that a team will return the ball on a given rally. It will return
    # to the caller the number of wins for Team A and the number of wins for Team B

    winsA, winsB = 0, 0  # variables need to be initialized before they are referenced

    # For each game out of the total number of games to be simulated, we will run a single game
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        # each game returns the scores of both teams which can be used to decide the winner

        # if Team A had a higher score than Team B for the given game,
        # they won that game and the win is added to their total
        if scoreA > scoreB:
            winsA += 1
        # vice versa for Team B
        else:
            winsB += 1

    return winsA, winsB  # the wins will be returned in the format the caller asked for (A is always first)


def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0  # initialize scores to be referenced later
    server = "A"  # starts off with server being Team A
    while not gameOver(scoreA, scoreB):  # this will return false while no team has 25 pts
        # simOnePoint can't return the actual score, so it returns what is to be added
        # to the actual score (it works) which is addA and addB
        addA, addB, server = simOnePoint(probA, probB, server)

        # the point from the rally, 1 or 0, is added to the scores
        scoreA += addA
        scoreB += addB

    return scoreA, scoreB  # returns scores to caller in format that they are called by


def gameOver(scoreA, scoreB):
    return scoreA == 25 or scoreB == 25 # if one team has 25 points, the game ends


def simOnePoint(probA, probB, server):
    while True:
        if server == "A":
            if random() < probA:  # if Team A hits the ball back (or hits first serve)
                server = "B"  # Team B now has to hit the ball back in the rally when the loop starts over
            else:  # if the ball hits the ground, the point has ended and Team B get a point
                return 0, 1, "B"  # Team B will get a point, but will also have to server next time so we return "B" up
                                  # to the caller (which is server)
        else:
            if random() < probB:  # if Team B hits the ball back (or hits first serve)
                server = "A" # Team A will have to hit the ball back next when the loop starts over
            else:  # the ball hit the ground if they did not hit it
                return 1, 0, "A"  # team A will serve next since they won (and get a point)


def summary(wonA, wonB, n, probA, probB):
    print("")  # spaces output from the previous lines
    print("-" * 60)  # length of table
    print("Team |    Games Won    | Games Played |    Rally Chance    |")  # table titles
    print("-" * 60)  # separation line
    # Each of the values below are centered in the middle of their respective title using string formatting
    print("  A  |{0:^17}|{1:^14}|{2:^20.2%}|".format(wonA, n, probA))  # the last one is a percent with 2 precision
    print("-" * 60) # speration line
    # same as above, but for team B
    print("  B  |{0:^17}|{1:^14}|{2:^20.2%}|".format(wonB, n, probB))


def main():
    printIntro()

    gamesTotal, probRallyA, probRallyB = getInputs()

    gamesWonA, gamesWonB = simGames(gamesTotal, probRallyA, probRallyB)

    summary(gamesWonA, gamesWonB, gamesTotal, probRallyA, probRallyB)


if __name__ == '__main__':
    main()

