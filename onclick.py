''' simple console based hangman game v3.2'''

import random
import string
import textwrap


def welcomeScreen():
    ''' captures player's name, prints welcome msg and returns name '''

    while True:
        name = input("\nEnter Your Name: ")
        if name:
            break

    print(f"\nWelcome, {name}, to your very own hangman game!")
    print("Try to guess what is the cause of victim's death or you'll hang.")
    print("Let the game begin!")

    return name


def hangman(gallows, name='Player'):
    ''' core game logic '''

    def getguess():
        ''' display input prompt and return valid input of letter or word guess
            reject inputs of: invalid characters, letters already tried, return
            on its own, and word guesses of wrong length '''

        template = ' ' + ' '.join(c for c in msg) + ' '
        guesses_out = ','.join(guess for guess in guesses)
        while True:
            print(f"\nGuess the word: {template}")
            print(f"[Tried: {guesses_out} ]")
            print()

            while True:
                guess = input('Your letter/word guess (or exit)?').lower()
                if guess:
                    break
            if guess == 'exit':
                break
            guesslen = len(guess)
            if guesslen != len(word) and guesslen > 1:
                print(f'{guess} is wrong length for a word guess.')
            else:
                if guess in guesses:
                    print(f"You've already tried {guess}.")
                elif set(guess).issubset(VALID):
                    break
                else:
                    print(f"{guess} is not a valid letter or word.")

        return guess

    word = random.choice(
        ['Burning', 'Choking', 'Hanging', 'Suffocation',
         'Drowning', 'Poisoning', 'Burial', 'Decapitation',
         'Electrocution', 'Crushing', 'Explosion',
         'Starvation', 'Dehydration', 'Crucifixion',
         'Decompression', 'Radiation', 'Boiling']).lower()
    msg = '_' * len(word)
    VALID = string.ascii_letters
    guesses = []
    tries = 10
    found = False

    while not found and tries:

        guess = getguess()
        if guess == 'exit':
            break
        guesses.append(guess)

        if guess in word:
            if len(guess) == 1:
                msg = ''.join([c if c in guesses else '_' for c in word])
                found = msg == word
            else:
                found = True
            print('Good find.')
        else:
            tries -= 1
            print(textwrap.dedent(gallows[tries]))

    else:
        print()
        if found:
            print(f"You are correct, {name}.")
            print(f"The word is: {word}.\n")
        else:
            print(f"You just hung to death, {name}.")
            print("Game Over!\n")


def yesno(question):
    ''' return True/False for affirmation/rejection response to supplied question '''
    AFFIRMATION = frozenset({'y', 'yey', 'yes', 'ok', '1', 'oui', 'si'})
    REJECTION = frozenset({'n', 'nah', 'no', 'nope', '0'})
    while True:
        while True:
            response = input(question).lower()
            if response:
                break
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
