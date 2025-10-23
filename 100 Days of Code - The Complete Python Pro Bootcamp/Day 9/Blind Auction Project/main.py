# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo,"\n")

bidders = {}
more_bidders = 'yes'
highest_bid = 0
highest_bidder = None

while more_bidders == 'yes':
    name = input("What is your name? \n")
    bid = int(input("What is your bid? \n"))

    bidders[name] = bid
    more_bidders = (
        input("Are there any other bidders? Type yes or no \n").lower())
    print("\n" * 20)

for key,value in bidders.items():
    if bidders[key] > highest_bid:
        highest_bid = bidders[key]
        highest_bidder = key

print(bidders)
print(f'{highest_bidder} at ${highest_bid}')