class Menu():
    
    def __init__(self, name, funcs):
        self.name = name
        self.exit = False  # funct should return dict with '_menu_exit': True to exit
        self.last_option = (None, None)  # key for option entered by user, function matched
        self.last_go_outcome = None
        '''create menu dictionary using function docstring...
        * assume each function has a docstring with the format:
          <option>: <description>
        * where <option> will probably be a single character
        * note: case of <option> is ignored so do not try to use upper and lower options of same letter'''
        self.menu = {option.strip().lower(): (option.strip(), desc.strip(), func ) 
            for func in func_list 
            for option, desc in [func.__doc__.split(':')] }

    def __str__(self):
        text = f'\n{self.name}\n{"-" * len(self.name)}\n'
        for _, (opt, desc, _) in self.menu.items():
              text += f'{opt:5}: {desc}\n'
        return text + '\n'
              
    def get_option(self, prompt='Enter option: ', print_menu=True, repeat_menu=True):
        'prompts user to make choice and returns function chosen'
        if print_menu: print(self)
        while True:
            opt = input(prompt).strip().lower()
            if opt and opt in self.menu:
                func = self.menu[opt][2]
                self.last_option = (opt, func)
                return func
            print('Not a valid option. Please try again.')
            if repeat_menu: print(self)
    
    def go(self, prompt, print_menu=True, repeat_menu=True):
        'get menu option from user and call corresponding function'
        outcome = self.get_option(prompt, print_menu, repeat_menu)()
        if isinstance(outcome, dict) and outcome.get('_menu_exit', False):
            self.exit = True
            del outcome['_menu_exit']
        self.last_go_outcome = outcome
        return outcome

def menu_option_1():
    '''1: This is option one'''
    print('one')

def menu_option_2():
    '''2: This is option two'''    
    print('two')
    return True

def menu_option_3():
    '''3: This is option three'''
    print('Three')
    return [1, 2, 3]

def menu_option_abc():
    '''Test: This is option three'''
    print('Test completed')

def menu_option_exit():
    '''X: Exit'''
    print('Exiting')
    return {'_menu_exit' : True, 'answers': [34, 56, 78]}

func_list = [func for name, func in globals().items() 
                 if callable(func) and name.startswith('menu_option_')]

menu = Menu('TOP LEVEL', func_list)
while not menu.exit:
    response = menu.go('What? ', print_menu=False, repeat_menu=False)
    if menu.last_option[0] == '3':
        for idx, num in enumerate(response):
            print(f'Option 3: item {idx} = {num}')

if response and isinstance(response, dict):
    answers = response.get('answers', None)
    if answers:
        for idx, num in enumerate(answers):
            print(f'Final result: item {idx} = {num}')
