'example code that is run by another python scipt called runner.py'
'programme will be re-invoked if it halts for any reason other than'
'the exit code 101 option indicated below'

import sys

while True:
    num = int(input('Number: (>= 10 to exit) '))
    print(num * 2)
    if num > 9:
        sys.exit(101)
