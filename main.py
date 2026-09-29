# Lab 1
# Author: Marcos Bezerra
# Date: 09/28/2026

from guessing import guessing_game
from rps import rps_game


def welcome():
    """Print a welcome message explaining what the program does and how it works."""

    print("=" * 50)
    print("Welcome to the Game Center!")
    print("You can play two games:")
    print("  1. Guessing Game: guess a secret number in 5 tries.")
    print("  2. Rock-Paper-Scissors: play against the computer.")
    print("Pick a game by typing its number. After each game")
    print("you can play again, switch games, or quit.")
    print("=" * 50)


def choose_game():
    """Ask the user which game to play and return 1 or 2."""

    while True:
        choice = input("Which game do you want to play? 1. Guessing Game, 2. Rock-paper-scissors: ").strip()
        if choice in ("1", "2"):
            return int(choice)
        print("Please enter 1 or 2.")


def after_game():
    """Ask what to do after a game and return 'again', 'switch' or 'quit'."""

    while True:
        choice = input("Play the same game again (A), switch games (S), or quit (Q)? ").strip().lower()
        if choice in ("a", "again"):
            return "again"
        if choice in ("s", "switch"):
            return "switch"
        if choice in ("q", "quit"):
            return "quit"
        print("Please enter A, S or Q.")


def main():
    """Run the program: show the welcome message, then let the user play games until they quit."""

    welcome()
    game = choose_game()
    while True:
        if game == 1:
            guessing_game()
        else:
            rps_game()

        action = after_game()
        if action == "quit":
            print("Thanks for playing. Goodbye!")
            break
        if action == "switch":
            game = choose_game()


if __name__ == "__main__":
    main()
