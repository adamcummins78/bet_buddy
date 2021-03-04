import datetime

user = input("Please enter your name:  ")
print("\n")
print("======================================================")
print("===================== BET BUDDY ======================")
print("======================================================")
print(f"Welcome to Bet Buddy, {user}! (College Football Edition)")
print()
print("It is WEEK ONE of the college football season.") #I want this section to print out what week of the college football season it is based of datetime entry
print("======================================================")
print("======================================================")
print("======================================================")
print("\n")
team = input("Please enter the first team you would like to compare, or q to quit:  ")
while(team == "q"):
    exit()
team_two = input("Please enter the second team you would like to compare:  ")
print("\n")


while(team != "q" or team_two != "q"):
    print("Happy betting! Are there more teams you want to compare?""\n")
    team = input("Please enter the first team you would like to compare:  ")
    team_two = input("Please enter the second team you would like to compare, or q to quit:  ")
    print("\n")
        # if(team == "UK"):
    
    
    

