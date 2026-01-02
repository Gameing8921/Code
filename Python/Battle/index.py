import random


class Character:
    def __init__(self, name, type):
        self.name = name

    def setIvs(self):
        self.atk += random.randint(0, 31)
        self.defense += random.randint(0, 31)
        self.hp += random.randint(0, 31)
        self.speed += random.randint(0, 31)

    def setEvs(self):
        fullEvs = 510
        deducted = 510
        deduction = 0

        while fullEvs != 0:
            deduction = random.randint(0, 252)

            self.atk += int(deduction / 4)
            deducted -= deduction
            deduction = random.randint(0, 252)

            self.defense += int(deduction / 4)
            deducted -= deduction
            deduction = random.randint(0, 252)

            self.hp += int(deduction / 4)
            deducted -= deduction
            deduction = random.randint(0, 252)

            self.speed += int(deduction / 4)
            deducted -= deduction
            deduction = random.randint(0, 252)

    def attack(self, opponentDefense, opponentHp, opponentSpeed, power):
        if self.speed > opponentSpeed:
            opponentHp -= ((200 * random.randint(1, 2)) / 5 + 2) * power * (
                self.attack / opponentDefense
            ) / 50 + 2

    def heal(self):
        self.hp += random.randint(1, 75)

    def defend(self):
        self.defense += random.randint(50, 100)
