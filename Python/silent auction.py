import os

#clear console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


print("Welcome to Miguelito's Silent Auction Program\n")
x=input("Press enter")
clearConsole()


bidding={}
game_done = False
while not game_done:

  name=str(input("Please input your name: \n")).lower()
  price=int(input("What is your bidding price? $"))

  #if bidder makes an existing bid
  price_duplicate=False
  while not price_duplicate:
    if price in bidding.values():
      print("This amount is already bidded")
      price=int(input("Input your bidding price again $"))
    else:
      price_duplicate=True


  #name and bid will be stored here
  bidding[name]=price


#going to ask if are there other bidders. if yes go back to input  
  clearConsole()
  bidders=str(input("Are there other bidders? type yes or no: ")).lower()
  if bidders =="no":
    game_done = True
    winner=max(bidding, key=bidding.get)
    highest_bid=str(max(bidding.values()))
    print(f"The winner is {winner} with amount of ${highest_bid}")


  elif bidders=="yes":
    clearConsole()
  else:
    print("Type appropriately")