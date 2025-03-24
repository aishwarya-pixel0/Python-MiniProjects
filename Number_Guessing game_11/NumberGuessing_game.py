logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
print(logo)
import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5




def check_answer(user_guess,actual_answer,turns):
    if user_guess > actual_answer:
        print("Too High")
        return turns-1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You guessed it right, the number is indeed {actual_answer}!")

def set_difficulty():
    level = input("Choose a difficulty.Type 'easy' or 'hard': ").lower()
    if level=="easy":
        return EASY_LEVEL_TURNS
    elif level=="hard":
        return HARD_LEVEL_TURNS
    else:
        print("Enter correct input")

def game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    answer = random.randint(1,100)
    turns = set_difficulty()
    guess=0
    while guess!=answer:
        print(f"You have {turns} remaining")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")



game()
