
"""

Pandas is an python library providing high performance data manipulation & analysis tool using it's data structures like Series, DataFrame & Panel.

Pandas data structures are very fast because these data structures are built on top of Numpy array.

Pandas can clean messy data sets, and make them readable and relevant

Pandas allows us to analyze big data and make conclusions based on statistical theories

"""

import pandas as pd

dataframe1 = pd.DataFrame({'name':['Tanikonda','Purna','Chandra'],'age':[45,6,34]})
dataframe2 = pd.DataFrame({'name':['Ongole','Prakasam','Andhra Pradesh'],'age':[5,55,55]})

combined_dataframes = pd.concat([dataframe1,dataframe2])
print(combined_dataframes)
print("\n\n")

# Joining using common unique id

# Joining is similar to what we do with tables in an SQL database

dataframe3 = pd.DataFrame({'city':['Ongole','Prakasam','Andhra Pradesh'],'company':['Shorewise','Jamawealth','Capgemini']})

joined_dataframes = pd.concat([dataframe1, dataframe3], axis=1, join='inner')
print(joined_dataframes)
