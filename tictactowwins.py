''' generate all tic tac tow winning positions '''
from collections import namedtuple

Pos = namedtuple('Pos', 'row col')
pos = Pos(row=0, col=0)
board = [[0 for _ in range(3)] for _ in range(3)]
print(board)

for row in range(3):
    for col in range(3):
        01   02  03
