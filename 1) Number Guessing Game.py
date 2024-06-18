import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    
    # Initialize the number of guesses
    guess_count = 2
    
    while True:
        # Get the user's guess
        guess = input("Enter your guess: ")
        
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue
        
        # Increment the number of guesses
        guess_count += 1
        
        # Check if the guess is correct
        if guess == number_to_guess: 
            print(f"Congratulations! You guessed the number in {guess_count} tries.")
            break
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Start the game
if __name__ == "__main__":
    number_guessing_game()
