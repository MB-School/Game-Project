# Lab 1
# Author: Marcos Bezerra
# Date: 09/28/2026

import random

NAMES = {1: "paper", 2: "scissors", 3: "rock"}
# Each key beats its value: paper covers rock, scissors cut paper, rock crushes scissors
BEATS = {1: 3, 2: 1, 3: 2}
REASONS = {
    (1, 3): "paper covers rock",
    (2, 1): "scissors cut paper",
    (3, 2): "rock crushes scissors",
}


def ask_yes_no(prompt):
    """Ask a yes/no question and return True for yes, False for no."""

    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter Y or N.")


def get_choice():
    """Ask the user to pick 1, 2 or 3 and keep asking until the input is valid."""

    while True:
        text = input("Enter your choice: 1. paper, 2. scissors, 3. rock: ").strip()
        if text in ("1", "2", "3"):
            return int(text)
        print("Invalid choice. Please enter 1, 2 or 3.")


def rps_game():
    """Play Rock-Paper-Scissors, repeating until the user chooses to stop.

    The computer generates a random number (1, 2, 3) and the user picks a number
    too. The program compares them, says who won (or if it is a tie), and
    explains why. Paper beats rock, scissors beat paper, and rock beats scissors.

    """
    if not ask_yes_no("Do you want to play? (Y/N): "):
        return

    playing = True
    while playing:
        user = get_choice()
        computer = random.randint(1, 3)
        print(f"You chose {NAMES[user]}. The computer chose {NAMES[computer]}.")

        if user == computer:
            print("It is a tie!")
        elif BEATS[user] == computer:
            print(f"You win! {REASONS[(user, computer)].capitalize()}.")
        else:
            print(f"You lose! {REASONS[(computer, user)].capitalize()}.")

        playing = ask_yes_no("Do you want to play again? (Y/N): ")


if __name__ == "__main__":
    rps_game()
