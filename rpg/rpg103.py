from characters import wizards
from characters.characters import Character

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

while True:
    names = Character.pickplayers(NAMES)
    players = Character.generatecharacters(names)
    Character.battle(players)

    answer = input('Want another battel? ').strip().lower()
    if answer and answer not in AFFIRM:
        break

    del names
    del players