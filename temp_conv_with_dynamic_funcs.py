''' temperature conversion '''

def tempconv_F_to_C(temp):
    return (temp - 32) / 1.8

def tempconv_C_to_F(temp):
    return (temp * 1.8) + 32

def tempconv_Ré_to_C(temp):
    return temp * 5/4

def tempconv_C_to_Ré(temp):
    return temp * 4/5

def tempconv_Ré_to_F(temp):
    return tempconv_C_to_F(tempconv_Ré_to_C(temp))

def tempconv_F_to_Ré(temp):
    return tempconv_C_to_Ré(tempconv_F_to_C(temp))

# build dictionary of temperature conversion functions,
# (dropping from the keys the prefix of tempconv_ and removing the _ before and after to)
prefix = 'tempconv_'
prefix_len = len(prefix)
tempconv_funcs = {name[prefix_len:].replace('_to_', ' to '): func for name, func in globals().items()
                 if callable(func) and name.startswith(prefix)
                }
# define set of temperature units available
UNITS = set([unit for temp in [k.partition(' to ')
                for k in tempconv_funcs.keys()]
                for unit in temp if unit != ' to '])
ORIG = 'C'  # default original temp
NEW = 'F'  # default to convert to

def temp_convert(temp, orig, new):
    if not(isinstance(temp, int) or isinstance(temp, float)):
        raise ValueError('Valid temperature not provided')
    if not orig or not new:
        raise ValueError('Original and/or New units not specified')
    func = tempconv_funcs.get(f'{orig} to {new}')
    if not func:
        raise TypeError(f'No coversion available for {orig} to {new}')
    return func(temp)

print('Welcome to this temperature conversion programme\n')
print(f'The following units are accepted: {", ".join(UNITS)}')
print('and the following conversions:-', end='')
print('', *tempconv_funcs.keys(), sep='\n * ')

while True:  # do another conversion loop
    while True:  # get valid unit selections from user
        orig = input(f'What units to convert from? [{ORIG}]  ')
        if not orig:
            orig = ORIG
        new = input(f'What units to convert to? [{NEW if orig != NEW else ORIG}] ')
        if not new:
            new = NEW if orig != NEW else ORIG
        if orig != new and orig in UNITS and new in UNITS:
            break
        print(f'You need to select from the following units: {", ".join(UNITS)}')

    while True:  # get a numeric input for temperature
        try:
            temp = float(input(f'Temperature ({orig}): '))
            break
        except:
            print('Numeric value required')

    try:
        print(f'{temp:.2f} degrees {orig} is {temp_convert(temp, orig, new):.2f} degrees {new}')
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)

    if input('Another? [Yes/no] ').lower() not in ('y', 'yes', '1', 'yup', 'ok', ''):
        break