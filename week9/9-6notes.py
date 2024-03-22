import pandas as pd 
import json 

accounts_dict = {'accounts': [
    {'account': 100, 'name': 'Jones', 'balance': 24.98},
    {'account': 200, 'name': 'Doe', 'balance': 343.98}    
]}

with open('accounts.json', 'w') as accounts: 
    json.dump(accounts_dict, accounts)
    
    
grades_data = {'students': [
    {'first_name': 'jadon', 'last_name': 'lama', 'exam1':98, 'exam2':99, 'exam3':100},
    {'first_name': 'ron', 'last_name': 'kobert', 'exam1':78, 'exam2':29, 'exam3':50}    
]}

grades_data['students']['']

with open('grades.json', 'w') as file:
    json.dump(grades_data, file)