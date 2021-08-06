import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MakePlot:
    def __init__(self):
        pass
    
    pass



# this is parent class
class TaskAnalysis:

    whatdonumber = 0 # class attribute for initial task number chosen

    def __init__(self):
        self.taskvalue = 0 # child class' task selected
        self.credentialvalue = [] #needed credential inputs selected based on task selection
        self.categoryname = [] # player name or team name
        self.serialnumber = []
        # self.whatdonumber = whatdonumber # state of initial whatdo to then select the child classes


    def execute(self):
        serialnumber = taskvalue + credentialvalue #serial number is going to specify the plotting process

    


# This will be a child class from a parent that stores objects such as taskvalue and credentialvalue. taskvalue and credentialvalue will be used in conjunctio to create a serial number for the MakePlot funciton to run a plot. There may also be a playername/teamname string used for recognition and labeling. 
class AnalyzePlayer(TaskAnalysis):
    print("Select a Task by inputting corresponding list integer?")
    print("-----------------------")
    print("1) Analyze Game-by-game Weighted Average Percentages Against Opposing Teams")
    print("2) Analyze Game-by-game Percentages Over Time")

    def __init__(self, whatdonumber):
        TaskAnalysis.__init__(self, )
        # print("Select a Task by inputting corresponding list integer?")
        # print("-----------------------")
        # print("1) Analyze Game-by-game Weighted Average Percentages Against Opposing Teams")
        # print("2) Analyze Game-by-game Percentages Over Time")



    






# def opposing_team_two_average_percentage_comparisons_barplot(data,year,situation,percentages,percentage_colors,graph_title,percentage_legend):
#     #sets the year for the user
#     if year:
#         year_data = data[data['season'] == year]
#     else:
#         year_data = data

    
#     #filters the situation
#     if situation:
#         situation_data = year_data[year_data['situation'] == situation]
#     else:
#         situation_data = year_data

#     #instantiates subplotting capabilities
#     plt.subplots(figsize = (25,15))
#     width = 0 #set the iterable widths outside of loop to be grown upon as more percentages are added
    
    
#     #for a percentage in percentages
#     for i, percentage in enumerate(percentages):
#         spread = 0.25 #set the spread of bar graphs from one another

#         #for the team in teams
#         for j, team in enumerate(sorted(situation_data['opposingTeam'].unique())):
#             team_matchup = situation_data[situation_data['opposingTeam'] == team]
#             #get weighted average of the percentage for the team
#             weighted_avg_percentage = np.average(team_matchup[percentage], weights = np.full(team_matchup.shape[0], team_matchup.shape[0]), axis = 0)

#             #we need a condition to locate when to set the legend for what percentage
#             if j == (len(situation_data['opposingTeam'].unique()) - 1):
#                 #plot across the barplot with all that weighted percentage with an "j + width" where width = 0 for first pass through
#                 plt.bar(j + width, weighted_avg_percentage, spread, alpha = 0.5, color = percentage_colors[i], label = percentage_legend[i])
#             else: 
#                 plt.bar(j + width, weighted_avg_percentage, spread, alpha = 0.5, color = percentage_colors[i])
        
#         #add 0.25 to width before iterating percentage for the next group of bars
#         width = width + 0.25
    
#     #establish grid
#     plt.grid(which = 'major', axis = 'both')
#     #plot xticks
#     plt.xticks(list(range(len(situation_data['opposingTeam'].unique()))), sorted(situation_data['opposingTeam'].unique()), rotation = 60, fontsize = 16)
#     #plot yticks
#     plt.yticks(fontsize = 16)
#     #set xlabel
#     plt.xlabel('Opposing Teams', fontsize = 18)
#     #set ylabel
#     plt.ylabel('Weighted Average Percentages', fontsize = 18)
#     #set title
#     plt.title(graph_title, fontsize = 20)
#     #set legend
#     plt.legend(framealpha = 1, frameon = True, fontsize = 18)
#     #change plot color
#     #plt.rcParams('figure.facecolor') = 'gray';



def processtask(whatdonumber):
    
    if whatdonumber == 1:
        AnalyzePlayer
    elif whatdonumber == 2:
        pass
    elif whatdonumber == 3:
        pass
    elif whatdonumber == 4:
        pass