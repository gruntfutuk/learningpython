# get student scores from user
# output the second lowest score (first instance)
# ignoring equal lowest scores

from operator import itemgetter
from collections import namedtuple

NameScore = namedtuple('NameScore', 'name score')
scoretable = []

while True:
    name = input('Name of student (return to exit): ')
    if name:
        score = float(input(f'{name}\'s score: '))
        scoretable.append(NameScore(name, score))
    else:
        break

if len(scoretable) > 1:
    scoretable = sorted(scoretable, key=itemgetter(1))

    lowest = scoretable[0].score
    low2nd = lowest
    if len(scoretable) > 1:
        for name, score in scoretable[1:]:
            if score > lowest:
                if score > low2nd and low2nd > lowest:
                    break
                print(f'2nd lowest: {name} {score}')
                low2nd = score
        else:
            if low2nd == lowest: print('Everyone had same mark')
else:
    print('Insufficient entries')