# This script will read an excel or csv table into a python dataframe
# The dataframe will then be sorted by first and lastname
# The salesmanagertable2 spreadsheet or CSV file must be in the current directory for this script to work
import pandas as pd
df = pd.read_csv('salesmanagertable2.csv')                        # Create a dataframe from a CSV file
df[['InvoiceID','Price','Quantity','Freight','Total']].head()

# Sort the data using different criteria and save the dataframes
labels = ['CustomerID','SupervisorID']
dfsort = pd.read_c8sv('salesmanagertable2.csv',index_col=labels)   # Create a dataframe from a CSV file and specify index column(s)
df.sort_index(inplace=True)
dfsort_sup = df.sort_values(['SupervisorID','CustomerID'])
dfsort_cus = df.sort_values(['CustomerID','SupervisorID'])

# Remove Duplicates
df.drop_duplicates(subset=None,keep='first',inplace=False)                   # Return only unique rows
df.drop_duplicates(subset=None,keep=False,inplace=False)                     # Return only rows that have no duplicates
df.ix[df.duplicated(subset=None,keep='first'),:]                             # Return the first copy of each duplicated row
df_duplicates = df.ix[df.duplicated(subset=None,keep=False),:]               # Return only rows that are not unique
df_all = df.drop_duplicates(subset=None,keep='first',inplace=False)          # Remove the duplicate rows
df_unique = df.drop_duplicates(subset=None,keep=False,inplace=False)         # Remove the duplicate rows and their originals



