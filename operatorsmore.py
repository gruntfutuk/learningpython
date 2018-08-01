""" simple arithmetic expression evaluator """

import regex as re
import operator

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv,
       '//': operator.floordiv,
       '%': operator.mod,
       '**': operator.pow,
       '^': operator.pow,
       '<': operator.lt,
       '<=': operator.le,
       '==': operator.eq,
       '!=': operator.ne,
       '>=': operator.ge,
       '>': operator.gt
       }

precedence = {
    '+': 10,
    '-': 10,
    '*': 20,
    '/': 20,
    '//': 20,
    '%': 20,
    '**': 30,
    '^': 30,
    '<': 5,
    '<=': 5,
    '==': 5,
    '!=': 5,
    '>=': 5,
    '>': 5,
    '(': 1,
    ')': 1
}


def evaluateexpression(entered):
    ''' evaluate a simple expression '''

    class BadExpression(Exception):
        def __init__(self, msg):
            Exception.__init__(self)
            self.msg = msg

    def tokenise(entered):
        ''' convert list of expression elements to returned list of correctly typed elements '''

        repattern = re.compile('''
                         \s*                # bypass leading whitespace
                         (                  # grouping starts
                          (?<!\d)-?         # allow for negative number (rather than - operator)
                          \d+               # a number, optionally followed by fractional part
                          (?:\.\d+)?        # assumes we use . a decimal seperator
                         |                  # OR
                           (?://|\*\*)      # Non-capturing single operator
                           |(?:[+-/*^])     # or two-character operator group
                         )                  # grouping ends
                         \s*                # bypass trailing whitespace
                         ''', re.VERBOSE)

        expression = re.split(repattern, entered)

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
        x = values.pop()
        y = values.pop()
        op = operators.pop()

        try:
            answer = ops[op](x, y)
        except Exception as inst:
            raise BadExpression(f'Error: {inst}, {x} {op} {y}')
        else:
            values.append(answer)

    try:
        expression = tokenise(entered)
    except BadExpression as bad:
        return f'{bad.msg}'

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
                operators.pop()  # remove the matching (
            elif token in ops:
                while len(operators) > 0 and precedence[operators[-1]] >= precedence[token]:
                    evalrpn()
                operators.append(token)
        else: raise BadExpression('{token} not recognised.')

    try:
        while len(operators) > 0:
            evalrpn()

    except BadExpression as bad:
        return f'{bad.msg}'

    return f'{entered} = {values[0]}'


print('''

Welcome to this simple arithmetic expression evaluator

Basic arithmetic and logic operators that work on two values are
understood and may be chained. Round brackets can also be used
to override BODMAS precedence order (and are required for consecutive
power operators at present). Evaluator works with floats and integers
only.

(Note. ** and ^ are both used for raising to power.)

RPN entry is also supported (use spaces to separate inputs).

Exit by entering nothing (or words/characters like q, quit, exit, etc).
        
''')

while True:

    leave = frozenset(['q', 'exit', 'exit()', 'quit', 'end', 'fini', 'finish', 'bye', "x", ""])
    providedexpression = input('\nEnter a simple expression: ')
    if providedexpression.lower() in leave: break
    answer = evaluateexpression(providedexpression)
    print(f'\n{answer}\n')

print('\n\n** finished **\n\n')