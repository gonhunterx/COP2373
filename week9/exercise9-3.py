# Class average written to CSV program 

import pandas as pd 

def main():
        try:
            # get the number of students 
            num_of_students = int(input("Enter number of students: "))
            # create a list to store the data collected to use in the dataframe 
            data = []
            # a for loop for each student 
            for _ in range(num_of_students):
                # getting the values for the dataframe 
                first_name = input("Input first name: ").strip()
                last_name = input("Input last name: ").strip()
                # input list comprehension for creating grades for the individual student 
                grades = [float(input(f"Enter grade {i + 1}/3: ")) for i in range(3)]
                # append the values to data list 
                data.append([first_name, last_name] + grades)

            # creating the dataframe from the data and a list of names for the columns 
            df = pd.DataFrame(data, columns=['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

            # writing the df to grades.csv
            # setting index to false so it does not appear in the csv file
            df.to_csv('grades.csv', index=False)
            
        except Exception as e:
            print(f"Error at {e}")
            
if __name__ == "__main__":
    main()