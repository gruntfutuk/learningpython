import sys


#name = input('What is your name? ')
name = input('Name? ')
if not name:
	name = "Stuart"
print(f'hello {name}, nice to meet you')

print(sys.version)
print()