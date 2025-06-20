#import requests

# INSTALL BEAUTIFUL SOUP https://beautiful-soup-4.readthedocs.io/en/latest/

# INSTALL PDF PARSER FOR PDF PARSING https://www.freecodecamp.org/news/extract-data-from-pdf-files-with-python/

def daily3():
    print("Daily 3 selected")

    url = "https://www.michiganlottery.com/games/daily-3"



    #req = requests.get(url)

    #print(req)

print("Welcome to FastCheck! The slightly easier way to verify numbers on the MSL website")

print("1 - Daily 3")

input = int(input("What do you want to check? "))

if(input == 1):
    daily3()
else:
    print("no valid selections")