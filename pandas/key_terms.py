# Data frame: A two-dimensional data structure inside Pandas similar to a spreadsheet, with columns and rows.

# Series: A one-dimensional array with axis labels, usually created from a Pandas data frame column.

# Loading: The process of reading external data into a Pandas data frame.

# Exploratory analysis: Initial investigation of data to understand its characteristics before further analysis.

# Exporting: Saving data from a Pandas data frame out to another format like CSV or Excel.

import pandas as pd

# Create data frame 
data = [[1, 2], [3, 4]] 
df = pd.DataFrame(data, columns=['Num1', 'Num2'], index=['R1', 'R2'])
print(df)

# Create series
s = df['Num1']
print(s)


# Load CSV file into data frame
df = pd.read_csv('data.csv') 

# Exploratory analysis
print(df.describe())

# Export data frame to CSV
df.to_csv('export.csv')
