import sys

def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args)

print(foo(*sys.argv[1:]))
