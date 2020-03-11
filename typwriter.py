import time
import sys

text = '''This is a line of characters that I would like to running word by word'''

for letter in text:
    print(letter, end='')
    sys.stdout.flush()
    time.sleep(.1)
print()
