# creating a program that will sum the triples(n*3) of the even integers from 2 through 10 
# by utilizing the 

# function for mapping, filtering evens, and reducing to sum 
def sum_mfr(lst):
    # creating a result in memory to store our list 
    result = list(map(lambda x: x * 3, filter(lambda x: x % 2 == 0, lst)))
    # returning the sum
    return sum(result)    

# sum with list comprehension 
def sum_lc(lst):
    # returning the entire comprehension
    return [sum(item * 3 for item in lst if item % 2 == 0)]
    
# if name statement for calling 
if __name__ == "__main__":
    # global list containing 1 through 10 
    lst = list(range(1, 11))
    # creating variables that represent the returned values of the
    # functions for displaying the objects 
    sum_mfr = sum_mfr(lst)
    sum_lc = sum_lc(lst)
    print("The sum from using map, filter, and sum is: ", sum_mfr)
    print("The sum from using list comprehension is: ", sum_lc)

