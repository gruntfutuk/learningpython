#!/usr/bin/env python3
''' simple programme to calculate largest demoninations of change for given value.

    uses a Money class with a dictionary of currencies (just sterling for now), with
    a nested dictionary for each currency listing value (as multiples of smallest base unit)
    paired with usual name for that value.
'''


import sys
from collections import OrderedDict

class Money:
    denominations = {'sterling':
        OrderedDict([
            (200, 'two pound'),
            (100, 'one pound'),
            (50, 'fifty pence'),
            (20, 'twenty pence'),
            (10, 'ten pence'),
            (5, 'five pence'),
            (2, 'two pence'),
            (1, 'one penny')
        ])
    }


    def __init__(self, name, amount=0, currency='sterling'):
        self.name = name
        self.amount = amount
        self.change = []
        if currency not in Money.denominations: currency = 'sterling'
        self.currency = currency

    def getamount(self):
        request = f'\nFor {self.name},' + \
                  f'\n\t what amount (in smallest whole {self.currency} denomination)' + \
                  f'\n\t do you want a breakdown of: ' + \
                  '\n\t (just enter on its own to exit)  ' + \
                  '---> '
        while True:
            response = input(request)
            if not response:
                self.amount = 0
                return
            if response.isnumeric():
                self.amount = int(response)
                return
            print('Sorry. That is not a valid amount of change. Please try again')

    def breakdown(self):
        self.change = []
        amount = self.amount
        for money in Money.denominations[self.currency].keys():

            if amount <= 0: return

            if amount >= money:
                self.change.append((amount // money, money, Money.denominations[self.currency][money]))
                amount = amount % money

    def __str__(self):
        if self.amount > 0:
            self.breakdown()
            output = f'\n\nChange for {self.name} {self.amount} {self.currency}\n'
            total = 0
            for quantity, money, desc in self.change:
                amount = quantity * money
                total += amount
                output += f'{quantity:2d} x {desc:15s} = {amount:3d} ->  {total:4d}\n'
        else:
            output('No change.')
        return output



if __name__ == "__main__":
    if not sys.argv[1:]:
        pocket = Money('your coin purse')
        while True:
            pocket.getamount()
            if pocket.amount:
                print(pocket)
            else:
                break
    elif sys.argv[-1] in ['-t', '--test']:
        # test a range of values
        from random import randint

        bottle = Money('old money jar')
        for _ in range(0, randint(10, 50)):
            bottle.amount = randint(0, 999)
            print(bottle)
    else:
        print('Uknown command line arguments')