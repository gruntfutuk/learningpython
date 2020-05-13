def bet():
    while True :
        a = ["love", "sex", "money"]
        b = input("Enter your choice: ")
        if b == a[0]:
            print("\n you want to be loved, \n but afraid to invest in it \n")
            continue
        elif b == a[1]:
            print("\n i like your honesty, \n but dont be afraid to love \n ")
            continue
        elif b == a[2]:
            print("\n you are predictable, \n money is not everything \n")
            continue
        elif b == "done":
            print(f"thanks for playing with me", u)
            break
        else:
            print("\n not in list \n\t Don't be dumb")
            continue


print("#guessing game with ChimaHotize \n")
print("Type 'guest' to get access")
print("Type 'done' to exit game \n")
print("choose between love, sex & money \n")

u = "guest"
while True:
    user_name = input("Enter a User name > ")



while True:
    if user_name == u:
        bet()
        break
    elif user_name == "done":
        print(f"thanks for playing with me", u)
        break
    else:
        print("you're not authorized")
        break
