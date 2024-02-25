# Exercise 7.1

import numpy as np

print('\n Exercise 7.1 \n')
ones = np.ones((2, 3))
print("Array of ones")
print(ones)
# Answer
#array([[1., 1., 1.],
#       [1., 1., 1.]])

zeros = np.zeros((3, 3))
print("Array of zeros")
print(zeros)
#Answer
#array([[0., 0., 0.],
#      [0., 0., 0.],
#      [0., 0., 0.]])

full = np.full((2, 5), 7)
print("Array of sevens")
print(full)
# Answer
#array([[7, 7, 7, 7, 7],
#       [7, 7, 7, 7, 7]])

# Exercise 7.2

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
# Answer
#array([[ 0,  1],
#       [ 8, 27]])

numbersPlus7 = [x + 7 for x in numbers]
print("numbers array plus 7")
print(numbersPlus7)
# Answer
#array([[ 7,  8],
#       [ 9, 10]])

numbersTimesTwo = [x * 2 for x in numbers]
print("numbers array times 2")
print(numbersTimesTwo)
#Answer
#array([[0, 2],
#       [4, 6]])

# Exercise 7.3

print(f'\n Exercise 7.3')

numbers1 = np.arange(2, 19, 2).reshape(3, 3)
print(f'numbers1\n {numbers1}')
# Answer
#array([[ 2,  4,  6],
#       [ 8, 10, 12],
#       [14, 16, 18]])

numbers2 = np.arange(1, 10).reshape(3, 3)
numbers2 = numbers2[::-1, ::-1]
print(f'numbers2\n {numbers2}')
# Answer
#array([[9, 8, 7],
#       [6, 5, 4],
#       [3, 2, 1]])

# fill in product of numbers 1 and numbers 1
product = numbers1 * numbers2
print(f'The product is\n {product}')
# Answer
#array([[18, 32, 42],
#       [48, 50, 48],
#       [42, 32, 18]])

# Exercise 7.4

print(f'\n Exercise 7.4')

new_array = np.array([[2, 3, 5, 7, 11],[13, 17, 19, 23, 29]])

print(f'New Array is \n {new_array}')
# Answer
#array([[ 2,  3,  5,  7, 11],
#       [13, 17, 19, 23, 29]])

# Exercise 7.5

print(f'\n Exercise 7.5')

# by not adding in a start and stop to range I just have the list comprehension run 6 times then reshape the 
# array into a 2d array
powers = np.array([2 ** i for i in range(6)]).reshape(2, 3)
print(f'Array of powers:\n{powers}')
# Answer
#array([[ 1,  2,  4],
#       [ 8, 16, 32]])

fpowers = powers.flatten()
# flatten creates a deepcopy of the array 
print(f'Flatten function result:\n{fpowers}')
# Answer
#array([ 1,  2,  4,  8, 16, 32])

rpowers = powers.ravel()
# ravel produces a view which is changed if the original array is changed 
print(f'Ravel function result:\n{rpowers}')
# Answer
#array([ 1,  2,  4,  8, 16, 32])

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
