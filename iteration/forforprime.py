#!/usr/bin/env python #!/usr/bin/env python


def isprime(n):
    # return true if n is a prime number
    if n <= 1:
        return False
    if n in [2, 3]:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    # algorithmic check
    i = 5
    w = 2

    while i * i < n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w

    return True


def primes(low, high):
    for num in range(low, high):
        if isprime(num):
            yield num


for n in primes(1, 10000):
    print("{:6d}".format(n), end="\t")
print("\n")
