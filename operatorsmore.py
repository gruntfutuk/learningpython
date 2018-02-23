import regex
import operator

ops = {'+':  operator.add,
       '-':  operator.sub,
       '*':  operator.mul,
       '/':  operator.truediv,
       '//': operator.floordiv,
       '%':  operator.mod,
       '**': operator.pow,
       '^':  operator.pow,
       '<':  operator.lt,
       '<=': operator.le,
       '==': operator.eq,
       '!=': operator.ne,
       '>=': operator.ge,
       '>':  operator.gt
       }

precedence = {
       '+':  10,
       '-':  10,
       '*':  20,
       '/':  20,
       '//': 20,
       '%':  20,
       '**': 30,
       '^':  30,
       '<':  5,
       '<=': 5,
       '==': 5,
       '!=': 5,
       '>=': 5,
       '>':  5,
       '(':  1,
       ')':  1
       }



def evaluateexpression(entered):
    ''' evaluate a simple expression '''

    class BadExpression(Exception):
        def __init__(self, msg):
            Exception.__init__(self)
            self.msg = msg


    def tokenise(entered):
        ''' convert list of expression elements to returned list of correctly typed elements '''

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

        expression = regex.split(repattern, entered)

        newexpression = []
        for token in expression:
            if not token: continue  # ignore empty tokens
            if token in ops or token in "()":
                newexpression.append(token)
            else:
                try:
                    newtoken = int(token)
                except ValueError:
                    try:
                        newtoken = float(token)
                    except ValueError:
                        raise BadExpression(f'Error: {token} not recognised.')
                newexpression.append(newtoken)
        return newexpression


    def evalrpn():
        ''' evaluate topmost operation on stack, replace top two values with answer, remove operator '''
        if len(values) <= 1:
            raise BadExpression('Error - too many operators for values provided')
        if len(operators) == 0:
            raise BadExpression('Error - too few operators for values provided')
        num2 = values.pop()
        num1 = values.pop()
        op = operators.pop()

        try:
            answer = ops[op](num1, num2)
        except Exception as inst:
            raise BadExpression(f'Error: {inst}, {num1} {op} {num2}')
        else:
            values.append(answer)
    try:
        expression = tokenise(entered)
        values = []
        operators = []
        for token in expression:
            if isinstance(token, int):
                values.append(int(token))
            elif isinstance(token, float):
                values.append(float(token))
            elif isinstance(token, str):
                if token == '(':
                    operators.append(token)
                elif token == ')':
                    while not operators[-1] == '(':
                        evalrpn()
                    operators.pop() # remove the (
                elif token in ops:
                    while len(operators) > 0 and precedence[operators[-1]] >= precedence[token]:
                        evalrpn()
                    operators.append(token)
        while len(operators) > 0:
            evalrpn()
    except BadExpression:
        print(f'{entered} is not an acceptable expression.')
        return "no answer"

    return values[0]


while True:

    entered = input('\nEnter a simple expression: (or return to exit) ')
    if not entered:break
    answer = evaluateexpression(entered)
    print(f'\n{entered} = {answer}\n')

