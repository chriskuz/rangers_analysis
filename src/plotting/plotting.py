def opposing_team_two_average_percentage_comparisons_barplot(data,year,situation,percentages,percentage_colors,graph_title,percentage_legend):
    #sets the year for the user
    if year:
        year_data = data[data['season'] == year]
    else:
        year_data = data

    
    #filters the situation
    if situation:
        situation_data = year_data[year_data['situation'] == situation]
    else:
        situation_data = year_data

    #instantiates subplotting capabilities
    plt.subplots(figsize = (25,15))
    width = 0 #set the iterable widths outside of loop to be grown upon as more percentages are added
    
    
    #for a percentage in percentages
    for i, percentage in enumerate(percentages):
        spread = 0.25 #set the spread of bar graphs from one another

        #for the team in teams
        for j, team in enumerate(sorted(situation_data['opposingTeam'].unique())):
            team_matchup = situation_data[situation_data['opposingTeam'] == team]
            #get weighted average of the percentage for the team
            weighted_avg_percentage = np.average(team_matchup[percentage], weights = np.full(team_matchup.shape[0], team_matchup.shape[0]), axis = 0)

            #we need a condition to locate when to set the legend for what percentage
            if j == (len(situation_data['opposingTeam'].unique()) - 1):
                #plot across the barplot with all that weighted percentage with an "j + width" where width = 0 for first pass through
                plt.bar(j + width, weighted_avg_percentage, spread, alpha = 0.5, color = percentage_colors[i], label = percentage_legend[i])
            else: 
                plt.bar(j + width, weighted_avg_percentage, spread, alpha = 0.5, color = percentage_colors[i])
        
        #add 0.25 to width before iterating percentage for the next group of bars
        width = width + 0.25
    
    #establish grid
    plt.grid(which = 'major', axis = 'both')
    #plot xticks
    plt.xticks(list(range(len(situation_data['opposingTeam'].unique()))), sorted(situation_data['opposingTeam'].unique()), rotation = 60, fontsize = 16)
    #plot yticks
    plt.yticks(fontsize = 16)
    #set xlabel
    plt.xlabel('Opposing Teams', fontsize = 18)
    #set ylabel
    plt.ylabel('Weighted Average Percentages', fontsize = 18)
    #set title
    plt.title(graph_title, fontsize = 20)
    #set legend
    plt.legend(framealpha = 1, frameon = True, fontsize = 18)
    #change plot color
    #plt.rcParams('figure.facecolor') = 'gray';