def is_prime(x):
    '''test if argument is a prime number, return True or False'''

    if not isinstance(x, int): raise TypeError("argument must be positive integer")
    if x < 1:raise ValueError("argument must be positive integer")

    if x == 1: return False
    if x % 2 == 0: return x == 2

    maxdiv = int(x**0.5) + 1 # math.sqrt would be slightly faster once math imported
    # only check devisors up to square root of argument, and only odd numbers
    for i in range(3, maxdiv, 2):
        if x % i == 0:
            return False
    return True
