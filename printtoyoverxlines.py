#!/usr/bin/python3
#
# given x and y, print the number series 0 to y over x lines

y = int(input('What number should be printed from 0 to: ')
x = int(input('Over how many lines: '))

if x < 1 or y < 1 or y < x:
        print('Sorry, that is not a feasible range.')

numperlines = y // x
        for num in y+1:

