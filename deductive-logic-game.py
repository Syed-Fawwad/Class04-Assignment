import random

def generate_secret_number():
    """Generate a random 3-digit secret number"""
    return str(random.randint(100, 999))

def give_feedback(secret, guess):
    """Provide feedback for the guess"""
    feedback = []
    
    # Check for correct digits in the correct place (👍)
    for i in range(3):
        if guess[i] == secret[i]:
            feedback.append("👍")
        else:
            feedback.append("❌")
    
    return ''.join(feedback)

def main():
    print("Welcome to the Guessing Game!")
    
    # Generate the secret 3-digit number
    secret = generate_secret_number()
    attempts = 10
    
    # Game loop
    while attempts > 0:
        guess = input(f"\nYou have {attempts} attempts left. Guess a 3-digit number: ")
        
        if len(guess) != 3 or not guess.isdigit():
            print("Please enter a valid 3-digit number.")
            continue
        
        # Provide feedback
        feedback = give_feedback(secret, guess)
        
        # Print feedback
        print(feedback)
        
        # Check if the guess is correct
        if guess == secret:
            print("You got it! Congratulations, you guessed the correct number.")
            break
        
        attempts -= 1
        
    if attempts == 0:
        print(f"\nGame Over! The secret number was: {secret}")

# Run the game
if __name__ == "__main__":
    main()