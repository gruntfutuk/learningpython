#!/usr/bin/python3

# simple text version of the Rock Paper Scissors Lizard Spock game
# http://bigbangtheory.wikia.com/wiki/Rock_Paper_Scissors_Lizard_Spock

# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
#   0 - rock
#   1 - Spock
#   2 - paper
#   3 - lizard
#   4 - scissors

# Each player picks a "hand-shape", then all players reveal their choices at the same time.
# The winner is the one who defeats the others. The rules of rock-paper-scissors-lizard-Spock
# are described in the rules dictionary, winning weapon > losing weapon : reason

# Given two weapon choices, a and b (that are different) 
# the winner can be determined by (a-b) %5 < 3
# (i.e. the remainder after divion by 5 is less than 3)
# a wins if True, b wins if False

def main():
    
    import random
  
    
    def choice_to_index(choice):
        # Converts player choice to its index number
        # returns the value associated with the string key
        return weaponsnames[choice]
    
    
    def index_to_choice(index):
        # Converts player choice index to its name
        # returns the value associated with the string key
        return weaponsindex[index]
    
    
    def whowins(player, computer):
        # Determines who wins; uses a calculation on indexes to figure it out
        if player == computer:
            return 'Tie', "'great minds think alike' (as the saying goes)."
        elif (choice_to_index(player)-choice_to_index(computer))%5 < 3:
            return 'Player', reasoning(player, computer)
        else:
            return 'Computer', reasoning(computer, player)
  
    
    def reasoning(winner, loser):
        # generate explanation of how the game was won
        action = rules[f'{winner}>{loser}']  # look up the rule using the key
        return f'{winner} {action} {loser}'  # return explanation 
  
    
    def player_input():
        # remind player of weapon choices, and get choice (or exit option)
        while True:
            player = input(f"\nEnter your choice {'/'.join(weapons)}\n  (or enter to exit): ")
            if player in weaponsinits:
                player = weaponsinits[player]
            if not player or player in weapons:
                break
            print(f"{player} is not valid. Try again.")
        return player
    
    
    def computer_input():
        return index_to_choice(random.randint(0, len(weapons)-1))

    # dictionary used for weapons, index values used to calculate winner
    weaponsindex = {0:'rock', 1:'Spock', 2:'paper', 3:'lizard', 4:'scissors'}
    weaponsnames = dict((v, k) for k, v in weaponsindex.items())
    weapons = list(weaponsindex.values())
    weaponsinits = {weapon[0]:weapon for weapon in weapons} # initial character of weapon - should be unique
    scores = {'Player': 0, 'Computer': 0, 'Tie': 0}
    # rules & user input are case sensitive, because I couldn't be bothered to address
    rules = {"scissors>paper" : "cut",
            "paper>rock" : "covers",
            "rock>lizard" : "crushes",
            "lizard>Spock" : "poisons",
            "Spock>scissors" : "smashes",
            "scissors>lizard" : "decapitate",
            "lizard>paper" : "eats",
            "paper>Spock" : "disproves",
            "Spock>rock" : "vaporizes",
            "rock>scissors" : "crushes"
        }
    console = False

    def gui():

        import tkinter as tk

        class Application(tk.Frame):
            def __init__(self, master=None):
                super().__init__(master)
                self.pack()
                self.gameboard()
                self.weaponbuttons()
                self.gameround = tk.IntVar(value=1)

            def gameboard(self):
                tk.Label(self, text = "Welcome to our rock-paper-scissors-lizard-Spock game").pack()
                self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
                self.quit.pack(side="bottom")

            def weaponbuttons(self):

                def onbutton_click(label):
                    player = label
                    computer = computer_input()
                    winner, reason = whowins(player, computer)
                    scores[winner] += 1
                    roundmsg, matchmsg, resultmsg = outresult(self.gameround.get(), player, computer, winner, reason)
                    setmsg(roundmsg, matchmsg, resultmsg)
                    self.gameround.set(self.gameround.get()+1)

                def setmsg(roundmsg, matchmsg, resultmsg):
                    roundlbl.set(roundmsg)
                    matchlbl.set(matchmsg)
                    resultlbl.set(resultmsg)

                win = tk.Tk()
                win.title = 'Click weapon of choice'
                for col, weapon in enumerate(weapons):
                    butName = tk.Button(win, text=weapon, command=lambda e=weapon: onbutton_click(e))
                    butName.grid(row=0, column=col)

                roundlbl = tk.StringVar()
                matchlbl = tk.StringVar()
                resultlbl = tk.StringVar()
                tk.Label(self.master, textvariable=roundlbl).pack()
                tk.Label(self.master, textvariable=matchlbl).pack()
                tk.Label(self.master, textvariable=resultlbl).pack()
                setmsg("Round (None).",
                        "You chose: None, Computer chose: None.",
                        "Winner: None because no reason yet"
                        )

        root = tk.Tk()
        app = Application(master=root)
        app.mainloop()


    def outresult(gameround, player, computer, winner, reason):  
        roundtxt = f"Round {gameround:2d}."
        matchtxt = f"You chose: {player}, Computer chose: {computer}."
        resulttxt = f"Winner: {winner} because {reason}"
        if console:  
            print("\n" + roundtxt)
            print("  " + matchtxt)
            print("  " + resulttxt)
        else:
            return roundtxt, matchtxt, resulttxt

    def outgreeting():
        if console:
            print('\n\nWelcome to our rock-paper-scissors-lizard-Spock game\n\n')
        else:
            pass
        
    def consoleplay():
        global round, computer, player, winner, reason
        outgreeting()
        gameround = 1
        while True:
            computer = computer_input()
            player = player_input()
            if not player:
                break
            winner, reason = whowins(player, computer)
            scores[winner] += 1
            outresult(gameround, player, computer, winner, reason)
            gameround += 1
        print(f"\n\nTotal scores: You: {scores['Player']}, Computer: {scores['Computer']}, Ties: {scores['Tie']}\n\n")    


    if not console:
        gui()
    else:
        consoleplay()


if __name__ == "__main__":
    main()

