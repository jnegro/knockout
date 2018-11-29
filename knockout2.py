#!/usr/bin/python3

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
    name = input("Please enter your name: ")

    # Create the player as a new Boxer
    player = Boxer(name)

    # Create the Computer boxer
    computer = Boxer("Computer")

    # Print out the initial health stats
    print("")
    print("----------------------")
    print(player.name)
    print("Health: {0}".format(player.health))
    print("Stamina: {0}".format(player.stamina))
    print("----------------------")
    print(computer.name)
    print("Health: {0}".format(computer.health))
    print("Stamina: {0}".format(computer.stamina))
    print("----------------------")
    print("")

    # Start our game loop and keep repeating until someone falls down
    while player.standing and computer.standing:

        # Pause and wait for the player to hit enter to punch
        player_action = input("Press enter to punch, or b to block: ")

        # if player blocked, set them as blocked
        if player_action == 'b':
            player.block()

        # Choose 1 in 3 chance that computer punches
        punch_or_block = random.randint(1, 3)
        if punch_or_block == 1:
            computer.block()

        # if both players blocked, stamina resets for both
        if player.blocking and computer.blocking:
            print("Both boxers blocked!")
            player.reset_stamina()
            computer.reset_stamina()
        # else if player blocks computer, reset player stamina and lower computer stamina
        elif player.blocking:
            print("Player blocks computer")
            player.reset_stamina()
            computer.blocked()
        # else if computer blocks player, reset computer stamina and lower player stamina
        elif computer.blocking:
            print("Computer blocks player")
            player.blocked()
            computer.reset_stamina()
        # else no one blocked and they both punched each other
        else:
            print("Players punch each other")
            player.punched(computer.punch())
            computer.punched(player.punch())

        # Print out the stats after they punch each other
        print("")
        print("----------------------")
        print(player.name)
        print("Health: {0}".format(player.health))
        print("Stamina: {0}".format(player.stamina))
        print("----------------------")
        print(computer.name)
        print("Health: {0}".format(computer.health))
        print("Stamina: {0}".format(computer.stamina))
        print("----------------------")
        print("")

        # Reset both players for next move
        player.reset()
        computer.reset()

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
