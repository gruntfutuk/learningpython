""" Example dictionary based menu system"""

from collections import namedtuple  # to refer to dictionary values easily

def menu_option(menu):
    header = "\nMenu\n"
    __data__ = menu.get('__data__')
    if __data__:
        header = __data__.get('header', header)
    print(header)
    for option, details in menu.items():
        if not option == "__data__":
            print(f'{option}:  {details.desc}')
    print('\n')
    while True:
        option = input('Option? ').strip().lower()
        if option in menu and option != "__data__":
            return menu[option]
        print('Sorry, that option is not available')

# function for each menu option except quit/exit where None is assigned
def option_1():
    print('option_1')

def option_2():
    print('option_2')

def option_3():
    print('option_3')

def option_2_1():
    print('option_2_1')

def option_2_2():
    print('option_2_1')
        
        
Menu = namedtuple('Menu', 'desc misc func')  # menu entries have three values, {<key>: (<desc>, <misc>, <func>)}
                                             # can add whatever addition fields are required
                                             # I used <func> to be the reference to the function to be called for
                                             # the correspnding option


menu1 = {"1": Menu("option 1", "misc", option_1),
         "2": Menu("option 2", "misc", option_2),
         "3": Menu('option 3', "misc", option_3),
         "q": Menu("quit", "", None),
         "__data__": {"header": "\nExample top level menu\n"},
           }
menu2 = {"1": Menu("option 2.1", "misc", option_2_1),
         "2": Menu("option 2.2", "misc", option_2_2),
         "q": Menu("exit", "", None),
         "__data__":  {"header": "\nExample second level menu\n"},
        }

# example use
while True:
    menu1_choice = menu_option(menu1)
    if not menu1_choice.func:
        break
    menu1_choice.func()