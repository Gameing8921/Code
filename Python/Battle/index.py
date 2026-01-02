import random
from character import Character

opponentNames = ["Zombie", "Assassin", "Slime", "God"]

player = Character(input("Name: "))
opponent = Character(random.choice(opponentNames))
