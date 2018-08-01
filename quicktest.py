num = int(input())
for i in range(num, -1, -1):
    print(" " * i + "*" * ((num - i) * 2 + 1))
for i in range(1, num + 1):
    print(" " * i + "*" * ((num - i) * 2 + 1))
for i in range(num * 2 + 1):
    print("*" * (num * 2 + 1))
for i in range(num, -1, -1):
    print(" " * i + "*" * ((num - i) * 2 + 1))
for i in range(1, num + 1):
    print(" " * i + "*" * ((num - i) * 2 + 1))
