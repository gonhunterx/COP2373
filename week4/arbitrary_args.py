# creating a program that will allow the user to enter any number of integers and view the results of their product 

# creating the product function and using "*" before args to take in any number of args 
def product(*args):
    # if args == 0 return 0 
    if args == 0:
        product = 0
        return product 
    product = 1
    # create a for loop for the num of args in the list 
    for num in args:
        # increment with the multiplied value 
        product *= num
    # return the final product outside of the loop  
    return product 

# main function for menu and logic calls 
def main():
    # try except for simplifying exiting the program 
    try:
        while True:
            # creating a list to store the values input 
            inputs = []
            # making a counter for the number of inputs entered 
            count = 1
            print("How many numbers would you like to calculate the product of?(ctrl + c to exit)")
            # variable storing the number of inputs as an interger 
            num_of_numers = int(input("Num of numbers: "))
            
            # for loop just to iterate through the range of desired numbers to enter
            for _ in range(num_of_numers):
                # create a value to append to the list 
                val = int(input(f"Input {count}: "))
                # append
                inputs.append(val)
                # increment count 
                count += 1
            # create a result fo the products function to print 
            res = product(inputs)
            print(f"Inputs: {inputs}")
            print(res)
    # end of try except 
    except KeyboardInterrupt:
        print("\nExiting...")
        
# name statement for executing 
if __name__ == "__main__":
    print(f'The correct answer is 362880, product function answer is {product(1, 2, 3, 4, 5, 6, 7, 8, 9)}')
    print(f'The correct answer is 1500, product function answer is {product(5, 3, 100)}')
    print(f'The correct answer is 0, product function answer is {product()}')
    main()