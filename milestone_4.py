import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        # self.guesses = set()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word.lower()))
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        # Convert the guess to lowercase
        guess = guess.lower()

        # Checking if the input is a valid guess
        if len(guess) == 1 and guess.isalpha() and guess not in self.list_of_guesses:
            # Checking if the guessed letter is in the word
            if guess in self.word.lower():
                print("Good guess! The letter is in the word.")
                # Update the word_guessed list with the correct guess
                for i, letter in enumerate(self.word):
                    if letter.lower() == guess:
                        self.word_guessed[i] = letter
            else:
                print("Oops! The letter is not in the word.")
                # Deduct a life for incorrect guesses
                self.num_lives -= 1
                print(f"Lives remaining: {self.num_lives}")

            # Add the guess to the list_of_guesses
            self.list_of_guesses.append(guess)
            # Returning True if the guess is valid
            return True
        else:
            print("Oops! That is not a valid or repeated input.")
            # Returning False if the guess is not valid
            return False

    def ask_for_input(self):
        # Running the game in a continuous loop
        while self.num_lives > 0:
            # Displaying the word_guessed and the list of guesses
            print("Word Guessed:", ' '.join(self.word_guessed))
            print("List of Guesses:", ', '.join(self.list_of_guesses))

            # Getting a single letter guess from the user
            guess = input("Enter a single letter: ")

            # Check if the guess is not a single alphabetical character
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
                continue

            # Check if the guess is already in the list_of_guesses
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                continue

            # Calling the check_guess method with the user's guess
            if self.check_guess(guess):
                # Check if the word has been completely guessed
                if '_' not in self.word_guessed:
                    print("Congratulations! You guessed the word:", self.word)
                    break

        # Display a message if the player runs out of lives
        if self.num_lives == 0:
            print("Game over! You ran out of lives. The correct word was:", self.word)

if __name__ == "__main__":
    # Creating an instance of the Hangman class
    hangman_game = Hangman(word_list=['apple', 'banana', 'orange', 'grapes', 'mango'])

    # Calling the ask_for_input method to start the game
    hangman_game.ask_for_input()

