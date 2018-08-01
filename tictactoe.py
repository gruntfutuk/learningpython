# Tic Tac Toe Game

tab = list(" " * 9)
# flag[0] to check tab full or not
# flag[1] to check win or not
flag = [None, None, 0, 0]
# flag[2] x_wins = 0
# flag[3] o_wins = 0
print("\033[1;32;40m !!!TIC TAC TOE!!!  \n")


def print_tab():
    print("[", tab[0], '|', tab[1], '|', tab[2], "]")
    print("[", tab[3], '|', tab[4], '|', tab[5], "]")
    print("[", tab[6], '|', tab[7], '|', tab[8], "]")


def check_result():
    if " " in tab:
        if tab[0:3] == "X" or tab[3:6] == "X" or tab[7:9] == "X" or tab[0] == tab[3] == tab[6] == "X" or tab[1] == tab[4] == tab[7] == "X" or tab[2] == tab[5] == tab[8] == "X" or tab[0] == tab[4] == tab[8] == "X" or tab[2] == tab[4] == tab[6] == "X":
            print("X wins this Game.")
            flag[2] += 1
            print("Total Result : X Won =", flag[2], "and O Won =", flag[3])
            flag[0] = True
            new_game()

        if tab[0:3] == "O" or tab[4:6] == "O" or tab[7:9] == "O" or tab[0] == tab[3] == tab[6] == "O" or tab[1] == tab[4] == tab[7] == "O" or tab[2] == tab[5] == tab[8] == "O" or tab[0] == tab[4] == tab[8] == "O" or tab[2] == tab[4] == tab[6] == "O":
            print("O wins the Game.")
            flag[3] += 1
            print("Total Result : X Won =", flag[2], "and O Won =", flag[3])
            flag[0] = True
            new_game()

    else:
        print("The Game is DRAW. Total Result : X Won =",
              flag[2], "and O Won =", flag[3])
        flag[0] = True
        new_game()


def clr():
    print("\n" * 50)


def insert_x():
    while True:
        pos = int(input("X, Choose a position to insert X._ "))
        if pos in range(1, 10):
            if tab[pos - 1] == " ":
                tab[pos - 1] = "X"
                clr()
                break

            else:
                print(
                    pos, " Position is not available. Choose a position that is available from the table below.")
                print_tab()

        else:
            print("Please choose a number from 1 to 9.")
            print_tab()
    print_tab()


def insert_o():
    pos = int(input("O, Choose a position to insert O._ "))
    if pos in range(1, 10):
        if tab[pos - 1] == " ":
            tab[pos - 1] = "O"
            clr()

        else:
            print(
                pos, " Position is not available. Choose a position that is available from the table below.")
            print_tab()
            insert_o()
    else:
        print("Please choose a number from 1 to 9.")
        print_tab()
        insert_o()
    print_tab()


def new_game():
    ch = input("Do you want to play Tic Tac Toe?(Y?N):_ ")
    if ch == "N" or ch == "n":
        print("Thank you!")

    elif ch == "Y" or ch == "y":
        clr()
        for i in range(0, 9):
            tab[i] = " "

        #  tab = list(" " * 9)
        print_tab()
        while flag[1] is True or flag[1] is None:
            insert_x()
            check_result()
            insert_o()
            check_result()
    else:
        print('Please type Y or N only.')


while True:
    ch = input("Do you want to play Tic Tac Toe?(Y?N):_ ")
    if ch == "N" or ch == "n":
        print("Thank you!")
        break
    elif ch == "Y" or ch == "y":

        print_tab()
        while flag[1] is True or flag[1] is None:
            insert_x()
            check_result()
            insert_o()
            check_result()
    else:
        print('Please type Y or N only.')
