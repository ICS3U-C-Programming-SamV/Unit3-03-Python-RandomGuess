#!/usr/bin/env python3
# Created By: Sam V
# Date: Oct 13th, 2026
# A number guessing game with a loop to let the user try again.

import random


def main() -> None:
    """Run the random number guessing game."""
    random_number = random.randint(0, 100)

    print("Welcome to the Random Number Guessing Game!")
    print("I have selected a number between 0 and 100. Try to guess it!")

    try:
        user_input = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input; please enter an integer.")
        return

    if user_input == random_number:
        print("You Guessed Correctly!")
    else:
        print("You Guessed Wrong. The correct number was:", random_number)

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
