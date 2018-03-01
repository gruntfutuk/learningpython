''' basic number conversion functions.'''

import string

def anybase_to_dec(basestr, base=2):
    ''' converts a string holding a number in any base 2 - 36 to decimal.

    Args:
        basestr (str): string of digits (0-9A-Z) of number in the specified base
        base (int): number base to be used, defaults to 2 for binary

    Returns:
        dec: the decimal equivalent of passed number in specific base.

    '''
    if not isinstance(basestr, str):
        raise TypeError('Number for conversion must be supplied as a string')
    if not isinstance(base, int):
        raise TypeError('Base to convert from to a decimal must be an integer in the range 2 - 36')
    if not 2 <= base <= 36:
        raise ValueError(f'{base} out of range base range 2 - 36')

    if len(basestr) > 2:
        basecodes = {'0b': 2, '0o': 8, '0x': 16}
        basecode = basestr[:2]
        if basecode in basecodes:
            checkbase = basecodes[basecode]
            if not base == checkbase:
                raise ValueError(f'Base requested, {base}, and base code in string, {checkbase}, do not match.')
            basestr = basestr[2:]

    decimalmark = '.'
    decimalsep = ','
    if decimalmark in basestr:
        raise TypeError('Only integer values can be handled')

    dec = 0
    digits = (string.digits + string.ascii_uppercase)[:base]
    for digit in basestr:
        if digit in [' ', '_', decimalsep]:
            pass
        else:
            if digit.upper() not in digits:
                raise ValueError(f'({digit} is not a valid digit in base {base}.)')
            dec *= base
            dec += digits.find(digit.upper())
    return dec