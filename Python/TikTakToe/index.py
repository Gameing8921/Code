"""
Docstring for Python.TikTakToe.index

Winning lines = [0, 1, 2], [3, 4, 5], [6, 7, 8]
                [0, 3, 6], [1, 4, 7], [2, 5, 8]
                [0, 4, 8], [2, 4, 6]
"""

winningLines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]


class Player:
    def __init__(self):
        self.takenSpaces = []

    def play(self):
        move = int(input("Where do you wanna move (0-8): "))

        self.takenSpaces.append(move)


player = Player()
player.play()
player.play()


def check_best_move(player):
    for line in winningLines:
        count = 0
        missing = None

        for space in line:
            if space in player.takenSpaces:
                count += 1
            else:
                missing = space

        # If the player has 2 of the 3, and the missing one is free:
        if count == 2 and missing not in player.takenSpaces:
            return missing

    return None


print(check_best_move(player))

# UNFINISHED
