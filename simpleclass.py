def report(choices, desc='For breakfast: '):
    if breakfast:
        print(desc, end='')
        print(*choices, sep=", ")

class breakfast:
    def __init__(self, choices=['fishystuff', 'yogurt']):
        self.choices = choices
        report(self.choices)
        return
     
    def add(self, addchoice):
        self.choices.extend(addchoice)
        report(addchoice, 'Adding: ')
        report(self.choices, 'So for breakfast now have: ')
        return
     
     
stuart=breakfast()
lucy=breakfast(['porridge', 'fruit'])
options = ['nuts', 'raisons']
lucy.add(options)