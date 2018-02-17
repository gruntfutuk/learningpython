import regex
import operator

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



repattern = regex.compile("""
                 \s*                # Ignore leading whitespace
                 (                  # Group the result, which is either ...
                  (?<!\d)-?         # A possibly negative (but not the operator minus)
                  \d+               # number
                  (?:\.\d+)?        # with optional fraction part
                 |                  # ... or alternate group of ...
                   (?://|\*\*)      # Non-capturing single operator
                   |(?:[+-/*^])     # or two-character operator group
                 )                  # ... end of group
                 \s*                # Ignore trailing whitespace
                 """, regex.X)

# pattern = f"\s*({'|'.join([regex.escape(pattern) for pattern in ops.keys()])})\s*"



while True:

    entered = input('\nEnter a simple expression: (or return to exit) ')
    if not entered:break

    expression = regex.split(repattern, entered)
    expression = [pattern for pattern in expression if pattern]
    # got full expression down but not in BODMAS order
    print(expression)
    op = expression[1]
    num1 = int(expression[0])
    num2 = int(expression[2])

    if op in ops:
        try:
            answer = ops[op](num1, num2)
        except Exception as inst:
            print(f'** ERROR ** {inst}: expression:  {num1} {op} {num2}')
        else:
            print(answer)
    else:
       print("Invalid input")
