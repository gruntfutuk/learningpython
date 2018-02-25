''' A simple character battle game - the next step, usig subclasses.'''

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

    @staticmethod
    def fight(player1, player2):
        ''' determine outcomes of fight between two characters. '''

        print(f'... {player1.name} and {player2.name} fight')
        player2.combat(player1.hitpoints)
        player1.combat(player2.hitpoints)

    @staticmethod
    def result(*players):
        ''' output status of characters that are still alive. '''

        alive = []
        print('     Name  | Health | Pwr | Type       | Spells & Potions')
        print('---------------------------------------------------------')
        for player in players:
            if player.alive():
                alive.append(player.name)
                print(player)
        return alive

    @staticmethod
    def battleover(players):
        ''' output status of players alive, and determine if battle has finished. '''

        alive = Character.result(*players)
        if alive == []: print('\n\n** Everyone died **\n\n')
        elif len(alive) == 1: print(f'\n\n** WINNER: {alive[0]} **\n\n')
        return len(alive) <= 1

    @staticmethod
    def pickplayers(NAMES):
        ''' given list of potential character names, choose all or some to become characters in battle. '''

        picks = list(NAMES)
        players = []
        for _ in range(rint(2, len(NAMES))):
            players.append(picks.pop(randrange(len(picks))))
        return players

    @staticmethod
    def generatecharacters(names):
        ''' generate a character for each supplied name.'''

        HEALTH = (100, 300)
        HP = (10, 35)
        players = []
        for name in names:
            if rint(1,12) >= 12:
                players.append(Wizard(name, rint(HEALTH[0], HEALTH[1]), rint(HP[0], HP[1]),
                                      potions=[rint(30, 100), rint(10, 40), rint(10,20)]))
            else:
                players.append(Character(name, rint(HEALTH[0],HEALTH[1]), rint(HP[0], HP[1])))
        return players

    @staticmethod
    def battle(players):
        ''' conduct battle ( a serious of fights ) until all dead or there is one character left. '''

        round = 1
        while True:

            print('\n' + '-' * 30)
            print(f'Battle commences ...round {round}')

            picks = [player for player in players if player.alive()]
            fights = len(picks) // 2
            for _ in range(fights):
                fighter1 = picks.pop(randrange(len(picks)))
                fighter2 = picks.pop(randrange(len(picks)))
                Character.fight(fighter1, fighter2)

            print('-' * 30 + '\n')

            if Character.battleover(players): return
            round += 1

class Wizard(Character):

    def __init__(self,name, health, hitpoints, char_type='wizard', spells=[], potions=[]):
        Character.__init__(self, name, health, hitpoints, char_type)
        self.spells = spells
        self.potions = potions
        self.threshold = 50

    def __repr__(self):
        general = Character.__repr__(self)
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

print('\n'
      'Welcome to a simple little character battler\n'
      '\n'
      'A random selection of characters are created, with varying levels of health and hit power.\n'
      'Characters fight each other until one remains, or they all die.\n'
      '\n'
      'Let the fight commence ...\n'
      '\n')

NAMES = frozenset(['Fred', 'Bert', 'Sarah', 'Charlie', 'David', 'Kevin', 'Helen', 'Wendy', 'Steve', 'Tom', 'Linda'])

while True:
    names = Character.pickplayers(NAMES)
    players = Character.generatecharacters(names)
    Character.battle(players)

    if not input('Go again? ').strip().lower() in ['yes', 'y', 'ok', 'go', 'yeh', 'sure', 'please', 'k', 'si']:
        break

    del names
    del players
