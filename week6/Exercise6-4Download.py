# since result is actually a set and not a dict we can use comparison 
# operators and all the values are unique to the set 

# inital list 
result = {}
# getting the difference between all items in the two sets 
result = {1, 2, 4, 8, 16} - {1, 4, 16, 64, 256} # {2,8}
print(f"1 Difference method: {result}")

# Checking the intersection of the two sets (aka which items both have)
result = {1, 2, 4, 8, 16} & {1, 4, 16, 64, 256} # {1,4,16}
print(f"2 Intersection method: {result}")

# Union will combine the sets and maintain its 'set' status with unique values 
result = {1, 2, 4, 8, 16} | {1, 4, 16, 64, 256} # {1,2,4,8,16,64,256}
print(f"3 Union method: {result}")

# The symmetric difference method will result in a set that contains 
# items from both sets, but only items which are not in the tested subset or list 
result = {1, 2, 4, 8, 16} ^ {1, 4, 16, 64, 256} # {2,8,64,256}
print(f"4 Symmetric Difference method {result}")

# Order does not matter for set comparisons, but the items must all be the same for the operation to return True 
result = {1, 2, 4, 8, 16} >= {1, 4, 16, 64, 256} # False
print(f"5 Improper superset operator: {result}")

