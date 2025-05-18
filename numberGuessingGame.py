# Jeffrey Ponce Lopez
# Cognizant GenAI Externship
# Project: Number Guessing Game


# Generate random number and store to number_to_guess and variable storing the number of guesses
import random
number_to_guess = random.randint(1, 100)
numberOfGuesses = 1

# Infinite Loop because don't know how many times we need to loop
while 1 == 1:
    userGuess = int(input("Enter Guess Here: "))                        # user input
    if userGuess != number_to_guess:                                    # users guess doesn't match desired number
        if userGuess > number_to_guess and numberOfGuesses < 10:        # user guess is too high and within 10 guesses
            print("Sorry, Your Guess was too High, Try Again. \n")
        elif userGuess < number_to_guess and numberOfGuesses < 10:      # user guess is too low and within 10 guesses
            print("Sorry, Your Guess was too Low, Try Again. \n")
        else:
            print("Game Over. Better Luck Next Time. :(")               # if the number exceeds 10 guesses (given that guess is wrong)
            break                                                       # then end the loop and display game over message

        numberOfGuesses += 1
    else:                                                               # else (guess is correct) break loop and display win message
        print(f"Congratulations! You Guessed Correctly, it only took {numberOfGuesses} attempts!")
        break