my_dict = {}

country_capitals = {'Nepal': 'Kathmandu',
                    'Uruguay': 'Montevideo',
                    'Belgium': 'Brussels'}


def format_dict(dictionary):
    for key, value in dictionary.items():
        print(key, end='\n')
        print(value, end='\n')




my_dict['december'] = 12
my_dict['february'] = 2



print(format_dict(country_capitals))
print(format_dict(my_dict))

grade_book = {
    'Jadon': [88, 92, 100],
    'Alex': [100, 94, 99],
    'Tom': [79, 96, 77]
}


all_grades_total = 0 
all_grades_count = 0 

for name, grades in grade_book.items():
    total = sum(grades)
    print(f'Average for {name} is {total/len(grades):.2f}')
    all_grades_total += total 
    all_grades_count += len(grades)
    
print(f"Class's average is: {all_grades_total / all_grades_count:.2f}")

from collections import Counter 
num_lst = [44, 24, 44, 124, 4124, 124, 99, 00, 99]

cntr_dict = Counter(num_lst)
for num, value in cntr_dict.items():
    print(f'{num:<12}{value}')
print(f'Number of unique numbers: {len(cntr_dict)}')


grades = {'Sue': [90, 82, 99], 'Bob': [99, 91, 100]}

grades2 = {k: round(sum(v) / len(k), 2) for k, v in grades.items()}
print(grades2)


numbers = {number: number ** 3 for number in range(1, 6)}
print(numbers)

text1 = 'to be or not that is the question'

cleaned_text1 = text1.split()
for word in sorted(cleaned_text1):
    print(word, end=' ')
# print(sorted(cleaned_text1))

print(set('abc def ghi jkl mno').issuperset('hi mom'))



nums = list(range(10)) + list(range(5))
print(nums)
print(set(nums))