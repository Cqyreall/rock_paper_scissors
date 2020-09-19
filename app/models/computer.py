import random

def computer_choice():
    rps = ["rock", "paper", "scissors"]
    choice = random.randint(0,2)
    return rps[choice]


def winner(player, computer):
    winner = "AI"
  
    if player.choice == "rock":
        if computer == "paper":
             winner = "Titanius"
        elif computer == "scissors":
            winner = player.name
        else:
            winner = 'tie'


    if player.choice == "scissors":
        if computer == "rock":
            winner = "Titanius"
        elif computer == "paper":
            winner = player.name
        else:
            winner = 'tie'
    
    if player.choice == "paper":
        if computer == "scissors":
            winner = "Titanius"
        elif computer == "rock":
            winner = player.name
        else:
            winner = 'tie'
        
    return winner
        
