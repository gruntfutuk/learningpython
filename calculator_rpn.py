class Calculator:
    
    GUIDE = ''  # placeholder for init
    
    def __init__(self):
        self.clear()
        self.degrees = True
        self.scimode = False
        self.rpn = True
        print(Calculator.GUIDE)

    @staticmethod
    def is_quit(text):
        return text.lower() in ('q', 'quit', 'exit', 'x')

    def stack_op(self, text):
        if text.lower() in Calculator.OPS:
            self.stack.append(Calculator.OPS[text.lower()][-1])
            return True
        return False

    def stack_num(self, text):
        num = None
        try:
            num = float(text)
            num = int(text)
        except ValueError:
            pass
        if num is None:
            return False
        self.stack.append(num)
        return True                

    def clear(self):
        self.display = ""
        self.memory = 0
        self.stack = []

    def enough_nums(self, required=2):
        """confirm if stack holds sufficient numbers for an operation"""
        if len(self.stack) >= required:
            for n in range(required):
                if not isinstance(self.stack[-1-n], (int, float)):
                    return False
            return True
        return False    

    def entry(self):
        while True:
            response = input(f'{self.display} > ')
            if self.is_quit(response):
                return None
            elif self.stack_op(response):
                return True
            elif self.stack_num(response):
                return False
            self.display = f'ERR (unknown) {self.stack}'

    def op_add(self):
        if self.enough_nums():
            print(self.stack)
            self.stack.append(self.stack.pop() + self.stack.pop())
            self.display = self.stack
        else:
            self.display = f'ERR (not enough nums) {self.stack}'

    def op_sub(self):
        if self.enough_nums():
            self.stack.append(- self.stack.pop() + self.stack.pop())
            self.display = self.stack
        else:
            self.display = f'ERR (not enough nums) {self.stack}'

    def op_mul(self):
        if self.enough_nums():
            self.stack.append(self.stack.pop() * self.stack.pop())
            self.display = self.stack
        else:
            self.display = f'ERR (not enough nums) {self.stack}'

    def op_div(self):
        if self.enough_nums():            
            if not self.stack[-1] == 0:
                self.stack.append(self.stack.pop(-2) / self.stack.pop())
                self.display = self.stack
            else:
                self.display = f'ERR (div by 0 not allowed) {self.stack}'
        else:
            self.display = f'ERR (not enough nums) {self.stack}'

    def op_del1(self):
        if self.stack:
            self.stack.pop()
            self.display = self.stack

    def op_whole(self):
        if self.enough_nums(1):
            self.stack.append(int(self.stack.pop()))
            self.display = self.stack
        else:
            self.display = f'ERR (not enough nums) {self.stack}'

    def op_round(self):
        if self.enough_nums():
            self.stack.append(round(self.stack.pop(-2), self.stack.pop()))
            self.display = self.stack
        else:
            self.display = f'ERR (not enough nums) {self.stack}'

    def op_help(self):
        print(Calculator.GUIDE)

    def work(self):
        while True:
            status = self.entry()
            if status is None:
                return
            elif status:
                op = self.stack.pop()
                op(self)
            else:
                self.display = self.stack
                
    OPS = {'+': ('add two numbers', op_add),
           '-': ('subtract top from next down', op_sub),
           '*': ('multipple two numbers', op_mul),
           '/': ('divide 2 down by top', op_div),
           'int': ('truncate top to integer', op_whole),
           'round': ('round 2 down to top decimal places', op_round), 
           'h': ('display hel', op_help),
           'del': ('remove top number', op_del1),
           'q': ('quit Calculator', None),
          }
    
    DETAILS = ''.join(f'\t{code:5} {desc}\n' for code, (desc, _) in OPS.items()) 
    
    GUIDE = f'Welcome to our simple RPN Calculator\n\n' \
            f'Operators/Commands:\n{DETAILS}\n'
    

calc1 = Calculator()
calc1.work()