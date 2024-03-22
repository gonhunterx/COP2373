import os 

with open('accounts.txt', mode='w') as accounts:
    accounts.write('100 Jones 24.98\n')
    accounts.write('200 Doe 292.98\n')
    accounts.write('300 White 445.98\n')
    accounts.write('400 Stone -14.98\n')
    accounts.write('500 Rich 224.98\n')
    

# updating accounts.txt 
accounts = open('accounts.txt', 'r')
temp_file = open('temp_file.txt', 'w')

# Saving and having to change values and not losing the proper formatting 
with accounts, temp_file:
    for record in accounts:
        account, name, balance = record.split() 
        if account != '300':
            temp_file.write(record)
        else:
            new_record = ' '.join([account, 'Williams', balance])
            temp_file.write(new_record + '\n')

# printing accounts 

with open('temp_file.txt', mode='r') as tmp_file:
    print(f'{"Account":<10}{"Name":<10}{"Balance":<10}')
    for record in accounts:
        account, name, balance = record.split()
        print(f'{account:<10}{name:<10}{balance:<10}')

with open('accounts.txt', mode='r') as accounts:
    print(f'{"Account":<10}{"Name":<10}{"Balance":<10}')
    for record in accounts:
        account, name, balance = record.split()
        print(f'{account:<10}{name:<10}{balance:<10}')

# Grades file         
with open('grades.txt', mode='w') as grades:
    grades.write('8492 Jared 89\n')
    grades.write('8493 Jadon 99\n')
    grades.write('8494 Bob 95\n')
    grades.write('8495 Robert 83\n')

with open('grades.txt', mode='r') as grades:
    print(f'{"ID":<10}{"Name":<10}{"Grade":<10}')
    for record in grades:
        id_1, name, grade = record.split()
        print(f'{id_1:<10}{name:<10}{grade:<10}')