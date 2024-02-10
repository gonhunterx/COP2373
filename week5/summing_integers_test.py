# creating a program that will sum the triples of the even integers from 2 through 10 

dict_of_users = {
    'jhonnyRocket':{
        'name': 'john',
        'password': 'appleseed123'}, 
    'jacobrancher':{
        'name': 'jacob',
        'password': 'transformerseed123'} 

}   

def user():
    name = 'john'
    password = 'appleseed123'
    
    return name, password

username_exists = lambda u: u in dict_of_users
print(username_exists('jhonnyRocket'))  # Output: True
print(username_exists('notAUser'))



lst = list(range(1, 11))

def is_odd(x):
    return x % 2 != 0
    # returns true or false 
    
print(list(filter(is_odd, lst)))
print(list(filter(lambda x: x % 2 != 0, lst)))





def process_odd_items(lst):
    return [item for item in lst if is_odd(item)]
    
    

    

print(process_odd_items(lst))