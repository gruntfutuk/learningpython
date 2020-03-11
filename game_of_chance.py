from numpy.random import choice  # better than random.choice, need numpy installed

# set starting conditions: money_pot, high, low, ratio
money_pot, too_high, too_low, ratio = 100, 1000, 0, 50
odds = [1 * ratio / 100, 1 * (100 - ratio) / 100]
# start a counter
counter = 0

#start a while loop to play until money_pot equals or exceeds high or low marks
while too_low < money_pot < too_high:
    # get stake from user (validate to make sure can afford)
    while True:
        try:
            stake = float(input(f'Pot: £{money_pot:.2f}, odds: {ratio}:{100-ratio}, your stake: £'))
            if stake > money_pot:
                print('Sorry, not enough money.')
            else:
                break
        except ValueError:
            print('Sorry, do not understand that as a stake')

    # use random.choice to pick win/lose
    win = choice([True, False], p=odds)  # numpy.choice lets us provide probability weights
    # increment counter
    counter += 1
    # apply outcome
    change = stake * 2 if win else -stake
    money_pot += change
    print(f"{'Well done, won' if win else 'Bad luck, lost'} £{abs(change):.2f}")

print(f'Game over, final balance: £{money_pot:.2f}, plays: {counter}')
