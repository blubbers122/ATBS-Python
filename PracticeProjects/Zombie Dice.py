import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while True:
            num = random.randint(0,1)
            if num == 1:
                zombiedice.roll()
            else:
                break


class MyZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        while True:
            diceRollResults = zombiedice.roll()
            if diceRollResults == None:
                break
            print(diceRollResults)
            brains = diceRollResults["brains"]
            print(brains)
            if brains >= 2 or brains == None:
                break


class MyZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        while True:
            diceRollResults = zombiedice.roll()
            if diceRollResults == None:
                break
            elif diceRollResults["shotgun"] == 2:
                break
            else:
                zombiedice.roll()




zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    #MyZombie(name='Random stop after 1 roll'),
    #MyZombie(name="stop rolling after 2 brains"),
    MyZombie(name="stop rolling after 2 shotguns")
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)