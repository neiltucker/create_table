import pandas as pd
employees = pd.read_csv('allemployees.csv')
employees.to_json('allemployees.json')
