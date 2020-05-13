def yes(msg="Yes or No? ", err="don't undestand",
            default=None, affirm=None, reject=None) -> bool:
    """True if user input in first sequence, False if in second sequence
    or default if True or False and user enters empty response"""

    AFFIRMATION = frozenset(('yes', 'y', 'yeh', 'ok', '1', 'yup')) \
        if affirm is None else affirm
    REJECTION = frozenset(('no', 'n', '0', 'nope', 'nah')) \
        if reject is None else reject

    while True:
        response = input(msg).lower().strip()
        if not response and default in (True, False):
            return default
        if response in AFFIRMATION:
            return True
        if response in REJECTION:
            return False
        print(err)