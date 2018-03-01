from random import randint as rint
from random import randrange

class Character:

    characters = 0

    def __init__(self, name, health, hitpoints, char_type='common'):
        self.char_type = char_type
        self.name = name
        self.hitpoints = hitpoints
        self.health = health
        Character.characters += 1

    def __repr__(self):
        return f'{self.name:>10} | {self.health:5d}) | {self.hitpoints:3d} | {self.char_type:<10} |'

    def combat(self, woundpoints):
        ''' adjust health of character based on woundpoints inflicted. '''

        self.health -= woundpoints
        if self.health < 0: self.health = 0

    def alive(self):
        ''' confirm if character is still alive'''

        return self.health > 0



