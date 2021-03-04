import datetime

user = input("Please enter your name:  ")
print("\n")
print("=" * 54)
print("=" * 21 + " BET BUDDY " + "=" * 22)
print("=" * 54)
print(f"Welcome to Bet Buddy, {user}! (College Football Edition)")
print()
print("   It is WEEK ONE of the college football season.") #I want this section to print out what week of the college football season it is based of datetime entry
print("=" * 54)
print("=" * 54)
print("=" * 54)
print("\n")

while(True):
    team = input("Please enter the first team you would like to compare, or q to quit:  ")
    if(team == "q"):
        exit()
    team_two = input("Please enter the second team you would like to compare:  ")
    print("\n")
    print("Happy Betting!")
    print("\n")
    
    
    

