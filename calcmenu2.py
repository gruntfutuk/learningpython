
    def rounding():
        # code goes here, all indented one level (4-spaces)
        print('rounding')

    def another():
        # code goes here, all indented one level (4-spaces)
        print('another')

    def choose(menu):
        """display menu and return option"""
        
        print("\n\nMenu: \n")
        for option, (desc, func) in menu.items():
            print(f"{option}: {desc}")
        
        while True:
            option = input('Option? ').strip().lower()
            if option in menu:
                return menu[option][1]
            print('Invalid option, please try again')

    menu = {'r': ('rounding', rounding),
            'a': ('another', another), 
            'x': ('exit', None),
            }

    while True:
        option = choose(menu)
        if option:  # a calculator function returned
            option()  # call function
        else:  # None was returned
            break
        
