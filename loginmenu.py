''' text menu in python.'''

logged_in = False

def print_menu():  ## Your menu design here
    print(30 * "-", "MENU", 30 * "-")
    print("1. Login")
    print("2. Create an account")
    print("3. List all accounts")
    print("4. Quit")
    print(67 * "-")

def read_credentials():
    ''' write code to read credentials and return a dictionary '''
    users = {}
    try:
        with open('credential.txt', 'r') as file:
            for line in file:
                user, password = line.strip().split()
                users[user] = password
    except FileNotFoundError:
        pass
    return users

def login(users):
        attempts = 0
        while True:
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")

            if username in users and users[username] == password:
                print("\nLogin successful!\n")
                return True

            attempts += 1

            print("\nUser doesn't exist or wrong password!\n")

            if attempts >= 3:
                print("Too many attempts.")
                return False

            print('Please try again.')

def register(users):
    while True:
        username = input("Please input your desired username: ")
        password = input("Please input your desired password: ")

        if not username or not password:  # if either is blank
            print("Enter a valid username and password...")
        elif username in users:
            print("Username already exists. Please try again ...")
        else:
            break

    # users = c.get_all_users()  - need to write the function for this, let's fake it for now

    users[username] = password
    print('Writing user details to file ...3')
    with open("credential.txt", "a") as file:
        file.write(username + " " + password + "\n")

    thank_you()

def listusers(users):
    ''' list the users registered with the system'''

    print('Registered users:')
    for user in users.keys():
        print(user)

def thank_you():
    print("Thank you for signing up at our website!.")



users = read_credentials()

while True:

    print_menu()
    choice = input("Enter your choice [1-4]: ")

    if choice == "1":
        if login(users):
            logged_in = True
    elif choice == "2":
        register(users)
    elif choice == "3":
        listusers(users)
    elif choice == "4":
        logged_in = False
        break
    else:
        print('Unknown option. Please try again.')

print('Farewell')