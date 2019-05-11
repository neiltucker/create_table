# This script will read an excel or csv table into a python dataframe
# The dataframe will then be sorted by first and lastname
# The salesmanagertable2 spreadsheet or CSV file must be in the current directory for this script to work
import pandas as pd
df = pd.read_csv('salesmanagertable2.csv')                        # Create a dataframe from a CSV file

# In the df dataframe, create a column that stores the total for each row (Price * Quantity + Freight)                     
rows = len(df)
total_array = [None] * rows
for row in range(rows):
  total_sale = df['Price'][row] * df['Quantity'][row] + df['Freight'][row]     # Find the total for a particular row in the dataframe
  total_array[row] = round(total_sale,2)                          # Round the value to two decimal places

df['Total'] = total_array
df[['Price','Quantity','Freight','Total']].head()

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


# Create a new dataframe with no predefined index
df2 = pd.read_csv('salesmanagertable.csv')   

# Search for duplicate data on a row and column level.  A result of "True" indicates a row has duplicates
df2.duplicated(subset=None)                     # Row level duplicates
df2.duplicated(subset='SupervisorID')           # Column level duplicates

# Drop duplicate data on a row or column level.  Results will be written to a new variable without changing the original dataframe
df2_unique_rows = df2.drop_duplicates(subset=None,keep='first',inplace=False)
df2_unique_columns = df2.drop_duplicates(subset='SupervisorID',keep='first',inplace=False)

# Create an array that stores the "total" for each row (Price * Quantity + Freight)                     
rows = len(df2)
total_array = [None] * rows
for row in range(rows):
  total_sale = df2['Price'][row] * df2['Quantity'][row] + df2['Freight'][row]     # Find the total for a particular row in the dataframe
  total_array[row] = round(total_sale,2)                                          # Round the value to two decimal places

# Create a new column in the dataframe using the "total" array
df2['Total'] = total_array

# Get the total sales for each customer / supervisor  
df2.groupby('CustomerID')['Total'].sum()                                   
df2.groupby('SupervisorID')['Total'].sum()

# Export a dataframe to a CSV file
# df2.to_csv('dataframe_export.csv')


