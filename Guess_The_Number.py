from art import logo
import random
import os

HARD_ATTEMPTS = 5
EASY_ATTEMPTS = 10


def set_difficulty():
    options = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if options == 'easy':
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS
    
    
def compare(guess, answer, turns):
    if guess < answer:
        print("Too low")
        return turns - 1
    elif guess > answer:
        print("Too high")
        return turns - 1
    else:
        print(f"You got it. the answer is {answer}")
    
    
def play_game():
    os.system("cls")
    print(logo)
    print("Welcome to the Number Guessing Game!.")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"psst, the answer is {answer}")
    
    turns = set_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"You have {turns} remaining attempts")
        
        guess = int(input("Make a guess: "))
        
        turns = compare(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again")
    
play_game()