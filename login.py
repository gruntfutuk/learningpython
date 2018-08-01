class Test:
    a_var = 123

    def __init__(self):
        self.b_var = 456

    def __repr__(self):
        return f'{vars(self)}'

    def testinc(self):
        self.a_var += 1
        self.b_var += 1

x = Test()
y = Test()

print(f'x: {x}, y: {y}')
x.testinc()
y.testinc()
print(f'x: {x}, y: {y}')