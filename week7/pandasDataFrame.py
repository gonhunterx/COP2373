import pandas as pd 

recorded_temps = {'Maxine': [87, 80, 95], 'James': [67, 55, 81], 'Amanda': [87, 60, 50]}

# Section A 
print("=" * 30)
print("Section A DataFrame: ")
# creating the inital temperatures dataframe with just the recorded temps dictionary 
temperatures = pd.DataFrame(recorded_temps)
print(temperatures)


# Section B 
print("=" * 30)
print("Section B DataFrame: ")
# list consisting of times of day to use for dataframe arguments 
time_of_day_list = ['Morning', 'Afternoon', 'Evening']
# initlizing the temperatures DataFrame 
temperatures = pd.DataFrame(recorded_temps, index=time_of_day_list)
print(temperatures)


# Section C
print("=" * 30)
print("Section C DataFrame: ")
print("Maxine's Data")
print("-------------")
# getting the values from 'Maxine' 
print(temperatures.Maxine)


# Section D
print("=" * 30)
print("Section D DataFrame: ")
print("All 'Morning' recordings")
print("----------------------")
# only have to use .loc if only need to access one rows values 
print(temperatures.loc['Morning'])

# Section E
print("=" * 30)
print("Section E DataFrame: ")
print("All 'Morning' and 'Evening' recordings")
print("--------------------------------------")
print(temperatures.iloc[[0, 2], 0:3])


# Section F
print("=" * 30)
print("Section F DataFrame: ")
print("Temperature readings for 'Amanda' and 'Maxine'")
print("---------------------------------------")
# using .ColumnName for accessing all values from a column
print(f"{temperatures.Amanda}\n------\n{temperatures.Maxine}")


# Section G
print("=" * 30)
print("Section G DataFrame: ")
print("'Amanda' and 'Maxine' values for 'Morning' and 'Afternoon'")
print("---------------------------------------")
# using iloc for multiple values 
print(f"{temperatures.iloc[[0, 1], 2]}")
print("------")
print(f"{temperatures.iloc[[0, 1], 0]}")


# Section H
print("=" * 30)
print("Section H DataFrame: ")
print("Temperatures DataFrame descriptive information")
print("------")
# using the .describe to display descriptive information 
print(temperatures.describe())

# Section I 
print("=" * 30)
print("Section I DataFrame: ")
print("Transposed DataFrame")
print("------")
# using .T to get the transposed object and printing it 
print(temperatures.T)

# Section J
print("=" * 30)
print("Section J DataFrame: ")
print("Temperatures DataFrame sorted in alphabetical order by index name")
print("------")
# sorting the temperatures DataFrame by setting the sort_index functions argument to axis = 1
print(temperatures.sort_index(axis=1))