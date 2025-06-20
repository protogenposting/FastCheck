# import requests

import datetime

# INSTALL BEAUTIFUL SOUP https://beautiful-soup-4.readthedocs.io/en/latest/

def daily3():
    print("Daily 3 selected")

    yesterday = datetime.now() - timedelta(1)

    time = datetime.strftime(yesterday, '%Y-%m-%d')

    print(time)

    url = "https://www.michiganlottery.com/games/daily-3?drawDate="+time

    req = requests.get(url)

    print(req)

print("Welcome to FastCheck! The slightly easier way to verify numbers on the MSL website")

print("1 - Daily 3")

input = int(input("What do you want to check? "))

if(input == 1):
    daily3()
else:
    print("no valid selections")