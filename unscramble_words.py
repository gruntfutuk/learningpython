''' based on a hacker rank challenge to unscramble several words the originals of which are held in a longer list of words supplied in a file '''

from random import shuffle
from random import choice


def generate_scrambled_words(quantity=10):
    ''' substitute for hacker rank generated scrambled word list '''

    def scramble_words(word_list, quantity):
        ''' return list of <quantity> scrambled words randomly chosen from <wordlist> '''

        def scramble(word):
            ''' returns string with character order randomly shuffled'''
            scrambled = list(word)
            shuffle(scrambled)
            return ''.join(scrambled)

        scrambled_words = []
        for _ in range(quantity + 1):
            while True:
                word = choice(word_list)
                scrambled_word = scramble(word)
                if scrambled_word not in scrambled_words:
                    break
            scrambled_words.append(scrambled_word)
        return scrambled_words

    def read_words_from_file():
        ''' read file of words '''
        with open('wordlist.txt', 'r') as f:
            # sorted string versions of words (keys), with original words (values)
            word_list = [word.strip() for word in f]
        return word_list

    word_list = read_words_from_file()
    scrambled_words = scramble_words(word_list, quantity)
    return scrambled_words


def solve_scrambled_words(scrambled_words):
    ''' return list of unscrambled words for supplied scrambled words '''

    def read_words_from_file():
        ''' read file of words '''
        with open('wordlist.txt', 'r') as f:
            # sorted string versions of words (keys), with original words (values)
            word_dict = {}
            for word in f:
                sorted_word = ''.join(sorted(word.strip()))
                if not word_dict.get(sorted_word):
                    word_dict[sorted_word] = word.strip()
        return word_dict

    word_dict = read_words_from_file()

    unscrambled_words = []

    for scrambled in scrambled_words:
        sorted_scrambled = ''.join(sorted(scrambled))
        found = word_dict.get(sorted_scrambled, '** not found **')
        unscrambled_words.append(found)
    return unscrambled_words


def main():

    scrambled_words = generate_scrambled_words()
    unscrambled_words = solve_scrambled_words(scrambled_words)
    print(f"\n\nWords to unscramble are: {', '.join(scrambled_words)}:\n")

    for scrambled, unscrambled in zip(scrambled_words, unscrambled_words):
        print(f'{scrambled} = {unscrambled}')


if __name__ == "__main__":
    main()
