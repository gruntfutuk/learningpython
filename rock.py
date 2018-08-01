def my_game(com_play, user_play, *plays):
    plays = list(plays)
    while plays[0] != com_play:
        shifted = plays.pop(0)
        plays.append(shifted)
    game_state = ['draw', 'You lose', 'You win', 'You lose', 'You win'] \
    if len(plays) == 5 else ['draw', 'You win', 'You lose']
    return game_state[plays.index(user_play)]
