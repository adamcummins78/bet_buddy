import datetime
from datetime import date

def cfbCountDown():
    today = date.today()
    start_date = date(2021, 8, 28)
    delta = start_date - today
    if (today < start_date):
        print(f"There are {delta.days} more days until the start of College Football!")
    elif (today >= start_date ) and (today <= date(2021, 9, 1)):
        print("It is Week 1 of College Football")
    elif (today >= date(2021, 9, 2)) and (today <= date(2021, 9, 8)):
        print("It is Week 2 of College Football")
    else:
        print("College Football is over...")

cfbCountDown()