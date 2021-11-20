from replit import clear
import art

print(art.logo)
print("Welcome to the Secret Auction Program \n")

flag = True

auction = {}
while flag:
    
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    auction[name] = bid

    choice = input("Are there any other bidders? Type 'yes or 'no'.\n")

    if choice == 'no':
        flag = False
    
    clear()
    
max_key = max(auction, key = auction.get)

(f"The winner is {max_key} with a bid of ${auction[max_key]}")


