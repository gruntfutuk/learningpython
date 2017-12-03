#!/usr/bin/env python3
# create a matrix of random numbers, print out only even ones

import random

width = 5
height = 6


def createmat(width, height, low, high):
    return [[random.randint(low, high)
             for x in range(width)] for y in range(height)]


def evens(stream):
    for x in stream:
        if x % 2 == 0:
            yield x


def flat(mat):
    for row in mat:
        for cell in evens(row):
            yield cell


nums = createmat(width, height, 1, 100)
print(nums)

for x in flat(nums):
   print(x, end=", ")

print('')
