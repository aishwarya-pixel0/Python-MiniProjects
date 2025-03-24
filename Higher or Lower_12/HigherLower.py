logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
from game_data import data
import random


def format_data(account):
    acc_name = account["name"]
    acc_desc = account["description"]
    acc_country = account["country"]
    return f"{acc_name}, a {acc_desc},from {acc_country}"

def check_answer(user_guess,a_followers,b_followers):
    if a_followers > b_followers:
        return user_guess=="a"
    else:
        return user_guess=="b"


print(logo)
score=0
game_should_continue=True
acc_b = random.choice(data)

while game_should_continue:
    acc_a = random.choice(data)
    acc_b = random.choice(data)
        #checking if both the randomly generated accounts are similar then reset the account b to a new randomly generated value
    if acc_a == acc_b:
        acc_b = random.choice(data)

    print(f"Compare A:{format_data(acc_a)}")
    print(vs)
    print(f"Against B:{format_data(acc_b)}")

    guess = input("Who has more followers? Type 'A' or 'B' ").lower()
    print("\n" * 20)
    print(logo)

    a_follower_count = acc_a["follower_count"]
    b_follower_count = acc_b["follower_count"]

    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    if is_correct:
        score+=1
        print(f"You got it right! Current Score is {score}")
    else:
        print(f"Tough Luck,your current score {score}")
        game_should_continue=False
