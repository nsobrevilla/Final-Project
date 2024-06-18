import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    player1_score = 0
    player2_score = 0
    
    while player1_score < 2 and player2_score < 2:
        input("Player 1, press Enter to roll the dice...")
        player1_roll = roll_dice()
        print(f"Player 1 rolled: {player1_roll}")
        
        input("Player 2, press Enter to roll the dice...")
        player2_roll = roll_dice()
        print(f"Player 2 rolled: {player2_roll}")
        
        if player1_roll > player2_roll:
            player1_score += 1
            print("Player 1 wins this round!")
        elif player2_roll > player1_roll:
            player2_score += 1
            print("Player 2 wins this round!")
        else:
            print("This round is a tie!")
        
        print(f"Score - Player 1: {player1_score}, Player 2: {player2_score}")
        
    if player1_score == 2:
        print("Congratulations! Player 1 is the overall winner!")
    else:
        print("Congratulations! Player 2 is the overall winner!")

play_game()
