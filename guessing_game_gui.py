"""
GUI-based Number Guessing Game using PySimpleGUI

This module provides a graphical user interface (GUI) for playing the number guessing game.
Players interact with the game through buttons and text input fields in a dedicated window.
Features include attempt tracking, game reset functionality, and an output history log.
"""

import PySimpleGUI as sg
import random

# Configure the GUI theme with a dark blue color scheme for better visual appearance
sg.theme('DarkBlue3')


def create_window():
    """
    Creates and returns the main game window with all UI elements.
    
    The window layout includes:
    - Title: "Number Guessing Game"
    - Instructions: "Guess a number between 1 and 100"
    - Input field: For player to enter their guess
    - Buttons: Submit, New Game, Exit
    - Output area: Displays game history and feedback
    - Attempts counter: Shows current number of attempts
    
    Returns:
        sg.Window: A PySimpleGUI Window object containing the game interface
    """
    # Define the window layout as a list of rows, each containing UI elements
    layout = [
        # Title row with large bold text
        [sg.Text('Number Guessing Game', font=('Arial', 20, 'bold'))],
        
        # Instructions row
        [sg.Text('Guess a number between 1 and 100', font=('Arial', 12))],
        
        # Spacer row (empty text for vertical spacing)
        [sg.Text('')],
        
        # Input row: Label and text input field for the player's guess
        # Key 'GUESS' allows access to this element in the event loop
        [sg.Text('Your Guess:', font=('Arial', 11)), 
         sg.InputText(size=(10,), key='GUESS', font=('Arial', 11))],
        
        # Button row: Three action buttons
        # Each button triggers a different event when clicked
        [sg.Button('Submit', size=(10,)), 
         sg.Button('New Game', size=(10,)), 
         sg.Button('Exit', size=(10,))],
        
        # Spacer row
        [sg.Text('')],
        
        # Output area: Multiline text box to display game history
        # Key 'OUTPUT' allows programmatic updates; disabled=True makes it read-only
        [sg.Multiline(size=(40, 10), key='OUTPUT', disabled=True, font=('Arial', 10))],
        
        # Attempts counter: Displays the current number of attempts
        # Key 'ATTEMPTS' allows programmatic updates
        [sg.Text('Attempts: 0', key='ATTEMPTS', font=('Arial', 11, 'bold'))]
    ]
    
    # Create and return the window with the defined layout
    return sg.Window('Number Guessing Game', layout)


def main():
    """
    Main game loop that manages the GUI interaction and game logic.
    
    This function:
    1. Creates the game window
    2. Initializes game variables (secret number, attempts, game state)
    3. Enters an event loop that handles user interactions
    4. Updates the UI based on player actions and game state
    5. Manages game reset and exit operations
    """
    # Create the main window with all UI elements
    window = create_window()
    
    # Generate a random secret number between 1 and 100 for the player to guess
    secret_number = random.randint(1, 100)
    
    # Initialize attempts counter to track the number of guesses made
    attempts = 0
    
    # Flag to track if the game is over (player guessed correctly)
    game_over = False
    
    # Initialize output text that will display in the multiline output box
    output_text = "Game started! Make your first guess.\n"
    
    # Main event loop - continues until window is closed or Exit button is clicked
    while True:
        # Read events and values from the window
        # event: The button/element that triggered this read
        # values: Dictionary containing current values of input fields
        event, values = window.read()
        
        # Check if window was closed or Exit button was clicked
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        
        # Handle "New Game" button click - reset all game variables for a fresh game
        if event == 'New Game':
            # Generate a new random secret number
            secret_number = random.randint(1, 100)
            
            # Reset attempts counter
            attempts = 0
            
            # Reset game_over flag to allow new guesses
            game_over = False
            
            # Reset output text to initial message
            output_text = "Game started! Make your first guess.\n"
            
            # Update the OUTPUT display with initial message
            window['OUTPUT'].update(output_text)
            
            # Update the ATTEMPTS counter display
            window['ATTEMPTS'].update('Attempts: 0')
            
            # Clear the input field for new game
            window['GUESS'].update('')
        
        # Handle "Submit" button click - only process if game is not over
        if event == 'Submit' and not game_over:
            try:
                # Get the player's guess from the input field and convert to integer
                guess = int(values['GUESS'])
                
                # Validate that guess is within the valid range (1-100)
                if guess < 1 or guess > 100:
                    output_text += "Please enter a number between 1 and 100.\n"
                else:
                    # Increment attempts counter for valid guess
                    attempts += 1
                    
                    # Compare guess with secret number and provide feedback
                    if guess < secret_number:
                        # Player's guess is too low
                        output_text += f"Attempt {attempts}: {guess} - Too low! Try again.\n"
                    elif guess > secret_number:
                        # Player's guess is too high
                        output_text += f"Attempt {attempts}: {guess} - Too high! Try again.\n"
                    else:
                        # Player guessed correctly!
                        output_text += f"Attempt {attempts}: {guess} - CORRECT! 🎉\n"
                        output_text += f"You guessed the number in {attempts} attempts!\n"
                        
                        # Set game_over flag to prevent further guesses
                        game_over = True
                    
                    # Update the OUTPUT display with new feedback
                    window['OUTPUT'].update(output_text)
                    
                    # Update the ATTEMPTS counter with new total
                    window['ATTEMPTS'].update(f'Attempts: {attempts}')
                    
                    # Clear the input field for next guess
                    window['GUESS'].update('')
            
            except ValueError:
                # Handle case where user entered non-integer input
                output_text += "Invalid input! Please enter a valid number.\n"
                window['OUTPUT'].update(output_text)
        
        # Clear the input field after each event (prevents duplicate input)
        window['GUESS'].update('')
    
    # Close the window when exiting the event loop
    window.close()


# Entry point: Execute main() when script is run directly (not imported)
if __name__ == '__main__':
    main()