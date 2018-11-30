#!/usr/bin/python

# STEP 2 - Create the Boxer Class
# In this step we create the Boxer class

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
    # Our main function will go here.  For now, lets create a boxer and print his name

    # Ask the player for their name
    name = raw_input("Please enter your name: ")

    # Create the player as a new Boxer
    player = Boxer(name)

    # Print the player's name
    print("The player's name is {0}".format(player.name))


if __name__ == "__main__":

    # run the main function
    main()
