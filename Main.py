# import requests #ADD THIS BACK

# INSTALL BEAUTIFUL SOUP FOR HTML PARSING https://beautiful-soup-4.readthedocs.io/en/latest/

# INSTALL PDF PARSER FOR PDF PARSING https://www.freecodecamp.org/news/extract-data-from-pdf-files-with-python/

# check daily 3 midday and evenings
def daily3():
    print("Daily 3 check started");

    url = "https://www.michiganlottery.com/games/daily-3";

    # Stuff is commented out due to not having the module installed yet

    # req = requests.get(url);

    #print(req);

# Start of program
print("Welcome to FastCheck! The program that saves you exactly 3 minutes of checking numbers");

print("1 - Daily 3");

# Get the input for which one to check, make it just simply check it in order later
input = int(input("What do you want to check? "));

# Keep this tree for now, check automatically in order later.
if(input == 1):
    daily3();
else:
    print("no valid selections");