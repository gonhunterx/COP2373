# creating a pd series with custom indices 
import pandas as pd 
import numpy as np 

grades = pd.Series([87, 100, 94], index=['Randy', 'Jadon', 'Bob'])
print(grades)
# or like this 
print("=" * 30)
grades2 = pd.Series({'Randy': 87, 'Jadon': 100, 'Bob': 94})
print(grades2)
# you can use the keys like a method 
print(grades.Jadon)

# each column in a DataFrame is a Series 