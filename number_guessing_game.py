import random

# Loop
while True:
    # Ask the user to guess a number between 1 and 100
    user_input = input('Try to guess the number between 1 and 100: ')

    # Check if the user entered a valid number
    if not user_input.isdigit():
        print("Error: Please enter a valid number.")
        continue  # If it's not a number, prompt the user to guess again

    # Convert the input to an integer
    userNumber = int(user_input)

    # Make sure the number is within the valid range
    if userNumber < 1 or userNumber > 100:
        print('Please choose a number between 1 and 100.')
        continue

    # Generate a random number between 1 and 100
    randomNumber = random.randint(1, 100)

    # Compare the user's guess with the random number
    if userNumber < randomNumber:
        print('Too low! Try again.')
    elif userNumber > randomNumber:
        print('Too high! Try again.')
    else:
        print('You got it! Congratulations!!!')
        break




