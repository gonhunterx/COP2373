numbers = [2, 3, 5, 7, 11, 13, 17, 19]
numbers2 = numbers[2:6]

print(numbers2)

numbers3 = numbers[::-1]
print(numbers3)

# looks for 7 in the range of elements with indices 0 through 3 
print(numbers.index(7, 0, 4)) # returns 3 (location of 7 and within the range set)