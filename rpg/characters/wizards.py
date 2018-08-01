''' Wizard subclass of common Character.

Has additional attributes and alternative method for alive status to apply recuperation if possible and needed
'''
from . import common

class Wizard(common.Character):

    def __init__(self,name, health, hitpoints, char_type='wizard', spells=[], potions=[]):
        common.Character.__init__(self, name, health, hitpoints, char_type)
        self.spells = spells
        self.potions = potions
        self.threshold = 50

    def __repr__(self):
        general = common.Character.__repr__(self)
        return general + f' {self.spells} | {self.potions} |'

    def recuperate(self):
        while self.health < self.threshold and not self.potions == []:
            healing = self.potions.pop(0)
            print(f'{self.char_type} {self.name} applied potion to heal by {healing} points')
            self.health += healing

    def alive(self):
        ''' confirm if character is still alive'''

        self.recuperate()
        return self.health > 0