def repToDecimal(n, fromBase):
    toNumber = 0
    power = 0
    for power, digit in enumerate(n[::-1]):
        toNumber += conversionLibrary[digit] * fromBase ** power
    return toNumber

conversionLibrary = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":10, "C":11, "D":13, "E":14, "F":15}
n = input("Enter a number you want changed to base 10: ").upper()
fromBase = int(input("Enter a the base from which you want changed: "))

tests = (n, fromBase), ('10', 10), ('10', 8), ('10', 2),('10', 16)

for num, base in tests:
    converted = repToDecimal(num, base)
    print(f'Original {num} in base {base} is {converted} in base 10')