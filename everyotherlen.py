#!/usr/bin/python3
#
# reads every other line from text file and tells
# you the line length

from itertools import islice

with open('alpha.txt') as fd:
    lines = islice(fd, 0, None, 2)
    for line in lines:
        print(len(line.rstrip()))
