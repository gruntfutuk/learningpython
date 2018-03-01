import string

def base_to_dec(basestr, base=2):
    if not 2 <= base <= 36:
        raise ValueError(f'{base} out of range base range 2 - 36')
    dec = 0
    digits = string.digits + string.ascii_uppercase
    digits = digits[:base]
    for power, digit in enumerate(basestr[::-1]):
        if digit not in digits:
            raise ValueError(f'({digit} is not a valid digit in base {base}.)')
        
        dec += digits.find(digit) * base**power
    return dec

print(base_to_dec('00111011'))
print(base_to_dec('77',8))
k=base_to_dec
p=print
p(k('5Z78',18))

        
