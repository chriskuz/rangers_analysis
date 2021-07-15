from bs4 import BeautifulSoup #how we clean 
import requests as req #how we access the web page
import pandas as pd
import os


all_game_level_data_120320 = req.get('http://moneypuck.com/moneypuck/playerData/careers/gameByGame/all_teams.csv')

print(all_game_level_data_120320.status_code)

soup = BeautifulSoup(all_game_level_data_120320.content, 'html.parser')