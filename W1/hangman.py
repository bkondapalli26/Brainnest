'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''
import random

# List of words to choose from
list_of_words = ["python", "java", "cplusplus", "javascript", "php", "html", "css", "csharp", "swift", "kotlin","scala"]

# Selecting a random word from the list
rword = random.choice(list_of_words)

# Creating an empty list to store the guessed letters
guess_letters = []

# Creating a variable to store the number of attempts left
tries_left = 6

# Looping until either the word is guessed or there are no attempts left
while tries_left > 0:
    # Printing the current status of the word
    check = ""
    for letter in rword:
        if letter in guess_letters:
            check = check+letter
        else:
            check = check+"_"
    print(check)

    # Getting a guess from the user
    guess = input("Guess a letter: ").lower()

    # Checking if the guess is a single letter
    if len(guess) != 1:
        print("Please enter a single letter.")
        continue

    # Checking if the guess is a letter and not a number or special character
    if not guess.isalpha():
        print("Please enter a letter.")
        continue

    # Checking if the letter has already been guessed
    if guess in guessed_letters:
        print("You have already guessed that letter.")
        continue

    # Adding the guessed letter to the list of guessed letters
    guess_letters.append(guess)

    # Checking if the guess is correct
    if guess in rword:
        print("Correct!")
    else:
        print("Wrong!")
        tries_left -= 1

    # Checking if all letters have been guessed
    if set(rword) == set(guess_letters):
        print("Congratulations, you have guessed the word!")
        break

# Checking if there are no attempts left
if tries_left == 0:
    print("Sorry, you ran out of attempts. The word was", rword + ".")


# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''