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