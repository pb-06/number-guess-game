"""
Console-based Number Guessing Game

This module provides a simple command-line interface for playing the number guessing game.
The player has unlimited attempts to guess a random number between 1 and 100.
The game provides feedback after each guess (too low, too high, or correct).
"""

import random


def guessing_game():
    """
    Main game function that runs the number guessing game in the console.
    
    Game Flow:
    1. Generates a random number between 1 and 100
    2. Continuously prompts the player for guesses
    3. Provides feedback on each guess (too low/high)
    4. Ends when the correct number is guessed
    5. Displays the total number of attempts taken
    
    Raises:
        ValueError: If the player enters non-integer input
    """
    # Display welcome message to the player
    print("Welcome to the Number Guessing Game!")
    
    # Generate a random number between 1 and 100 (inclusive) for the player to guess
    number_to_guess = random.randint(1, 100)
    
    # Initialize attempts counter to track how many guesses the player makes
    attempts = 0
    
    # Initialize guess variable; will be updated with player input in the loop
    guess = 0

    # Continue looping until the player guesses the correct number
    while guess != number_to_guess:
        # Get player's guess from console input and convert to integer
        guess = int(input("Enter your guess (1-100): "))
        
        # Increment attempts counter each time a guess is made
        attempts += 1

        # Provide feedback based on comparison with the target number
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            # Player guessed correctly - display congratulations message with attempt count
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")


if __name__ == "__main__":
    # Execute the game when script is run directly (not imported)
    guessing_game()