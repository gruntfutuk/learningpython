import sys
from collections import defaultdict as dd

string = str(sys.argv[1])

count_c = dd(int)

prev_c = string[0]
count_c[prev_c] = 1
for curr_c in string[1:]:
    if curr_c != prev_c:
        print(f'{prev_c}: {count_c[prev_c]}')
        count_c[prev_c] = 0
        prev_c = curr_c
    count_c[curr_c] += 1

