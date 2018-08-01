#b_file.py
import pdb
pdb.set_trace()
print('executing b_file')
from a_file import z
print(f'finished importing a_file, so z = {z}')
x = 5 + z
print(f'finished b file, so x = {x}')
