
from art import logo

bids  = {}
MorePeople = True

def findhighestbid(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while MorePeople:
  print(logo)
  name = str(input("What is your Name?: "))
  bid = int(input("How much would you like to Bid?: $"))
  bids[name] = bid
  ismore = str(input("Are there more people? 'y'/'n': "))
  if ismore == "y":
    MorePeople = True
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  elif ismore == "n":
    MorePeople = False
    findhighestbid(bids)
