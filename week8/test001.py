import numpy as np 
import pandas as pd 

print(f'{18.9824:.2f}')


val = 10 

print(f'{val:d}')

# characters numeric representation with :c
print(f'{65:c}, {97:c}')

# :s is default and it represents a string 
print(f'{"hello":s} {7}')

# scientific notation 
from decimal import Decimal 
original_val = Decimal(10000000000000000000000000.0)
print(f'{original_val:.3f}')

print(f'{original_val:.3e}')


import re 
# replacement text in a formatted string 
# A regular expression string describes a SEARCH PATTERN for MATCHING characters in other strings 
print(re.sub(r'\t',', ', '1\t2\t3\t4'))

text = 'Jadon Lama, e-mail: jadon@gmail.com'
# \w = Any word character (alphanumeric character)
# \W = Any character that is NOT a word character 
pattern = r'([A-Z][a-z]+ [A-Z][a-z]+), e-mail: (\w+@\w+\.\w{3})'
 
result = re.search(pattern, text)
print(result)
print(len(text))
print(result.groups())

prob = '10 + 5'
# \d = any digit (0-9)
result1 = re.search(r'(\d+) ([-+*/]) (\d+)', prob)
print(result1.groups())

MONTHS = ("January","February","March","April","May","June","July","August",
          "September","October","November","December")

print(type(MONTHS))