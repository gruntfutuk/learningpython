from blessed import Terminal

term = Terminal()
with term.location(0, term.height - 1):
    print('This is ' + term.underline('underlined') + '!')
