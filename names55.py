"""simple arithmetic calulator"""

print("""

Welcome to my simple calculator.

This supports integer and floating point numbers and the four basic
arithmetic operators.

Please enter the operator symbol for the operation required, or
just a blank entry to quit.
"""
)
def get_num(msg):
    """return an int or float input"""
    while True:
        entry = input(msg)
        num = None
        try:
            num = float(entry)
            num = int(entry)
        except ValueError:
            if not num is None:
                return num
        print('Invalid input, please enter a number (integer or float).')

def do_plus(op1, op2):
    return f'{op1} + {op2} = {op1 + op2}'

def do_minus(op1, op2):
    return f'{op1} - {op2} = {op1 - op2}'

def do_times(op1, op2):
    return f'{op1} x {op2} = {op1 * op2}'

def do_div(op1, op2):
    try:
        return f'{op1} / {op2} = {op1 / op2}'
    except ZeroDivisionError:
        return 'Divide by zero error'


OPS = {'+': do_plus, '-': do_minus, '*': do_times, '/': do_div,
        'x': do_times, '÷': do_div}


while True:
    print()
    op = input('Op: ').strip()
    if not op:
        break
    if op in OPS:
        op1 = get_num('Enter first operand: ')
        op2 = get_num('Enter second operand: ')
        result = OPS[op](op1, op2)
        print(result)
    else:
        print(f'invalid operator, use one of {" ".join(OPS)}')

print('Thank you for using this calculator\n')