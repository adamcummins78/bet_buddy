import requests
import time
import re
from bs4 import BeautifulSoup

#Stats Website

def get_defensive_stat(url):
    #Link URL and search through HTML
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # Get defensive total yards allowed
    stat = soup.find('td', {'data-stat':"opp_tot_yds"}).getText()
    
    return float(stat)

def get_offensive_stat(url):
    #Link URL and search through HTML
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # Get defensive total yards allowed
    stat = soup.find('td', {'data-stat':"tot_yds"}).getText()
    
    return float(stat)

ga_def = get_defensive_stat("https://www.sports-reference.com/cfb/schools/georgia/2020.html")
ga_off = get_offensive_stat("https://www.sports-reference.com/cfb/schools/georgia/2020.html")

ky_def = get_defensive_stat("https://www.sports-reference.com/cfb/schools/kentucky/2020.html")
ky_off = get_offensive_stat("https://www.sports-reference.com/cfb/schools/kentucky/2020.html")

al_def = get_defensive_stat("https://www.sports-reference.com/cfb/schools/alabama/2020.html")
al_off = get_offensive_stat("https://www.sports-reference.com/cfb/schools/alabama/2020.html")

ten_def = get_defensive_stat("https://www.sports-reference.com/cfb/schools/tennessee/2020.html")
ten_off = get_offensive_stat("https://www.sports-reference.com/cfb/schools/tennessee/2020.html")


print(ky_def)
print(ten_def, ten_off)

print(al_off)