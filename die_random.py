"""
Random numbers
Probability of a die roll

It is possible to mathematically predict the probability (or chance) of getting a
certain die roll; however, in this exercise you will use Python to do it without
math. The trick is to roll a die a large number of times and count how many
times we get a certain roll. You can, then, divide the count by the large number
to get the probability. For a fair 6-sided die, the chance of getting any of its
faces is about 16.6%
"""

# [ ] Complete the following program to display the probability of a certain
# die roll

from random import randint
from collections import defaultdict
from collections import OrderedDict

# This dictionary will contain the total number of times a given number is rolled
rolls = defaultdict(int)

def die_roller():
    ''' return random digit from 1-6 '''
    return (randint(1, 6))

range_max = 200
for _ in range(0, range_max):
    rolls[die_roller()] += 1

rolled = OrderedDict(sorted(rolls.items(), key=lambda x: x[0]))
for num, count in rolled.items():
    print(f"{num} rolled {count} times, {count / range_max * 100: .2f} % of the time.")



