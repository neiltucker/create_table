# This script will read an excel or csv table into a python dataframe
# The dataframe will then be sorted by first and lastname
# The employeestable spreadsheet or CSV file must be in the current directory for this script to work
import pandas as pd
labels = ['CustomerID','SupervisorID']
df = pd.read_csv('salesmanagertable.csv',index_col=labels)       # Create a dataframe from a CSV file and specify index column(s)
df.sort_index(inplace=True)
df.head(10)
df.sort_values(['SupervisorID'],inplace=True)
df.head(10)
df.sort_values(['InvoiceID'],inplace=True)
df.head(10)

# Specify the order of the columns
df[['Price','Quantity','Freight','OrderDate','InvoiceID','CreditCard']].head(10)

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


