import pandas as pd 
import numpy as np 

# Series are one dimentional arrays and dataframes are two dimentional arrays 
print("=" * 30)
print("Part A Series:")
# creating the first series and initlizing it with an array of integers 
series1 = pd.Series([7, 11, 13, 17])
print("Index Value")
print(series1)

# Section B 
print("=" * 30)
print("Part B Series:")
# using the range function to create 5 instance of 100 within the series 
series2 = pd.Series((100), range(5))
print("Index Value")
print(series2)

# Section C
print("=" * 30)
print("Part C Series:")
print("Index Value")
# creating a var to represent 20 random numbers between 0 and 100 
rand_nums = np.random.randint(0, 101, 20)
# printing the series and using the rand nums var to populate the series 
series3 = pd.Series(rand_nums)
print(series3)
# using .describe() method on the series to get more information for the user 
print(series3.describe())

# Section D
temperatures = pd.Series({'Julie': 98.6, 'Charlie': 98.9, 'Sam': 100.2, 'Andera': 97.9})
print("=" * 30)
print("Part D Series: ")
print("Index      Value")
print(temperatures)

# Section E
# changing the temperatures pd series into a dictionary 
names_values_dict = dict(temperatures)
print("=" * 30)
print("Part E Series: ")
print("Index      Value")
# print(names_values_dict)
# using the dictionary to initlize a pandas series then printing it. 
new_temps_series = pd.Series(names_values_dict)
# same as section D, however it has been changed into a dict then used to initlize a pandas series 
print(new_temps_series)



