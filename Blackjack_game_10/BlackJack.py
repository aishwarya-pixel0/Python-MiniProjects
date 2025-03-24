import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
        #deals a random card
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card



def calculate_score(cards):
        #takes a list of cards a returns the score calculated from the cards
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        #if the user score is above 21 then remove ace of 11 and add ace of 1
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

def compare(u_score,c_score):
        if u_score==c_score:
            return "Draw"
        elif c_score==0:
            return "You went over. You Lost"
        elif u_score==0:
            return "Win with a blackjack.!"
        elif u_score>21:
            return "You went over.You Lost!"
        elif c_score>21:
            return "Opponent went over. You Win!"
        elif u_score>c_score:
            return "You Won!"
        else:
            return "You Lost!"

def play_game():
    print(logo)
    user_cards=[]
    computer_cards=[]
    #debugging process
    computer_score=-1
    user_score=-1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards},current_score: {user_score}")
        print(f"Computer's first card:{computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or type 'n' to pass  ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    #as 0 represents blackjack hence the computer score while not 0
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand is:{user_cards} and final score is: {user_score}")
    print(f"Computer's final hand is:{computer_cards} and final score is:{computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        print("\n" * 20)
        play_game()




