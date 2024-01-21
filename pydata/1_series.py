#A pandas series is like column in a table with its serial number(indexing)

import pandas as pd
col = [1,7,2] 
colnew = pd.Series(col)
print(colnew)

#labeling(indexing) - label can be use to access a specified value.
print(colnew[0],'\n')

#you can create own name labels
colnew_1 = pd.Series(col,index=["x","y","z"])
print(colnew_1)
print(colnew_1["x"],'\n')


#can use a key or value object like dictonary
calories = {"day1":420,"day2":380,"day3":360}
colnew_2 = pd.Series(calories)
print(colnew_2)

#create series using only data from day1 and day2
calories = {"day1":420,"day2":380,"day3":360}
colnew_2 = pd.Series(calories,index=["day1","day2"])
print(colnew_2)


#dataframe:data sets in pandas are usually multidimentional tables & they are called data frames
#series are like column and dataframe is the whole table

#create a dataframe from 2 series.
col = {"calories":[420,340,680],"duration":[50,40,45]}
colnew = pd.DataFrame(col)
print(colnew)