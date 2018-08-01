import sys
if sys.argv[1:] and sys.argv[1].isdigit():
    N = int(sys.argv[1])
else:
    N = 0
if N > 0:
    myList = [i * 10 for i in range(1, N + 1)]
else:
    myList = []

print(myList)
