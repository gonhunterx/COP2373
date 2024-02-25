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

print("Arranging and reshaping")
arr1 = np.arange(1, 21).reshape(4, 5)
print(arr1)

print('\n Exercise 7.2 \n')
numbers = np.arange(0, 4).reshape(2, 2)
print("numbers array")
print(numbers)
# Answer
#array([[0, 1],
#       [2, 3]])

numbersCubed = [x**3 for x in numbers]
print("numbers array cubed")
print(numbersCubed)

numbersPlus7 = [x + 7 for x in numbers]
print("numbers array plus 7")
print(numbersPlus7)

numbers1 = np.arange(2, 19, 2).reshape(3, 3)
print(f'numbers1\n {numbers1}')

numbers2 = np.arange(1, 10).reshape(3, 3)
numbers2 = numbers2[::-1, ::-1]
print(f'numbers2\n {numbers2}')

product = numbers1 * numbers2
print(f'The product is\n {product}')


# test example from book 
# for reshape it is (rows, columns)
grades = np.random.randint(60, 101, 12).reshape(3, 4)
cntr = 1

print("=" * 30)
print("Calculation Methods")
print("Used matrix: ")
print(grades)

print(f"(grades.mean()) Mean: {grades.mean()}")
print(f"(grades.mean(axis=0) Mean axis=0: {grades.mean(axis=0)}")
print(f"(grades.mean(axis=1) Mean axis=1: {grades.mean(axis=1)}")

print("Looped mean values for each row ")
for i in grades.mean(axis=0):
    print(f"Row {cntr}: {i}")
    cntr += 1

cntr1 = 1
print("Looped mean values with columns")
for i in grades.mean(axis=1):
    print(f"Column {cntr1}: {i}")    
    cntr1 += 1
print(f"Minimum = {grades.min()}")
print(f"Maximum = {grades.max()}")
print(f"standard deviation = {grades.std()}")
print(f"Variance = {grades.var()}")



new_arr = np.array([x for x in range(1, 16)]).reshape(3, 5)
print(new_arr)
print(f"Second row of new arr = \n{new_arr[:, [1]]}")
print(f"First and third row = \n{new_arr[:, [0, 2]]}")
print(f"Middle 3 columns = \n{new_arr[:, 1:4]}")


numbers = np.array([2, 3, 5, 7, 11])
print(type(numbers))

print(f'\n Exercise 7.5')
                                                        
powers = np.array([2 ** i for i in range(1, 33)]).reshape(2, 3)
print(f'{powers}')
# Answer
#array([[ 1,  2,  4],
#       [ 8, 16, 32]])

# fpowers = powers***
# print(f'{fpowers}')
# # Answer
# #array([ 1,  2,  4,  8, 16, 32])

# rpowers = powers***
# print(f'{rpowers}')
# Answer
#array([ 1,  2,  4,  8, 16, 32])