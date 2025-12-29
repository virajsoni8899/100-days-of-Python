import os
print("Welcome to the auction program!")


name = input("What is your name?")
bid = float(input("What is your bid?"))
other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
auction_data = {}

auction_data[name] = bid


while other_bidders == "yes":
    os.system('cls')
    name = input("what is your name?")
    bid = float(input("what is your bid?"))
    auction_data[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if other_bidders == "yes":
        os.system('cls')

if auction_data:
    winner = max(auction_data, key=auction_data.get)
    highest_bid = auction_data[winner]
    print(f"The winner is {winner} with a bid of {highest_bid}")

