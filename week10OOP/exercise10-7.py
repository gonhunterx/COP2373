# Using the datatime module to manipulate dates and times 

from datetime import datetime

# simple function to calculate the difference between two datetime objects
def calculate_dt_diff(x, y):
    return x - y

def main():
    x = datetime.now()
    y = datetime.now()
    
    # displaying the datetime objects 
    print(f'Obj x: {x}\nObj y: {y}')
    
    # displaying individual attributes 
    print(f'x - Year: {x.year}, Month: {x.month}, Day: {x.day}, Hour: {x.hour}, Minute: {x.minute}, Second: {x.second}')
    print(f'y - Year: {y.year}, Month: {y.month}, Day: {y.day}, Hour: {y.hour}, Minute: {y.minute}, Second: {y.second}')

    # conditional statements comparing x and y 
    if x == y:
        print("Date time objects are the same.")
    if x != y:
        print("Date time objects are not the same.")
    
    # calculating the difference between the two variables. 
    diff = calculate_dt_diff(x, y)
    print(f'The difference between x and y is: {diff}')
    
    
if __name__ == "__main__":
    main()