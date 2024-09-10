import random

#loop
while True:

    # Ask: roll the dice?
    choice = input('Shall I roll the dice? (y/n): ').lower()

    # if user enters y
    if choice == 'y':
    # generate to random numbers for 2 dice
     die1 = random.randint(1, 6)
     die2 = random.randint(1, 6)
    # print them
     print(f'You rolled a ({die1} and a {die2})')
    # if user enters n
    elif choice == 'n':
      # print thank you message
     print('Thanks for playing')
     # terminate
     break
        # else
    else: 
    # print error message
      print('Invalid choice please use y/n')
   