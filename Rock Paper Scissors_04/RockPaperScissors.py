rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game_images = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user>=0 and user<=2:
    print("You choose:")
    print(game_images[user])

computer = random.randint(0,2)
print("Computer choose:")
print(game_images[computer])

if user==computer:
    print("It's a Tie")

elif user==0 and computer==2:
    print("You win!")

elif user< computer:
    print("You lost")

elif user==2 and computer==0:
    print("You lost")

elif user>computer:
    print("You win!")

else:
    print("Invalid input.Please enter a correct input out of 0,1,2")