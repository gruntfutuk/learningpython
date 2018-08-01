''' Simple menu system using a dictionary as a case/switch alternative. '''

print('\n\nSimple menu example - Python approach to switch/case\n\n')

menu = {}  # name must exist for definitions


def menuprint():
    print('\nMenu options:\n')
    for option, action in menu.items():
        print(option, action[0])
    print()


def menuround(func=None):
    def menuandgo(*args, **kwargs):
        func(args, kwargs)
        menuprint()
        return True

    return menuandgo


@menuround
def one(*args, **kwargs):
    print('You chose option 1. Singular choice.')


@menuround
def two(*args, **kwargs):
    print('You chose option 2. Two\'s company.')


@menuround
def three(*args, **kwargs):
    print('You chose option 3. Three\'s a crowd.')


def ender(*args, **kwargs):
    print('You chose option x. Farewell.')
    return False


@menuround
def huh(*args, **kwargs):
    print('Sorry, don\'t know that option.')
    return True


# update dictionary with options and corresponding functions
menu['1'] = ('One', one)
menu['2'] = ('Two', two)
menu['3'] = ('Three', three)
menu['x'] = ('eXit', ender)

menuprint()

while menu.get(input('Your choice: ').lower(), ('huh', huh))[1](): pass