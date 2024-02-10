# for exercise 5.9 I am creating a palindrome tester. It will
# take in a string argument and return whether or not the string is the same 
# reversed as it is in its standard arrangement.

# take in any string as the param 
def is_palindrome(string: str):
    # Try except for error handling and catching bugs 
    try:
        # list of tuples used to replace characters in the string 
        replacements = [('!', ''), ('?', ''), ('"', ''), ('.', ''), (',', ''), (':', ''), (' ', '')]
        for char, replacement in replacements:
            # looping through the string to check for characters that match replacements 
            if char in string:
                # replacing 
                string = string.replace(char, replacement)
        # set string to lower for comparison 
        string = string.lower()
        
        # ::-1 reverses the string and we check if it equals the original value 
        if string[::-1] == string: 
            return True 
        else:
            return False  
    # exception handling 
    except Exception as e:
        print(f"Error at {e}")
        

# main statement for testing function         
if __name__ == "__main__":
    print(f"Monday is not a palindrome, is_palindrome says {is_palindrome('Monday')}")
    print(f"able was i ere I Saw elba is a palindrome, is_palindrome says {is_palindrome('able was i ere I Saw elba')}")
    print(f"radar is a palindrome, is_palindrome says {is_palindrome('radar')}")
    print(f"able was i, ere I Saw elba: is a palindrome, is_palindrome says {is_palindrome('able was i, ere I Saw elba:')}")
    print(f"1249124 is not a palindrome or string: {is_palindrome(1248124)}")