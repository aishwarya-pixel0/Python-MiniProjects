logo = r'''
 ____                     _        _              _   _             
/ ___|  ___  ___ _ __ ___| |_     / \  _   _  ___| |_(_) ___  _ __  
\___ \ / _ \/ __| '__/ _ \ __|   / _ \| | | |/ __| __| |/ _ \| '_ \ 
 ___) |  __/ (__| | |  __/ |_   / ___ \ |_| | (__| |_| | (_) | | | |
|____/ \___|\___|_|  \___|\__| /_/   \_\__,_|\___|\__|_|\___/|_| |_|
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bid={}

def highest_bidder(bidding_dictionary):
      highest_bid=0
      winner=""
      for bidder in bidding_dictionary:
            #getting hold of the bid of each bidder in the dictionary
            bid_amount = bidding_dictionary[bidder]
            if bid_amount>highest_bid:
                  highest_bid=bid_amount
                  winner = bidder
      print(f"The winner is {winner} with the highest amount of {highest_bid}")

should_continue=True
while should_continue:
      name = input("What is your name? ")
      price = int(input("What is your bid?$ "))
      bid[name]=price
      other = input("Are there any other bidders? Type yes or no\n").lower()
      if other=="no":
            should_continue=False
            highest_bidder(bid)
      elif other=="yes":
            print("\n"*10)

            
