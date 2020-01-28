from time import sleep
print('hello')
for i in range(1, 10 + 1):
    print(f'\r{i}', end='')
    sleep(1)
print()
