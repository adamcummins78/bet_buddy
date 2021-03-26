import datetime
from countdown import cfbCountDown
from scraper import ga_def, ga_off, ky_def, ky_off, al_def, al_off, ten_def, ten_off

def buildMenu(): 
    user = input("Please enter your name:  ")
    while(True):
        print("\n")
        print("=" * 54)
        print("=" * 21 + " BET BUDDY " + "=" * 22)
        print("=" * 54)
        print(f"Welcome to Bet Buddy, {user}! (College Football Edition)")
        print()
        cfbCountDown() #I want this section to print out what week of the college football season it is based of datetime entry
        print("=" * 54)
        print("=" * 54)
        print("=" * 54)
        print("Selection:\n Kentucky (Enter: UK)\n Georgia (Enter: UGA)\n Alabama (Enter: AL)\n Tennesse (Enter: TN)")

        team = input("Please enter the number for first team you would like to compare, or q to quit:  ").upper()
        if(team == "Q"):
            exit()
        team_two = input("Please enter the second team you would like to compare:  ").upper()

        
        if (team == "UK"):
            print(f"UK is averaging {ky_off} yards on offense so far this year and on average allowing {ky_def} yards on defense.")
        elif (team == "UGA"):
            print(f"Georgia is averaging {ga_off} yards on offense so far this year and on average allowing {ga_def} yards on defense.")
        elif (team == "AL"):
            print(f"Alabama is averaging {al_off} yards on offense so far this year and on average allowing {al_def} yards on defense.")
        elif (team == "TN"):
            print(f"Tennesse is averaging {ten_off} yards on offense so far this year and on average allowing {ten_def} yards on defense.")
        else:
            print("Invalid option")
        

        if (team_two == "UK"):
            print(f"UK is averaging {ky_off} yards on offense so far this year and on average allowing {ky_def} yards on defense.")
        elif (team_two == "UGA"):
            print(f"Georgia is averaging {ga_off} yards on offense so far this year and on average allowing {ga_def} yards on defense.")
        elif (team_two == "AL"):
            print(f"Alabama is averaging {al_off} yards on offense so far this year and on average allowing {al_def} yards on defense.")
        elif (team_two == "TN"):
            print(f"Tennesse is averaging {ten_off} yards on offense so far this year and on average allowing {ten_def} yards on defense.")
        else:
            print("Invalid option")

        print("\n")
        print("Happy Betting!")
        print("\n")