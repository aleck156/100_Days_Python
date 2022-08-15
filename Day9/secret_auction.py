import os
from art import logo

print(logo)

auction_house = []
incoming_users = True

def find_highest_bidder(bidding_records):
    highest_bidder = auction_house[0]
    for index in range (1, len(auction_house)):
        if auction_house[index]['bid'] > highest_bidder['bid']:
            highest_bidder = auction_house[index]
    return highest_bidder

while incoming_users:
    name = input("Enter your name: ")
    bid = int(input('Enter your bid: $'))
    auction_house.append({
        'username': name,
        'bid': bid
    })

    answer = input('Are there any other users who want to bid [y/n]?: ')
    if answer == 'n':
        incoming_users = False
    else:
        os.system('clear')

highest_bidder = find_highest_bidder(auction_house)
print(f'Thie highest bidder was {highest_bidder["username"]}, with the bid of {highest_bidder["bid"]}')
