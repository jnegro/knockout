#!/usr/bin/python

# Knockout2 - Step 1: Add blocking into the Boxer Class
# We start out where we left on knockout.py, but now we want to add
# the capability of blocking punches to the Boxer class.  Even
# though we made changes, the 'main' function doesn't use them yet
# so the program will work just as it did before

from __future__ import print_function

import random


class Boxer(object):
    """
    An Object to describe a Boxer and the actions he/she takes
    This time we added a blocking action
    """

    def __init__(self, name):
        """
        Create a new boxer with a name, set starting health and blocking status
        This method runs automatically when a new Boxer is created

        """
        self.name = name
        self.health = 100
        self.blocking = False

        # stamina is the maximum damage a Boxer can cause.  Every time the Boxer is blocked
        # they lose one stamina.  Stamina resets if a Boxer blocks opponent successfully
        # or both block each other
        self.stamina = 10

    @property
    def standing(self):
        """A property we can check at any time to see if the boxer is still standing"""
        if self.health > 0:
            return True
        else:
            return False

    def punch(self):
        """Boxer throws a punch.  We randomly choose damage between 1 and their current stamina"""
        damage = random.randint(1, self.stamina)
        return damage

    def block(self):
        """Boxer blocks instead of punching"""
        self.blocking = True

    def punched(self, damage):
        """Boxer gets punched and receives damage"""
        self.health = self.health - damage

    def blocked(self):
        """Boxer gets blocked and loses stamina"""
        if self.stamina > 1:
            self.stamina = self.stamina - 1

    def reset_stamina(self):
        """Reset the boxers stamina"""
        self.stamina = 10

    def reset(self):
        """Reset blocking status"""
        self.blocking = False


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


# This is where the program actually starts running
if __name__ == "__main__":

    # run the main function
    main()
