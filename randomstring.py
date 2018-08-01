''' random string functions: randstr(n) returns n characters (ascii_letters & digits) '''

import random
import string


def randstr(length=12, initletter=True):
    ''' return random string/filename (might not be unique) of n length'''

    if not isinstance(initletter, bool):
        raise TypeError('second argument must be boolean True or False, or absent')
    if not isinstance(length, int):
        raise TypeError('first argument must be positive integer or absent (defaults to 12)')
    if length < 1:
        raise ValueError('first argument must be positive integer or absent (defaults to 12)')

    CHARS = string.ascii_letters + string.digits

    if initletter:
        initial = random.choice(string.ascii_letters)
    else:
        initial = random.choice(CHARS)
    if length == 1:
        return initial

    return initial + ''.join(random.choice(CHARS) for _ in range(length - 1))