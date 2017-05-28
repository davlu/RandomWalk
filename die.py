from random import randint
class Dice():
    def __init__(self, sides=6):        #default side # is 6
        self.sides = sides
    def roll(self):                         #returns randint from 1 to total # sides
        return randint(1,self.sides)

