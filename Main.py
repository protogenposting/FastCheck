import requests

import datetime

# INSTALL BEAUTIFUL SOUP https://beautiful-soup-4.readthedocs.io/en/latest/

def daily3():
    print("Daily 3 selected")

    yesterday = datetime.now() - timedelta(1)

    print(datetime.strftime(yesterday, '%Y-%m-%d'))

    url = "https://www.michiganlottery.com/games/daily-3?drawDate"

    req = requests.get("https://www.michiganlottery.com/games/daily-3?drawDate=2025-06-17")

print("Welcome to FastCheck! The slightly easier way to verify numbers on the MSL website")

print("1 - Daily 3")

input = int(input("What do you want to check? "))

if(input == 1):
    daily3()
else:
    print("no valid selections, DO BETTER")