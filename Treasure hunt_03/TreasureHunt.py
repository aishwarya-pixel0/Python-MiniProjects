print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
user_input = input("You are at a cross road.Where do you want to go\n Type left or right\n").lower()
if user_input == "left":

         print("You've come to a lake. There is an island in the middle of the lake.\n")
         choice2 = input("Type wait to wait for a boat. Type swim to swim across.\n").lower()
         if choice2=="wait":
             print("You arrive at the island unharmed. There is a house with 3 doors.\n")
             choice3 = input("One red, one yellow and one blue. Which colour do you choose?\n").lower()
             if choice3=="red":
                 print("It's a room full of fire. Game Over.")
             elif choice3=="yellow":
                 print("You found the treasure! You Win!")
             else:
                 print("You enter a room of beasts. Game Over.")
         else:
             print("You get attacked by an angry trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")