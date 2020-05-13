def yes(msg="Yes or No? ", default=None):
    """Obtain yes / no response from user and return as True/False

    if a default is provide, True or False, then a the use can just
    press return for that default
    """
    
    while True:
        response = input(msg).lower().strip()
        if not response and default in (True, False):
            return default
        if response in AFFIRMATION:
            return True
        if response in REJECTION:
            print("your information is incorrect, please re-enter")
            return False
        print("please enter a valid answer" )


AFFIRMATION = frozenset(('yes', 'y', 'yeh', 'ok', '1', 'yup'))
REJECTION = frozenset(('no', 'n', '0', 'nope', 'nah'))