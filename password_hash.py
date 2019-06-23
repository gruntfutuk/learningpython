import bcrypt  # install using pip install bcrypt  - might need to use pip3


def gen_password(password, salt=12):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(salt))


def check_password(check_password, stored_password):
    try:
        return bcrypt.checkpw(check_password.encode('utf-8'), stored_password)
    except ValueError:
        return False


def save_password(name, password):
    if name not in passwords:
        passwords[name] = gen_password(password)
        return True
    else:
        return False


def get_name_and_password():
    name = input('Name? (enter to finish): ')
    if not name:
        return None, None
    while True:
        password = input('Password? ')
        if password:
            break
        print('A password is require')
    return name, password


def add_users():
    print('\n\nAdd new users and passwords to password database\n')
    while True:
        name, password = get_name_and_password()
        if not name:
            return
        stored = save_password(name, password)
        if stored:
            print(f'{name} password saved')
        else:
            print(f'{name} is not unique and cannot be saved')


def test():
    print('\n\nEnter user names and passwords to test password database\n')
    while True:
        name, password = get_name_and_password()
        if not name:
            return
        if name in passwords:
            valid = check_password(password, passwords[name])
        else:
            valid = False
        print(f'Name and Password are {"correct" if valid else "not correct"}')


passwords = {}  # this would be stored in a file typically
add_users()
test()
