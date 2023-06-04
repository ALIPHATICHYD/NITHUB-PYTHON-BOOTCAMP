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