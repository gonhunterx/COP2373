# creating a program that allows the user to create their own function that will increment once  based on the 
# passed argument 
def create_adder(arg1):
    # create the adder function with a second argument for the user to input their second argument 
    def adder(arg2):
        # return the two arguments added together 
        return arg1 + arg2
    # return the adder function 
    return adder

# tests 
add_12 = create_adder(12)
print(add_12(100))
print(add_12(77))
