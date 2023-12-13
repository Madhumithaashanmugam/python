import random
def get_choice():
    player_choice=input("enter a choice(rock, paper, scissors):")
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    
    return choices

def check_win(player,computer):
    print(f"you chose  {player},computer choose is {computer}")
    if player == computer:
        return "it's a tie!"
    elif player == "rock" :
        if computer == "scissors":
            return "Rock smashes scissors! you win!"
        else:
            return "paper covers rock! you lose."
    
check_win("rock","paper") 