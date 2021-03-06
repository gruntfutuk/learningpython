''' A simple character battle game '''

from random import randint as rint
from random import randrange

class Character:

    def __init__(self, name, health, hitpoints):
        self.name = name
        self.hitpoints = hitpoints
        self.health = health
        print(self)

    def __repr__(self):
        return f'{self.name:>7} ({self.health:3d}) [{self.hitpoints:3d}]'

    def combat(self, woundpoints):
        ''' adjust health of character based on woundpoints inflicted '''

        self.health -= woundpoints
        if self.health < 0: self.health = 0

    def alive(self):
        ''' confirm if character is still alive'''

        return self.health > 0

    @staticmethod
    def fight(player1, player2):
        ''' determine outcomes of fight between two characters '''

        print(f'... {player1.name} and {player2.name} fight')
        player2.combat(player1.hitpoints)
        player1.combat(player2.hitpoints)

    @staticmethod
    def result(*players):
        ''' output status of characters that are still alive '''

        alive = []
        for player in players:
            if player.alive():
                alive.append(player.name)
                print(player)
        return alive

    @staticmethod
    def battleover(players):
        ''' output status of players alive, and determine if battle has finished '''

        alive = Character.result(*players)
        if alive == []: print('\n\n** Everyone died **\n\n')
        elif len(alive) == 1: print(f'\n\n** WINNER: {alive[0]} **\n\n')
        return len(alive) <= 1

    @staticmethod
    def pickplayers(NAMES):
        ''' given list of potential character names, just all or some to become characters in battle '''

        picks = list(NAMES)
        players = []
        for _ in range(rint(2, len(NAMES))):
            players.append(picks.pop(randrange(len(picks))))
        return players

    @staticmethod
    def generatecharacters(names):
        ''' generate a character for each supplied name '''

        HEALTH = (100, 300)
        HP = (10, 35)
        players = []
        for name in names:
            players.append(Character(name, rint(HEALTH[0],HEALTH[1]), rint(HP[0], HP[1])))
        return players

    @staticmethod
    def battle(players):
        ''' conduct battle ( a serious of fights ) until all dead or there is one character left '''

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

print('\n'
      'Welcome to a simple little character battler\n'
      '\n'
      'A random selection of characters are created, with varying levels of health and hit power.\n'
      'Characters fight each other until one remains, or they all die.\n'
      '\n'
      'Let the fight commence ...\n'
      '\n')

NAMES = frozenset(['Fred', 'Bert', 'Sarah', 'Charlie', 'David', 'Kevin', 'Helen', 'Wendy', 'Steve', 'Tom', 'Linda'])
names = Character.pickplayers(NAMES)
players = Character.generatecharacters(names)
Character.battle(players)