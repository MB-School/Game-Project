# Lab 1
# Author: Marcos Bezerra
# Date: 09/28/2026

import random


def get_guess(prompt):
    """Ask the user for a whole number and keep asking until they enter one."""

    while True:
        text = input(prompt).strip()
        try:
            return int(text)
        except ValueError:
            prompt = "Please enter a whole number: "


def ask_play_again():
    """Ask the user if they want to play again and return True for yes, False for no."""

    while True:
        answer = input("Do you want to play again? (Y/N): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter Y or N.")


def guessing_game(low=1, high=100, tries=5):
    """Play the Guessing Game, repeating until the user chooses to stop.

    A random number between low and high is picked and the user gets a set
    number of tries to guess it. After each wrong guess the program says if the
    guess was too high or too low. If the user runs out of tries, the program
    prints what the number was. After each round the user is asked if they want
    to play again.
    """
    playing = True
    while playing:
        number = random.randint(low, high)
        print(f"I'm thinking of a number between {low} and {high}.")
        guess = get_guess(f"Guess what it is. You have {tries} tries: ")
        tries_left = tries - 1
        won = False

        while True:
            if guess == number:
                print("You got it!")
                won = True
                break
            if tries_left == 0:
                break
            hint = "low" if guess < number else "high"
            word = "try" if tries_left == 1 else "tries"
            guess = get_guess(f"Nope! Too {hint}. Try again ({tries_left} {word} left): ")
            tries_left -= 1

        if not won:
            print(f"Nope! You lost. The number was {number}")

        playing = ask_play_again()


if __name__ == "__main__":
    guessing_game()
