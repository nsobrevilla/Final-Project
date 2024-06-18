import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

def play_game():
    player_score = 0
    computer_score = 0
    
    while player_score < 2 and computer_score < 2:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        winner = get_winner(player_choice, computer_choice)
        if winner == "player":
            player_score += 1
            print("You win this round!")
        elif winner == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("This round is a tie!")
        
        print(f"Score - You: {player_score}, Computer: {computer_score}")
        
    if player_score == 2:
        print("Congratulations! You are the overall winner!")
    else:
        print("Sorry! The computer is the overall winner!")

play_game()
