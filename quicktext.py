breakpoint()
from random import randint
total = 0
for count in range(10):
    total += randint(1, 100) * count
print(total)
