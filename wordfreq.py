''' simple programme to count frequency of words
    in a set if lyrics
'''

from typing import Dict, List

def count_word_frequency(words: List[str]) -> Dict[str, int]:
    """Count the frequency of words in list of words and
    return frequency table in a dictionary of words (key)
    and counts

    :param words: list of words
    :return: dictionary of frequency count
    """

    freq_table : Dict[str, int] = dict()
    for word_mixcase in words:
        word = word_mixcase.lower()
        if freq_table.get(word):
            freq_table[word] += 1
        else:
            freq_table[word] = 1
    print(freq_table)
    return freq_table

def test():
    def obtain_lyrics(filename=''):
        if not filename:
            lyrics = """
I found a love for me
Darling just dive right in
And follow my lead
Well I found a girl beautiful and sweet
I never knew you were the someone waiting for me
'Cause we were just kids when we fell in love
Not knowing what it was
I will not give you up this time
But darling, just kiss me slow, your heart is all I own
And in your eyes you're holding mine
Baby, I'm dancing in the dark with you between my arms
Barefoot on the grass, listening to our favorite song
When you said you looked a mess, I whispered underneath my breath
But you heard it, darling, you look perfect tonight
Well I found a woman, stronger than anyone I know
She shares my dreams, I hope that someday I'll share her home
I found a love, to carry more than just my secrets
"""
            return lyrics
        else:
            pass  # add reading lyrics from file later

    lyrics_org = obtain_lyrics()
    lyrics_org = lyrics_org.replace(",","")
    lyrics = lyrics_org.split()

    freqtable = count_word_frequency(lyrics)

    print('\n\nLyrics word frequency table, alphabatical:\n')
    for key in sorted(freqtable.keys()):
        print (f"{key}: {freqtable[key]}")

    print('\n\nLyrics word frequency table, by frequency:\n')
    for word, freq in sorted(freqtable.items(), key = lambda x: (x[1], x[0])):
        print (f"{word}: {freq}")


if __name__ == "__main__":
    test()
