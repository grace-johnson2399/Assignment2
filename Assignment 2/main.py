import numpy as np
import random


def print_header():
    print("\t What is the number you want the computer to guess?!")
    print("\t Your number must be between 1 and 100")
    print("\t If your number is higher type h, if your number is lower type l.")


def main():
    # prints the greeting banner
    print_header()

    your_number = int(input("What is your number:"))
    computer_guess = np.random.randint(1, 100)
    max_guess = 101
    min_guess = 0

    while True:
        print("The computer guess is:", computer_guess, "Your number is:", your_number)
        response = input()
        response.lower()
        if response == "h":
            min_guess = computer_guess
            computer_guess = ((min_guess + 1 + max_guess - 1) // 2)
        if response == "l":
            max_guess = computer_guess
            computer_guess = ((min_guess + 1 + max_guess - 1) // 2)
        if response == "You got it!":
            print("I knew I would out smart you!")
            print("Thanks for playing!")
            break
