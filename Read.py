"""
Created on Sun Mar  1 15:51:09 2020
@author: Abhinav
"""

#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('G:\skilledge/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('G:\skilledge/IIT-B.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('G:\skilledge/User_Data.xlsx')

df1 = pandas.read_excel('User_Data.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('IIT-B.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)
