from milestone_2 import word

#function to check the user guess
def check_guess(guess):
    # convert user input into lower case
    guess = guess.lower()

    # Checking if the input is a valid guess
    if len(guess) == 1 and guess.isalpha():

        # Checking if the guessed letter is in the word
        if guess in word.lower():
            print("Good guess! The letter is in the word.")
        else:
            print("Oops! The letter is not in the word.")
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

# Function to ask for user input
def ask_for_input():

    # running a continuous loop
    while True:

        # Getting a single letter guess from the user
        user_guess = input("Enter a single letter: ")

        # Calling the check_guess function with the user's guess
        if check_guess(user_guess):
            # Exiting the loop if the guess is valid
            break

# Calling the ask_for_input function to start the game
ask_for_input()