import random

#dictionary
emojis = {'r': '🪨', 's': '✂️', 'p': '📃'}
choices = ('r', 'p', 's')

  # Ask the user to choose rock, paper or scissors
def get_user_choice():
    choices = ['r', 'p', 's']  # Valid choices: 'r' for Rock, 'p' for Paper, 's' for Scissors
    while True:
        user_choice = input('Welcome, Rock, Paper, or Scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice  # Return valid choice
        else:
            print('Invalid choice, please choose r, p, or s.')


def display_choices(user_choice, computer_choice):
    print(f'You chose: {emojis[user_choice]}')
    print(f'Computer chose: {emojis[computer_choice]}')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Its a draw')
    elif ( 
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or 
        (user_choice == 'p' and computer_choice == 'r')):
        print('You win!!!')
    else:
        print('You lose') 

def play_game():
    while True:
        #users choice
        user_choice = get_user_choice()
        # computers choice
        computer_choice = random.choice(choices)
        #print choices (emojis)
        display_choices(user_choice, computer_choice)
        #determine winner
        determine_winner(user_choice, computer_choice)
        # want to continue
    
            # want to continue
        should_continue = input('Want to continue? (y/n): ').lower()
            #if not terminate
        if should_continue == 'n':
            break

play_game()