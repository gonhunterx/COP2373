# combined exercises 8.4, 8.5, 8.6
# take an input sentence and tokenize the sentence. 
# part 1: split method and output the tokens in reverse order (white space delimiters)

# part 2: output only words starting with 'b' (white space delimiters)

# part 3: output only the words ending with the letters 'ed' 


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
        # split user_input string again since it is a string again at this point 
        for word in user_input.split():
            # check for words in the split list that start with 'b' 
            if word.startswith('b'):
                # print the words that start with 'b' 
                print(word, end=' ')
        
        # Part 3
        print("\nPart 3 Results: ")
        # split user_input for part 3 
        for word in user_input.split():
            # check for words that end with 'ed'
            if word.endswith('ed'):
                # print words ending with 'ed'
                print(word, end=' ')
                
    except Exception as e:
        print(f"Error at {e}")

# name statement for executing functions from executable file.        
if __name__ == '__main__':
    main()