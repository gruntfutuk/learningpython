#!/usr/bin/python3
#
# input three numbers and sort them into ascending order without using any
# built in sorting functions


def getlist():
    nums = []
    while len(nums) < 3:
        num = input('Enter a whole positive number: ')
        if num.isdecimal():
            nums.append(int(num))
        else:
            print(f'{num.rstrip()} is  not a whole positive number.')
    return(nums)


def threeswap(l, i):  # swap ith and i+1th elements in list l
    l[i:i+1], l[i+1:i+2] = l[i+1:i+2], l[i:i+1]
    return l

def threesort(three):
    if three[0] <= three[1]:
        if three[1] <= three[2]:
            return
        else:
            threeswap(three, 1)
    else:
        threeswap(three, 0)
    threesort(three)


threelist = getlist()
threesort(threelist)
print(f'smallest: {threelist[0]}, mid: {threelist[1]}, largest: {threelist[2]}')
