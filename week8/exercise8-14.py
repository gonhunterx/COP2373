# Exercise 8.14 Rebuilding the pervious program; except using regular expressions instead of loops and splits 
import re 


def main(): 
    # use a try except for error handling 
    try:
        # get the input from the user (default input data type is string) 
        input_string = input("Enter a sentence: ")

        # split the string into a list of elements 
        user_input = input_string.split(' ')
        
        # Part 1
        print("Part 1 Results: ")
        # join the elements from the above created list and reverse it
        user_input =  ' '.join(user_input[::-1])
        print(f'{user_input}')
        
        # Part 2
        print("Part 2 Results: ")
        # variable that represents all the occurences of words starting with 'b' 
        words_starting_with_b = re.findall(r'\bb\w*', user_input, re.IGNORECASE)
        # printing the variable and joining them back into a string 
        print(' '.join(words_starting_with_b))
        
        # Part 3
        print("Part 3 Results: ")
        # create a var that represents all the words ending the 'ed'
        words_ending_with_ed = re.findall(r'\w*ed\b', user_input, re.IGNORECASE)
        # join the words stored in the variable
        print(' '.join(words_ending_with_ed))
                
    except Exception as e:
        print(f"Error at {e}")

# name statement for executing functions from executable file.        
if __name__ == '__main__':
    main()