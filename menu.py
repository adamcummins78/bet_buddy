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
        print("Selection:\n1. Kentucky\n2. Gerogia\n3. Alabama\n4. Tennesse")

        team = input("Please enter the number for first team you would like to compare, or q to quit:  ")
        if(team == "q"):
            exit()
        team_two = input("Please enter the second team you would like to compare:  ")
        print("\n")
        print("Happy Betting!")
        print("\n")