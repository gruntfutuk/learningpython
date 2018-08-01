from collections import OrderedDict


class AutoMenu:

    def __init__(self):
        """
        Menu is built by collecting functions decorated with "_menu_enumerator"
        """
        all_attribs = (getattr(self, attr) for attr in dir(self))
        menu_items = sorted((attr for attr in all_attribs
                             if hasattr(attr, '_menu_idx')),
                            key=lambda a: a._menu_idx)

        self._menu_prompts = '\nMake your choice\n' + '\n'.join(
            '{:2d} - {}'.format(f._menu_idx, f.__name__.replace('_', ' ').title()) for f in menu_items)
        self._menu = OrderedDict((str(m._menu_idx), m) for m in menu_items)

    @staticmethod
    def _make_menu_item(func, item_no=[0]):
        """ Method decorator
                Mark decorated function as menu item by setting attribute
                _item_idx and use it to set order
        """
        item_no[0] += 1
        setattr(func, '_menu_idx', item_no[0])
        return func

    _menu_enumerator = _make_menu_item.__func__

    @_menu_enumerator
    def one(self, *args, **kwargs):
        print('You chose option 1. Singular choice.')

    @_menu_enumerator
    def two(self, *args, **kwargs):
        print('You chose option 2. Two\'s company.')

    @_menu_enumerator
    def three(self, *args, **kwargs):
        print('You chose option 3. Three\'s a crowd.')

    @_menu_enumerator
    def end_game(self, *args, **kwargs):
        print('You chose option x. Farewell.')
        return True

    def bad_choice(self):
        print('Are you sure?')

    def __call__(self):
        while True:
            print(self._menu_prompts)
            choice = input('Your choice? ')
            end_game = self._menu.get(choice, self.bad_choice)()
            if end_game:
                break


AutoMenu()()
