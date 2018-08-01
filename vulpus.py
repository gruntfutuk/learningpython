import random

class Monster:
    name = 'Monster'
    hp = 5
    mp = 5

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp


monsters = [Monster(name='wolf',
                    hp=10,
                    mp=10
                    ),
            Monster(name='bear',
                    hp=11,
                    mp=11
                    ),
            Monster(name='hawk',
                    hp=9,
                    mp=9
                    ),
            Monster(name='rat',
                    hp=8,
                    mp=9
                    ),
            Monster(name='cobra',
                    hp=12,
                    mp=9
                    ),
            Monster(name='goblin',
                    hp=16,
                    mp=12
                    ),
            Monster(name='giant rat',
                    hp=9,
                    mp=7
                    ),
            Monster(name='bugbear',
                    hp=14,
                    mp=14
                    )
            ]

def selection(monsters):

    selections = []
    for length in range(1,5):
        selections.append([random.choice(monsters) for _ in range(length)])
    selector = random.choice(selections)
    for monster in selector:
        print(f"name: {monster.name}\nhp: {monster.hp}\nmp: {monster.mp}")

selection(monsters)