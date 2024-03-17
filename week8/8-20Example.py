# This is a program to validate one of three date formats.
# If the date entered is valid, the program will calculate
# and print the date in all the formats.

import re

DEBUG = True  # Set to True if you want to execute debug statements
MONTHS = ("January","February","March","April","May","June","July","August",
          "September","October","November","December")

# Match mmddyy
# Note the use of raw (r"something") string format to eliminate the need for escape characters
REGEX1 = r"^(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])([0-9][0-9])$"
def validFmt1(date1):
    if (re.fullmatch(REGEX1, date1)):
        result = re.search(REGEX1, date1)
        if DEBUG: mm = result[1]  # Debug
        if DEBUG: dd = result[2]  # Debug
        if DEBUG: yy = result[3]  # Debug
        if DEBUG: print(f'function says mm = {mm} dd = {dd} yy = {yy}')   #Debug
        if DEBUG: print(f'function says {result.groups()}')  # Debug      
        return result.groups()
    else:
        return None
# Match mm/dd/yyyy    You need to implement this function
def validFmt2(data1):
    # using a very similar regular expression to the first, but also getting the last 4 digits entered 
    REGEX2 = r"^(0[1-9]|1[012])/(0[1-9]|[12][0-9]|3[01])/(\d{4})$"
    if (re.fullmatch(REGEX2, data1)):
        result = re.search(REGEX2, data1)
        if DEBUG: mm = result[1]  # Debug
        if DEBUG: dd = result[2]  # Debug
        if DEBUG: yy = result[3]  # Debug
        if DEBUG: print(f'function says mm = {mm} dd = {dd} yy = {yy}')   #Debug
        if DEBUG: print(f'function says {result.groups()}')  # Debug      
        return result.groups()
    else:
        return None 
    
# Match monthname dd, yyyy
def validFmt3(data1):
    # using [A-Z][a-z]
    REGEX3 = r"^([A-Z][a-z]+) (0[1-9]|[12][0-9]|3[01]), (\d{4})$"
    if (re.fullmatch(REGEX3, data1, re.IGNORECASE)):
        result = re.search(REGEX3, data1, re.IGNORECASE)
        # get the entered month and set as title (which will change the first letter to uppercase and the rest lower)
        # this will allow for me to find the element in the tuple easier 
        month_name = result[1].title()
        # use month_name to get the index of that month from the MONTHS tuple 
        # zfill to ensure there are always 2 digits to avoid errors 
        month_number = str(MONTHS.index(month_name) + 1).zfill(2)
        # return individual parts instead of result.groups()
        return (month_number, result[2], result[3])
    else:
        return None 

#Print three formats from mm, dd, yy)
def printThreeFormats(mm, dd, yy):
    if len(yy) == 2:
        print(f'format 1 = {mm+dd+yy}')
        print(f'format 2 = {(mm + "/" + dd + "/" + "19" + yy)}')
        fmt3 = MONTHS[int(mm) - 1] + " " + dd + ", " + "19" + yy
        print(f'format 3 = {fmt3}')
    else:
        print(f'format 1 = {mm+dd+yy}')
        print(f'format 2 = {(mm + "/" + dd + "/" + yy)}')
        fmt3 = MONTHS[int(mm) - 1] + " " + dd + ", " + yy
        print(f'format 3 = {fmt3}')
        

def main():
    date = input('Enter date: ')
    # is date a valid format 1
    value = validFmt1(date)
    value2 = validFmt2(date)
    
    value3 = validFmt3(date)
    print("=" * 40)

    print("Date formatter: ")
    if value != None:
        printThreeFormats(value[0], value[1], value[2])
        if DEBUG: print(f'Main says {value}') # Debug
    else:
        print(f'{date} is not valid. (first format)')
    print("=" * 40)
    
    if value2 != None:
        printThreeFormats(value2[0], value2[1], value2[2])
    else:
        print(f'{date} is not valid. (second format)')
    print("=" * 40)

    if value3 != None:
        printThreeFormats(value3[0], value3[1], value3[2])
    else:
        print(f'{date} is not valid. (third format)')
    
    # Don't forget this logic structure must be modified to test the other two formats and say not valid 
    # only if date does not match any of the formats
main()
