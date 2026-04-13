import PySimpleGUI as sg
import random

# Set theme
sg.theme('DarkBlue3')

def create_window():
    layout = [
        [sg.Text('Number Guessing Game', font=('Arial', 20, 'bold'))],
        [sg.Text('Guess a number between 1 and 100', font=('Arial', 12))],
        [sg.Text('')],
        [sg.Text('Your Guess:', font=('Arial', 11)), sg.InputText(size=(10,), key='GUESS', font=('Arial', 11))],
        [sg.Button('Submit', size=(10,)), sg.Button('New Game', size=(10,)), sg.Button('Exit', size=(10,))],
        [sg.Text('')],
        [sg.Multiline(size=(40, 10), key='OUTPUT', disabled=True, font=('Arial', 10))],
        [sg.Text('Attempts: 0', key='ATTEMPTS', font=('Arial', 11, 'bold'))]
    ]
    return sg.Window('Number Guessing Game', layout)

def main():
    window = create_window()
    secret_number = random.randint(1, 100)
    attempts = 0
    game_over = False
    output_text = "Game started! Make your first guess.\n"
    
    while True:
        event, values = window.read()
        
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        
        if event == 'New Game':
            secret_number = random.randint(1, 100)
            attempts = 0
            game_over = False
            output_text = "Game started! Make your first guess.\n"
            window['OUTPUT'].update(output_text)
            window['ATTEMPTS'].update('Attempts: 0')
            window['GUESS'].update('')
        
        if event == 'Submit' and not game_over:
            try:
                guess = int(values['GUESS'])
                
                if guess < 1 or guess > 100:
                    output_text += "Please enter a number between 1 and 100.\n"
                else:
                    attempts += 1
                    
                    if guess < secret_number:
                        output_text += f"Attempt {attempts}: {guess} - Too low! Try again.\n"
                    elif guess > secret_number:
                        output_text += f"Attempt {attempts}: {guess} - Too high! Try again.\n"
                    else:
                        output_text += f"Attempt {attempts}: {guess} - CORRECT! 🎉\n"
                        output_text += f"You guessed the number in {attempts} attempts!\n"
                        game_over = True
                    
                    window['OUTPUT'].update(output_text)
                    window['ATTEMPTS'].update(f'Attempts: {attempts}')
                    window['GUESS'].update('')
            
            except ValueError:
                output_text += "Invalid input! Please enter a valid number.\n"
                window['OUTPUT'].update(output_text)
        
        window['GUESS'].update('')
    
    window.close()

if __name__ == '__main__':
    main()