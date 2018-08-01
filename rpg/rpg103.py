''' This rpg is a very basic game under development as a learning exercise.

It is primarily intended to explore the use of classes and subclasses and an
OOPS approach generally.
'''

from random import randint as rint, randrange

from characters.common import Character
from characters.wizards import Wizard
from characters.people import People
from characters.monsters import Monster

print('\n'
      'Welcome to a simple little character battler\n'
      '\n'
      'A random selection of characters are created, with varying levels of health and hit power.\n'
      'Characters fight each other until one remains, or they all die.\n'
      '\n'
      'Let the fight commence ...\n'
      '\n')

NAMES = frozenset(['Fred', 'Bert', 'Sarah', 'Charlie', 'David', 'Kevin', 'Helen', 'Wendy', 'Steve', 'Tom', 'Linda'])
AFFIRM = frozenset(['yes', 'y', 'yup', 'ok', 'go', 'yeh', 'sure', 'please', 'k', 'si'])

def battleover(players):
    ''' output status of players alive, and determine if battle has finished. '''

    alive = result(*players)
    if alive == []: print('\n\n** Everyone died **\n\n')
    elif len(alive) == 1: print(f'\n\n** WINNER: {alive[0]} **\n\n')
    return len(alive) <= 1


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


def fight(player1, player2):
    ''' determine outcomes of fight between two characters. '''

    print(f'... {player1.name} and {player2.name} fight')
    player2.combat(player1.hitpoints)
    player1.combat(player2.hitpoints)


def pickplayers(NAMES):
    ''' given list of potential character names, choose all or some to become characters in battle. '''

    picks = list(NAMES)
    players = []
    for _ in range(rint(2, len(NAMES))):
        players.append(picks.pop(randrange(len(picks))))
    return players


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
            fight(fighter1, fighter2)

        print('-' * 30 + '\n')

        if battleover(players): return
        round += 1

testing = True
while True:
    names = pickplayers(NAMES)
    players = generatecharacters(names)
    battle(players)

    if testing: break  # not going to go around again whilst testing

    answer = input('Want another battel? ').strip().lower()
    if answer and answer not in AFFIRM:
        break

    del names
    del players