#!/usr/bin/env python3
# Created By: Sam V
# Date: Oct 13th, 2026
# A number guessing game with a loop to let the user try again.

import random
# Generate a random number between 0 and 100
random_number = random.randint(0, 100)

print("Welcome to the Random Number Guessing Game!")
print("I have selected a number between 0 and 100. Try to guess it!")

# Get The User's Guess and convert it from a string to an integer
user_input = input("Enter your guess:")
user_input = int(user_input)

# Check if the input is a valid integer and correctly guess the random number

if user_input == random_number:
    print("You Guessed Correctly!")
else:
    print("You Guessed Wrong. The correct number was:", random_number)