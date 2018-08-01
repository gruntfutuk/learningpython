''' simple console based hangman game '''

import random
import string
import textwrap


def welcomeScreen():
    name = input("\nEnter Your Name: ")
    print(name)
    print(f"Welcome, {name}, to your very own hangman game!")
    print("Try to guess what is the cause of victim's death or you'll hang.")
    print("Let the game begin!")
    return(name)


def hangman(gallows, name='Player'):
    word = random.choice(
        ['Burning', 'Choking', 'Hanging', 'Suffocation',
         'Drowning', 'Poisoning', 'Burial', 'Decapitation',
         'Electrocution', 'Crushing', 'Explosion',
         'Starvation', 'Dehydration', 'Crucifixion',
         'Decompression', 'Radiation', 'Boiling'])
    wordlower = word.lower()
    valid = string.ascii_letters
    guess = msg = expect = ''
    tries = 10
    while True:
        if expect and expect.lower() == wordlower:
            found = True
        elif guess:
            guesslower = guess.lower()
            msg = ''.join([c if c in guesslower else '_' for c in wordlower])
            found = msg.lower() == wordlower
        else:
            msg = '_' * len(word)
            found = False
        if found:
            print(f"You are correct, {name}.")
            print(f"The word is: {word}.\n")
            break
        template = '|' + '|'.join(c for c in msg) + '|'
        while True:
            print(f"\nGuess the word: {template}")
            if guess:
                print(
                    f"(letters tried so far: {guess})")
            expect = input('Enter a letter or word guess: ')
            if len(expect) > 1 and set(expect).issubset(valid):
                break  # tried to guess word
            elif expect and expect in guess:
                print(f"You've already tried {expect}")
                continue
            elif expect and expect in valid:
                guess = guess + expect
                break
            else:
                print(f"{expect} is not a valid letter or the word: ")
        if expect.lower() in word.lower():
            print("Good guess.")
        else:
            tries -= 1
            print(textwrap.dedent(gallows[tries]))
            if tries == 0:
                print()
                print(f"You just hung to death, {name}.")
                print("Game Over!\n")
                break


def yesno(question):
    AFFIRMATION = frozenset({'y', 'yey', 'yes', 'ok', '1', 'oui', 'si'})
    REJECTION = frozenset({'n', 'nah', 'no', 'nope', '0'})
    while True:
        response = input(question).lower()
        if response in REJECTION:
            return False
        if response in AFFIRMATION:
            return True
        print('I\'m sorry, I didn\'t understand that')


def build_gallows():
    return {9: r'''

                |\
                ''',
            8: r'''
                |
                |
                |
                |
                |\
                ''',
            7: r'''
                ________
                |/
                |
                |
                |
                |\
                ''',
            6: r'''
                ________
                |/     |
                |
                |
                |
                |\
                ''',
            5: r'''
                ________
                |/     |
                |      O
                |
                |
                |\
                ''',
            4: r'''
                ________
                |/     |
                |      O
                |     /
                |
                |\
                ''',
            3: r'''
                ________
                |/     |
                |      O
                |     /|
                |
                |\
                ''',
            2: r'''
                ________
                |/     |
                |      O
                |     /|\
                |
                |\
                ''',
            1: r'''
                ________
                |/     |
                |      O
                |     /|\
                |     /
                |\
                ''',
            0: r'''
                ________
                |/     |
                |      O
                |     /|\
                |     / \
                |\
                '''
            }


def main():
    gallows = build_gallows()
    name = welcomeScreen()
    while True:
        hangman(gallows, name)
        if not yesno(f'Would you like to play again, {name}? '):
            break


if __name__ == "__main__":
    main()
