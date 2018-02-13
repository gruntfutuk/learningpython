import operator
import regex

ops = {'+':  operator.add,
       '-':  operator.sub,
       '*':  operator.mul,
       '/':  operator.truediv,
       '//': operator.floordiv,
       '%':  operator.mod,
       '**': operator.pow,
       '<':  operator.lt,
       '<=': operator.le,
       '==': operator.eq,
       '!=': operator.ne,
       '>=': operator.ge,
       '>':  operator.gt
       }

pattern = f"\s*({'|'.join([regex.escape(pattern) for pattern in ops.keys()])})\s*"

while True:

    entered = input('\nEnter a simple expression: (or return to exit) ')
    if not entered:break

    expression = regex.split(pattern, entered)
    op = expression[1]
    num1 = int(expression[0])
    num2 = int(expression[2])

    if op in ops:
        try:
            answer = ops[op](num1, num2)
        except Exception as inst:
            print(f'** ERROR ** {inst}: expression:  {num1} {op} {num2}')
        else:
            return answer
    else:
       print("Invalid input")
