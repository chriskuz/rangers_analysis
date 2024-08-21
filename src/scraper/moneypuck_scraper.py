#Imports
import requests as req #how we access the web page
import pandas as pd
import json
import os

#File and data calls
url_file = open("../dictionaries/url_dict.json")
url_dict = json.load(url_file)
url_list = list(url_dict.keys())


#User Input for data call
print('Choose and enter MoneyPuck data):')
user_input = input(f"Example entries to choose {url_list}: ")


#Checks if user input is valid
if user_input not in url_list:
    raise Exception(f"That is not a valid entry. Double check your entry. Last entry was {user_input}")


print(f"User has chosen valid entry: {user_input}")
print(f"Getting {user_input}...")


#Checks capability to call data 
response = req.get(url_dict[user_input])

assert response.status_code == 200, f"ABNORMAL URL RESPONSE CODE: {response}. Response should be 200."


#Store Table


## Store the information. Give the user the filepath information. State it is ready for intake into another notebook. 