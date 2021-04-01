# Bet Buddy
## Overview
I wanted to create a console application that would help me when making sports picks. I bit off a little more than I could currently handle when I first started, and ended up creating this application to compare teams offensive and defensive averages. This program uses Beautiful Soup to scrape different webpages associated with https://www.sports-reference.com/cfb/. The website houses an abundance of stats for every team that are simply and efficiently formatted making it perfect for scraping. <br/> <br/>The program displays a countdown to college football and then when the College Football season starts, displays the current week of the season. The program then asks the user to select two teams (currently can pick from 4) and returns the team's avg offensive yards and average yards allowed by their defense for the 2020 year.

## PIP Requirements
* beautifulsoup4  4.9.3
* certifi         2020.12.5
* chardet         4.0.0
* idna            2.10
* numpy           1.20.1
* pandas          1.2.3
* pip             20.2.3
* python-dateutil 2.8.1
* pytz            2021.1
* requests        2.25.1
* selenium        3.141.0
* setuptools      49.2.1
* six             1.15.0
* soupsieve       2.2
* urllib3         1.26.3

## Steps to run
To run the program, the user only needs to run main.py. 

## Features
1. Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program **(Located in menu.py)** <br/> <br/>
2. Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. **(Two fucntions are located in scraper.py, one is located in countdown.py, and then there is one to build the menu in main.py)** <br/> <br/>
3. Calculate and display data based on an external factor (ex: get the current date, and display how many days remaining until some event) **(Located in countdown.py)** <br/> <br/>
4. Implement a “scraper” that can be fed a type of file or URL and pull information off of it. For example, a web scraper that lets you provide any website URL and it will find certain keywords on the page **(Located in scraper.py)**
