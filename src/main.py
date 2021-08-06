from plotting import playerplotting

class main:
    print("\n")
    print("Welcome to the API" + "\n")
    print("---------------------------" + "\n")
    print("What do you want to do?" + "\n")
    print("Please enter the listed task number corresponding to the following options:" + "\n")
    print("1) Analyze Player" + "\n")
    print("2) Analyze Team" + "\n")
    print("3) General Season Analysis" + "\n")
    print("4) Random" + "\n")

    playerplotting.TaskAnalysis.whatdonumber = input("Task Number Input: ") 
    playerplotting.processtask(playerplotting.TaskAnalysis.whatdonumber)

    #to hide some of this code, we may create a "process task" method/class to store the if statement code to select where the task analysis method will continue

    #the reason why this code may not be running the plotting script is because nothing here really says to run playerplotting.py. This might be where I would need a Make file for everything to communicate or unfortunately.....make this file really big and ugly. 

    def __init__(self):
        pass
    
    # Initializing functions:
    # Clear cache on initialization??

    # Prep function Listing what the user wants to do
        # Inputs will then be used within main to activate other functions 
        # Once user select option, require step process for the option for input credentials
        # Run function  

    # https://realpython.com/python3-object-oriented-programming/
    # https://docs.python-guide.org/writing/structure/
    # https://pypi.org/project/selenium/
    # https://automatetheboringstuff.com/chapter11/
    # https://www.edureka.co/blog/web-scraping-with-python/