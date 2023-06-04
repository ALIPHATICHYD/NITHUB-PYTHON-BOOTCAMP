"""
Write a program to simulate the famous rock-paper-scissors game


Rules:
Rock wins Scissors
Scissors wins Paper
Paper wins Rock

Hint.
1. There are two user: A human and a computer 
2. The python random module to generate computer's play
3. When user type in "q" or "quit", you should end the game.

Bonus.
Keep track of the score
"""


import random

choices = ["rock", "paper", "scissors"]
score = {"human": 0, "computer": 0}

def determine_winner(human_choice, computer_choice):
    if human_choice == computer_choice:
        return "tie"
    elif (
        (human_choice == "rock" and computer_choice == "scissors") or
        (human_choice == "scissors" and computer_choice == "paper") or
        (human_choice == "paper" and computer_choice == "rock")
    ):
        return "human"
    else:
        return "computer"

def play_game():
    global score
    while True:
        print("\nLet's play Rock-Paper-Scissors!")
        print("Enter your choice (rock, paper, or scissors), or 'q' to quit:")
        human_choice = input().lower()

        if human_choice == "q" or human_choice == "quit":
            break

        if human_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print("Computer chooses:", computer_choice)

        winner = determine_winner(human_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "human":
            print("You win!")
            score["human"] += 1
        else:
            print("Computer wins!")
            score["computer"] += 1

        print("Score: Human -", score["human"], "Computer -", score["computer"])

play_game()
print("\nThanks for playing!")


# In this program, the choices list stores the available options of rock, paper, and scissors. The score dictionary keeps track of the score for the human and computer players.

# The determine_winner function compares the choices made by the human and computer to determine the winner based on the game rules.

# The play_game function runs the main game loop. It prompts the human player for their choice and generates a random choice for the computer player using the random.choice function. It then determines the winner and updates the score accordingly. The game continues until the human player enters "q" or "quit" to end the game.

# After the game ends, the program displays the final score.