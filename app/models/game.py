# class Game:

#     def __init__(self, player1, player2)

def winner_of_game(player_1, player_2):

    winner = "Player1"   
    if player_1 == "rock":
        if player_2 == "paper":
             winner = "Player 2"
        elif player_2 == "scissors":
            winner = "Player 1"
        else:
            winner = 'tie'

    if player_1 == "paper":
        if player_2 == "scissors":
            winner = "Player 2"
        elif player_2 == "rock":
            winner = "Player 1"
        else:
            winner = 'tie'

    if player_1 == "scissors":
        if player_2== "rock":
            winner = "Player 2"
        elif player_2== "paper":
            winner = "Player 1"
        else:
            winner = 'tie'
        
    return winner

        