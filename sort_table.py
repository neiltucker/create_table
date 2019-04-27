# This script will read an excel or csv table into a python dataframe
# The dataframe will then be sorted by first and lastname
# The employeestable spreadsheet or CSV file must be in the current directory for this script to work
import pandas as pd
employees_df = pd.read_excel('employeestable.xls') 
# employees_df = pd.read_csv('employeestable.csv')   # Uncomment this line to use a csv instead of a spreadsheet
# employees_df.head()   # Uncomment this line to see the first five rows of the dataframe
namesort = employees_df.sort_values(['LastName','FirstName'],ascending=True)
hiredatesort = employees_df.sort_values(['HireDate'],ascending=True)
namesort
hiredatesort

