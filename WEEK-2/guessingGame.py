# Building a Guessing Game in Python

# Structures that will be used in order to build this Guessing Game
# If Statements, While Loops, Variables

# Basic Idea: A Secret word will be specified, a secret word that will be stored inside the program, then the user can interact with the program and try to guess the secret word.

# Creating a Variables to store the secret word

secret_word = "ALPHA"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

# Creating a while loop and if statements when the user inputs a wrong guess
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!") 