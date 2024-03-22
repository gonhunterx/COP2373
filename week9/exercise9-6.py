# Class average written to JSON program
import json
gradebook_dict = {'students':[]}
def main():
    try:
        # get the number of students
        num_of_students = int(input("Enter number of students: "))
        # a for loop for each student
        for _ in range(num_of_students):
            # getting the values for the dataframe
            first_name = input("Input first name: ").strip()
            last_name = input("Input last name: ").strip()
            # input list comprehension for creating grades for the individual
            #student
            grades = [float(input(f"Enter grade {i + 1}/3: ")) for i in range(3)]
            
            new_student = {'first_name': first_name, 'last_name':last_name,'exam1':grades[0], 'exam2':grades[1], 'exam3':grades[2]}
        
            # append a new dict to the gradebook students value section
            gradebook_dict['students'].append(new_student)
        with open('grades.json', 'w') as file:
        # dump the gradebook into the grades.json file
            json.dump(gradebook_dict, file)
    except Exception as e:
        print(f"Error at {e}")
if __name__ == "__main__":
    main()
