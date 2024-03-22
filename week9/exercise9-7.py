# Class average written to JSON program 
import json 

def main():
        try:
            with open('grades.json', 'r') as students:
                # Load the gradebook from the grades.json file 
                data = json.load(students)
                # print(data['students'][0]['first_name'])
                
                # using the len to find the total number of students in the file 
                num_of_students = len(data['students'])
                
                # creating a for loop from the number of students 
                for i in range(num_of_students):
                    # creating a total of the exams 
                    exam_grade_total = data['students'][i]['exam1'] + data['students'][i]['exam2'] + data['students'][i]['exam3']
                    # creating a new key 'average' and setting its value for the specific student's average 
                    data['students'][i]['average'] = exam_grade_total / 3 
                
                # printing the column names before starting the loop to print the data 
                print(f'{"First Name":<12}{"Last Name":<12}{"Exam1":<6}{"Exam2":<6}{"Exam3":<6}{"Avg":<5}')

                # loop for printing the student data 
                for student in data['students']: 
                    f_name = student['first_name']
                    l_name = student['last_name']
                    exam1 = student['exam1']
                    exam2 = student['exam2']
                    exam3 = student['exam3']
                    average = student['average']
                    print(f'{f_name:<12}{l_name:<12}{exam1:<6}{exam2:<6}{exam3:<6}{average:<5.2f}')  

        except Exception as e:
            print(f"Error at {e}")
            
if __name__ == "__main__":
    main()