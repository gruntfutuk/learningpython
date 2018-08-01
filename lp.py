import lastpass

def search_name():
    pass

def search_url():
    pass

userdefault = 'lastpass@kyber.co.uk'

menu = {'1': ('Search for name', search_name),
        '2': ('Search for url', search_url),
        'q': ('quit', )
        }

def get_login_details():
    while True:
        username = input(f'Username ({userdefault}): ')
        if not username:
            username = userdefault
        password = input('Enter password: ')
        key = input('Enter authentication key: ')
        response = input('Ok to proceed?')
        if response.lower() in ['y', 'yes', 'ok', '1']:
            return username, password, key

def open_vault():
    print('Trying - be ready with confirmation on mobile device')
    vaultok  = True
    vault = lastpass.Vault.open_remote(username, password, key)
    return vault

def menu_choice():
    while True:
        for choice, entry in menu.items():
            print(choice, entry[0])
        option = (input(' -> ').lower())
        if option in menu:
            return option
        else:
            print('That is not a recognised option')

def vaultprint(search=''):
    search = search.strip().lower()
    for i, ac in enumerate(vault.accounts):
        search = search.strip().lower()
        id = ac.id.decode('utf-8')
        name = ac.name.decode('utf-8')
        username = ac.username.decode('utf-8')
        password = ac.password.decode('utf-8')
        url = ac.url.decode('utf-8')
        notes = [line for line in ac.notes.decode('utf-8').split('\n')]
        if search == '' \
          or search in username.lower() \
          or search in url.lower() \
          or search in " ".join(notes).lower() :
            print('id:\t', id)
            print('name:\t', name)
            print('u\'name:\t', username)
            print('pwd:\t', password)
            print('url:\t', url)
            if notes: print('notes:-')
            for line in notes:
                print('\t\t\t',line)
            print('-------------------------------------\n')

username, password, key = get_login_details()
vault = open_vault()
while True:
    option = menu_choice()
    if option == 'q':
        break

    menu[option][1]

print('** fini **')
