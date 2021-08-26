import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MakePlot:
    def __init__(self, serialnumber, credentialvalue):
        self.serialnumber = serialnumber
        self.credentialvalue = credentialvalue
    
    pass



# this is parent class
class TaskAnalysis:

    whatdonumber = 0 # class attribute for initial task number chosen
    
    taskvalue = 0 # meant for child class' task selection 
    credentialvalue = [] # meant for the credential input storage based on the child class' task selection
    
    serialnumber = [] # number used for the MakePlot command

    
    # TODO: children classes will accept an instance variable for the category name
    def __init__(self, categoryname):
        self.categoryname = categoryname


    def execute(self):
        serialnumber = taskvalue + credentialvalue #serial number is going to specify the plotting process

    




# This will be a child class from a parent that stores objects such as taskvalue and credentialvalue. taskvalue and credentialvalue will be used in conjunction to create a serial number for the MakePlot funciton to run a plot. There may also be a playername/teamname string used for recognition and labeling. 
class AnalyzePlayer(TaskAnalysis):

    
    # TODO: child class should accept an instance variable to operate of which player the person has chosen
    def __init__(self, categoryname):
        self.categoryname = categoryname

        print("Select a Task by inputting corresponding list integer: ")
        print("-----------------------")
        print("1) Analyze Game-by-game Weighted Average Percentages Against Opposing Teams")
        print("2) Analyze Game-by-game Percentages Over Time")
        
        
        print("Analyze Statistics Across Opponents")
        print("Analyze Statistics Over Time")

    # TODO: offer player comparison analysis (consider funcitonality to scrape trusted sources for potential trade rumors to be more intuitive on comparison presentations)  

    # TODO: offer statistics over time

        # TODO: percentages over time, tangible impacts over time, shifts over time, different team categorical representations over time, 
        
        # TODO: provide overlay options

    # TODO: offer statistics across opponents

        #TODO: offer against league, against individual teams (specified), against most recent opponent, against upcoming opponent (next game, next week, next month), against divisions

class AnalyzeTeam(TaskAnalysis):

    
    # TODO: child class will have an input of category name upon instance creation
    def __init__(self, categoryname):
        self.categoryname = categoryname

        print("Select a task by inputting corresponding list integer: ")
        print("-----------------------")

        print("Analyze Statistics Over Time")
        print("Analyze Statistics Across Opponenets")


        print("1) Analyze Seasonal Offensive Effect.")
        print("2) Analyze Seasonal Defensive Effect.")
        print("3) Analyze ")

    # TODO: 

class GeneralAnalysis(TaskAnalysis):

    def __init__(self):
        print("Display Current Seasonal Standings")
        print("Display Best Offensive Numbers")
        print("Display Best Defensive Numbers")
        print("Display Best Goalie Numbers")
        
        pass


    

def processtask(whatdonumber):
    if whatdonumber == 1:
        TaskAnalysis.categoryname = input("What player do you want to analyze?: ")
        return AnalyzePlayer(TaskAnalysis.categoryname)
    elif whatdonumber == 2:
        TaskAnalysis.categoryname = input("What team do you want to analyze?: ")
        return AnalyzeTeam(TaskAnalysis.categoryname)
    elif whatdonumber == 3:
        return GeneralAnalysis("General Analysis")
    elif whatdonumber == 4:
        pass
    elif whatdonumber == 5:
        pass



