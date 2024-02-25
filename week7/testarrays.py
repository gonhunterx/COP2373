import numpy as np 

tst_arr = [8, 4, 2, 4, 1, 2]

converted_array = np.array(tst_arr)

print(converted_array)

print(converted_array.dtype)

# 
print(converted_array.itemsize)


arr1 = np.array([x for x in range(2, 21, 2)])
arr2 = np.array([x for x in range(1, 20, 2)])

combo_arr = zip(arr1, arr2)



print([y for y in (combo_arr)])

lambda_var = lambda x: x + 2

print(lambda_var)




print(f"Odds: \n{arr1}\nEvens:\n{arr2}")
