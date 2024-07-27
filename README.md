# Potential Names of Project
- Crosscheck Hockey API
- Blue Line Hockey API
- Puckdump Hockey API
- Dump n Chase Hockey API

# UPDATE 2021: 
This project will be renamed and will have a focus on producing bulk visualizations only. It will not at all serve as a place to write actual statistics. Revamping of the project will focus heavity on making a working and easy-to-use day-of-game API. Ideally a dashboard where input credentials are entered and output files are made. There will also need to be a form of plot structure used to generate different plots. This project is now officially under complete renovation of structure. 

Test team will be the New York Rangers as I am a huge fan =)

## The General Mission
This project is meant as a hobby project to create tools that analyze Rangers statistics quickly. The goal of this project is to output analytics reports programmatically and to give enough context on the team's performance to develop articles. 

## Type of Statistical Analysis
- Team History Comparisons to Other Teams 
- Team History Comparison Against Self
- Career Performance of Players
- Player Comparison Across the League (inclusive of KPI stat averages and medians for references)
- Pre-Match Analytics for Advantages and Disadvantages
- Heat Maps of Shots on Ice
- Heat Maps of Successful Goals and Blocks on Goalies
- Miscellaneous Analysis
- KPI creations
    - dollar per point (a KPI rate to determine a skater's )

## Data Source Credits
www.moneypuck.com -- Special thanks to the creators and those who maintain the moneypuck website. Their website allows hobbyists utilize open-source data to a tremendous extent. 

## Restructure Considerations and Project Flow
- create a folder/file that pulls and stores csv table data.
    - i want a function that can pull in the latest table or specific kind of table
    - the function should store the file into a temporary folder that can be cleaned out everytime the user chooses to pull in an updated version of it (`update_xxx_table`)
    - the user should see all the possible tables they can pull
    - the user should have the ability to clean house
    - the user should have an easy affiliated call to pull in a table dictionary