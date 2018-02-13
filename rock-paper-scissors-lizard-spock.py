#!/usr/bin/python3

# simple text version of the Rock Paper Scissors Lizard Spock game
# http://bigbangtheory.wikia.com/wiki/Rock_Paper_Scissors_Lizard_Spock

# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
#   0 - rock
#   1 - Spock
#   2 - paper
#   3 - lizard
#   4 - scissors

# Each player picks a "hand-shape", then all players reveal their choices at the same time.
# The winner is the one who defeats the others. The rules of rock-paper-scissors-lizard-Spock
# are described in the rules dictionary, winning weapon > losing weapon : reason

# Given two weapon choices, a and b (that are different)
# the winner can be determined by (a-b) %5 < 3
# (i.e. the remainder after divion by 5 is less than 3)
# a wins if True, b wins if False

def main():

    import random

    def whowins(player, computer):
        # Determines who wins; uses a calculation on indexes to figure it out
        if player == computer:
            return 'Tie', "great minds think alike (as the saying goes)."
        elif (weaponsnames[player] - weaponsnames[computer]) % 5 < 3:
            return 'Player', reasoning(player, computer)
        else:
            return 'Computer', reasoning(computer, player)

    def reasoning(winner, loser):
        # generate explanation of how the game was won
        action = rules[f'{winner}>{loser}']  # look up the rule using the key
        return f'{winner} {action} {loser}'  # return explanation

    def player_input():
        # remind player of weapon choices, and get choice (or exit option)
        while True:
            player = input(f"\nEnter your choice {weaponschoices}\n  (or enter to exit): ")
            if player in weaponsinits:
                player = weaponsinits[player]
            if not player or player in weapons:
                break
            print(f"{player} is not valid. Try again.")
        return player


    # dictionary used for weapons, index values used to calculate winner
    weaponsindex = {0: 'rock', 1: 'Spock', 2: 'paper', 3: 'lizard', 4: 'scissors'}
    weaponsnames = dict((v, k) for k, v in weaponsindex.items())
    weapons = list(weaponsindex.values())
    weaponschoices = '/'.join(weapons)
    weaponsinits = {weapon[0]: weapon for weapon in weapons}  # initial character of weapon - should be unique
    scores = {'Player': 0, 'Computer': 0, 'Tie': 0}
    # rules & user input are case sensitive, because I couldn't be bothered to address
    rules = {"scissors>paper": "cut",
             "paper>rock": "covers",
             "rock>lizard": "crushes",
             "lizard>Spock": "poisons",
             "Spock>scissors": "smashes",
             "scissors>lizard": "decapitate",
             "lizard>paper": "eats",
             "paper>Spock": "disproves",
             "Spock>rock": "vaporizes",
             "rock>scissors": "crushes"
             }

    print('\n\nWelcome to our rock-paper-scissors-lizard-Spock game\n\n')

    round = 1
    winners = []
    while True:
        computer = random.choice(weapons)
        player = player_input()
        if not player:
            break
        winner, reason = whowins(player, computer)
        winners.append((winner, reason))

        scores[winner] += 1
        print(f"\nRound {round:2d}.")
        print(f"  You chose: {player}, Computer chose: {computer}.")
        print(f"  Winner: {winner} because {reason}")
        round += 1

    print(f"\n\nTotal scores: You: {scores['Player']}, Computer: {scores['Computer']}, Ties: {scores['Tie']}\n\n")
    if winners:
        print('\Table of winners:\n')
        heading = f"{'Winner':^10}   Result"
        print(heading,'\n', "-" * len(heading))
        for round in winners:
            print(f'{round[0]:^10}: {round[1]}')


# usually would have if __name__ == "__main__": to call main()
# but it doesn't work on repl.it
main()
