# Variables  # Uncomment to run

print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")


character_name = "ACE"
character_age = "20"

print("There was a man named " + character_name + ", ")
print("he was " + character_age + " years old")
print("he really liked the name " + character_name + ", ")
print ("but didn't like being " + character_age + ".")


# Strings
# Upper Cases and Lower Cases
phrase = "Giraffe Academy"
print(phrase.upper())
print(phrase.lower())
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper().isupper())
print(phrase.lower().islower())

# Dealing with Numbers in a String
print(len(phrase))
print(phrase[0])  # Strings get indexed starting from 0
print(phrase.index("A"))  # Returns the index of the first occurrence of the character

print (phrase.replace("Giraffe", "Elephant"))  # Replaces the first string with the second string in the variable


# Working with Numbers
from math import *

my_num = 5

print (str(my_num) + " is my favorite number")  # Converts the number into a string

print(abs(my_num))  # Returns the absolute value of the number

print (pow(3, 2))  # Raises the first number to the power of the second number

print (round(3.7))  # Rounds the number to the nearest integer

print (floor(3.7))  # Rounds the number down to the nearest integer

print (ceil(3.7))  # Rounds the number up to the nearest integer

print (sqrt(36))  # Returns the square root of the number


# Getting input from the users

name = input("Enter your name:  ")
age = input("Enter your age:  ")
print("Hello " + name + "! You are " + age + " years old.")