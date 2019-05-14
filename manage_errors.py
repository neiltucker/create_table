# This script will read an excel or csv table into a python dataframe
# The dataframe will then be sorted by first and lastname
# The salesmanagertable2 spreadsheet or CSV file must be in the current directory for this script to work
import pandas as pd
df = pd.read_csv('salesmanagertable2.csv')                                   # Create a dataframe from a CSV file
df[['InvoiceID','Price','Quantity','Freight','Total']].head(20)              # Select the columns to read from the first 20 rows

# Sort the data using different criteria and save the dataframes
labels = ['CustomerID','SupervisorID']
dfsort = pd.read_c8sv('salesmanagertable2.csv',index_col=labels)             # Create a dataframe from a CSV file and specify index column(s)
df.sort_index(inplace=True)
dfsort_sup = df.sort_values(['SupervisorID','CustomerID'])
dfsort_cus = df.sort_values(['CustomerID','SupervisorID'])
dfsort_sup.to_csv('sortbysupervisorid.csv')                                  # Save SupervisorID sorted dataframe to CSV file
dfsort_cus.to_csv('sortbycustomerid.csv')                                    # Save CustomerID sorted dataframe to CSV file

# Remove Duplicates
df.drop_duplicates(subset=None,keep='first',inplace=False)                   # Return only rows that are unique
df.drop_duplicates(subset='InvoiceID',keep='first',inplace=False)            # Return only rows with unique InvoiceIDs
df.drop_duplicates(subset='CustomerID',keep='first',inplace=False)           # Return only rows with unique CustomerIDs
df.drop_duplicates(subset=None,keep=False,inplace=False)                     # Return only rows that have no duplicates
df.loc[df.duplicated(subset=None,keep='first')]                              # Return the first copy of each duplicated row
df_duplicates = df.loc[df.duplicated(subset=None,keep=False)]                # Return only rows that are not unique
df_all = df.drop_duplicates(subset=None,keep='first',inplace=False)          # List the duplicate rows
df_unique = df.drop_duplicates(subset=None,keep=False,inplace=False)         # List the duplicate rows and their originals
df.drop_duplicates(subset=None,keep='first',inplace=True)                    # Remove the duplicate rows and keep the originals in the dataframe

# Manage Missing Data
df['Quantity'].ge(0)                                                         # Identify records that do or do not have a valid number in the Quantity field (True or False value for each row)
df.query('Quantity >= 0')                                                    # Identify records that do have a valid number in the Quantity field 
df_valid = df.where(df['Quantity'] >= 0).dropna()                            # Create a dataframe containing only records that have a valid number in the Quantity field
df_concat = pd.concat([df,df_valid])                                         # Concatenate the original dataframe with the one that only contains valid numbers
df_invalid = df_concat.drop_duplicates(subset=None,keep=False)               # Isolate rows that do not have a valid number in the Quantity field

# Format Errors
df_customer_valid = df.query('CustomerID.str.len() == 4')                    # Identify records that have a CustomerID with 4 digits (Valid)
df_customer_invalid = df.query('CustomerID.str.len() != 4')                  # Identify records that do not have a CustomerID with 4 digits (Invalid)
df_customer_invalid.to_csv('invalidcustomerid.csv')                          # Save records with invalid CustomerIDs to CSV file




