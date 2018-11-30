#!/usr/bin/python

# STEP 3 - Code the 'main' function to play the game
# In this step we replace the 'main' function with code that runs the game

from __future__ import print_function

# We need to import the 'random' Python library in order to generate random numbers
import random


class Boxer(object):
    """
    An Object to describe a Boxer and the actions he/she takes
    """

    def __init__(self, name):
        """Create a new boxer with a name and set starting health"""
        self.name = name
        self.health = 100

    @property
    def standing(self):
        """A property we can check at any time to see if the boxer is still standing"""
        if self.health > 0:
            return True
        else:
            return False

    def punch(self):
        """Boxer throws a punch.  We randomly choose damage between 1 and 10"""
        damage = random.randint(1, 10)
        return damage

    def punched(self, damage):
        """Boxer gets punched and receives damage"""
        self.health = self.health - damage


def main():
    """This function starts the program"""

    # Ask the player for their name
    name = raw_input("Please enter your name: ")

    # Create the player as a new Boxer
    player = Boxer(name)

    # Create the Computer boxer
    computer = Boxer("Computer")

    # Print out the initial health stats
    print("{0}: {1}".format(player.name, player.health))
    print("{0}: {1}".format(computer.name, computer.health))
    print("")

    # Start our game loop and keep repeating until someone falls down
    while player.standing and computer.standing:

        # Pause and wait for the player to hit enter to punch
        raw_input("Press enter to punch")

        # Computer punches the player
        player.punched(computer.punch())

        # Player punches the computer
        computer.punched(player.punch())

        # Print out the stats after they punch each other
        print("{0}: {1}".format(player.name, player.health))
        print("{0}: {1}".format(computer.name, computer.health))
        print("")

    # Once someone falls down the loop stops
    if player.standing:
        print("KNOCKOUT! YOU WON!")
        print("")
    else:
        print("You lost. Too bad")
        print("")


if __name__ == "__main__":

    # run the main function
    main()
