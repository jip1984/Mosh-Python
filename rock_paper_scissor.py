import random

#dictionary
emojis = {'r': '🪨', 's': '✂️', 'p': '📃'}
choices = ('r', 'p', 's')

while True:

    # Ask the user to choose rock, paper or scissors
    user_choice = input('Welcome, ROCK, PAPER or SCISSORS? (r/p/s): ').lower()

    # If choice is not valid
    #    print an error
    # if user_choice != 'r' and user_choice != 'p' and user_choice != 's':
    #     print('Invalid choice')
    if user_choice not in choices:
        print('Invalid choice')
        continue
    # computers choice
    computer_choice = random.choice(choices)


    #print choices (emojis)
    print(f'You chose: {emojis[user_choice]}')
    print(f'Computer chose: {emojis[computer_choice]}')

    #determine winner
    if user_choice == computer_choice:
        print('Its a draw')
    elif ( 
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or 
        (user_choice == 'p' and computer_choice == 'r')):
        print('You win!!!')
    else:
        print('You lose') 
    # want to continue
    should_continue = input('Want to continue? (y/n): ').lower()
    #if not terminate
    if should_continue == 'n':
        break
