import pdb
pdb.set_trace()
print('Starting a_file ...')
z=3
from b_file import x
print(f'just imported b_file, so x = {x} and z = {z}')
g = x + x
print(f'g = {g}')
print('finished a_file')
