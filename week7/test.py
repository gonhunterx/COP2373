import numpy as np 

numbers = np.array([2, 3, 5, 7, 11])

# creating an array with even numbers 
even_array_one_through_20 = np.array([x for x in range(2, 21, 2)])
#print(even_array_one_through_20)

both = np.array([[x for x in range(2, 11, 2)], [x for x in range(1, 10, 2)]])
#print(both)
print(f"\n")
print("_" * 20)
integers = np.array([[1, 2, 3], [4, 5, 6]])
print("Integers")
print(integers)
print(integers.dtype)
# ndim returns just the number of dimensions 
print(integers.ndim)
# shape will returns a tuple specifying an array's dimensions
print(integers.shape)

# standard way to iterate 
for row in integers:
    for column in row:
        print(column, end=' ')
    print()
print(f"\n")
# turning a matrix into a one-dimensional array using .flat 
for i in integers.flat:
    print(i, end=' ')
    
print(f"\n")
print("_" * 20)

floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
print("Floats")
print(floats)
print(floats.dtype)
print(floats.ndim)
print(floats.shape)
# size returns the length of the array 
print(floats.size)
# itemsize returns the number of bytes required to store each element 
print(floats.itemsize)



print("-" * 30)
fulled_array = np.full((4, 5), 15)
print(fulled_array)