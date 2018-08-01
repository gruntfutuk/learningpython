import operator

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

x = 10
y = 5.0

for func in ops.values():
    try:
        answer = func(x, y)
    except Exception as inst:
        print(f'** ERROR ** {inst} with values for x, y of: {x}, {y}')
    else:
        print(answer)
