class MyClass:
    variable = 'blah'


    def function(self):
        print(f'The variable is: {self.variable}')


me = MyClass()
print(me.variable)
me.function()
