from random import randint

class Dice:
    rolls = 0
    rolled = []

    @staticmethod
    def roll():
        return randint(1, 6)

    @staticmethod
    def roll2():
        return Dice.roll() + Dice.roll()


    def rollmydice(self):
        self.rolls += 1
        self.rolled.append(self.roll2())
        return self.rolled[-1]


    def rollanum(self, num = 12):
        self.clear()
        while self.rollmydice() != num: continue
        return self.rolled[-1]


    def rollatleast(self, num = 12):
        self.clear()
        while self.rollmydice() < num: continue
        return self.rolled[-1]

    def clear(self):
        self.rolls = 0
        self.rolled = []

print('\nrolls using class')
print(f'basic roll: {Dice.roll()}')
print(f'double roll: {Dice.roll2()}')

print('\nrolls using instance')
d1 = Dice()
print(f'd1 basic roll: {d1.roll()}')
print(f'd1 double roll: {d1.roll2()}')

print('\nrolls using instance, with targets')
print('Type  Rolled  Roll(s)  History')
for _ in range(5, 20):
    print(f'==\t\t{d1.rollanum(randint(2, 12)):2d}\t\t{d1.rolls:3d}\t\t{d1.rolled}')
    print(f'>= \t\t{d1.rollatleast(randint(2, 12)):2d}\t\t{d1.rolls:3d}\t\t{d1.rolled}')

print('\n\n++ FINISHED ++')