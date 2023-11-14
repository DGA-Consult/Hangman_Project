import random

# Creating a list of fruit names
word_list = ['Apple', 'Banana', 'Orange', 'Grapes', 'Mango']

# Printing the list
print(word_list)

# Using random.choice to select a random fruit
word = random.choice(word_list)

# Printing the random word
print(word)

# Using the input function to get a single letter from the user
guess = input("Enter a single letter: ")

# Checking if the input is a single alphabetical character
if len(guess) == 1 and guess.isalpha():
    # If the conditions are met, print "Good guess!"
    print("Good guess!")
else:
    # If the conditions are not met, print "Oops! That is not a valid input."
    print("Oops! That is not a valid input.")
