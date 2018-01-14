# a simple menu system

while True:
    
    # menu choices
    print("\n\nSelection one of the options below by entering the letter.\n")
    print('a\tif you want an apple')
    print('b\tif you want a banana')
    print('c\tif you want a cherry')
    print('or\tjust press ENTER to exit\n')
    option = input("Enter your choice:").lower()
    print()
    
    # actions
    if not option:
        break
    elif option == "a":
        print('Have an apple.')
    elif option == "b":
        print('Have a banana')
    elif option == "c":
        print('Have a cherry')
    else:
        print('Sorry, that was not a valid option. Try again.')