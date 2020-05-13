from random import choice
from itertools import cycle

def get_user_choice(prompt="Enter option: ", options=None):
    if options is None:
        options = directions
    while True:
        option = input(prompt).strip().lower()
        if option in options:
            return option
        print('That is not a valid choice.')
        print(f'Options are: {", ".join(option.title() for option in options)}')

def report(action, user_option, computer_option, saved):

    def reporting(team1, move1, team2, move2):
        report_txt = f"\n{team1} team shoots to the {move1}\n" \
                f"{team2} team goalkeeper dives to the {move2}\n"
        if saved:
            report_txt += "SAVED!!!\n"
        else:
            report_txt += f"GOAL !!! for {team1} team\n"
        return report_txt

    if action == "Shoot":
        return reporting("User", user_option, "Computer", computer_option)
    else:
        return reporting("Computer", computer_option, "User", user_option)
     
def take_penalty_each():
    user_goals = 0
    computer_goals = 0
    for _ in range(2): # loops twice, once for each team
        user_action = next(action)
        user_option = get_user_choice(action_prompt[user_action])
        computer_option = choice(directions)
        saved = (user_option, computer_option) in saves
        outcome = report(user_action, user_option, computer_option, saved)
        if not saved:
            if user_action == "Shoot":
                user_goals += 1
            else:
                computer_goals +=1
        print(outcome)
    return user_goals, computer_goals
        
def print_scores():
    final = total_penalties == max_penalties
    if final:
        print('\n\nFINAL SCORES\n')
    else:
        print('\n\nSCORES\n')
    print(f"The score is now USER: {user_team_score} "
          f"COMPUTER: {computer_team_score}")
    if final:
        if user_team_score > computer_team_score:
            print("Well done you won")
        elif user_team_score == computer_team_score:
            print("A draw")
        else:
            print("You Lose")
    print()


directions = ["left", "middle", "right"]
saves = (("right", "left"), ("middle", "middle"), ("left", "right"))
action = cycle(['Shoot', 'Keep'])
action_prompt = {'Shoot': "Pick your spot: ",
                 'Keep': "Choose dive direction: " }

total_penalties = 0
user_team_score = 0
computer_team_score = 0
max_penalties = 10

print("------WELCOME TO THE PYTHON PENALTY SHOOTOUT------")
print("The options you can choose are left,right or middle")

while total_penalties < max_penalties:
    user_goals, computer_goals = take_penalty_each()
    user_team_score += user_goals
    computer_team_score += computer_goals
    total_penalties += 2
    print_scores()