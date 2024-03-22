import pandas as pd 
import os 

def main():
    running = True 
    # checking if the file exists
    if os.path.isfile('grades.csv'):
    # creating a variable to contain the dataframe in the csv
    # using the pandas read csv function makes it easy to gain access to the information stored in a csv from another dataframe
        df = pd.read_csv('grades.csv')
        print("=" * 30)
        print("Tabular Data:")
        # printing the df 
        print(df)
    # if the file does not exist prompt the user to create one then display the information in it 
    else:
        while running:
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


                print("=" * 30)
                print("Tabular Data:")
                print(df)
                # making it a choice for the user to redo the file 
                choice = input("Do you want to go again?(y/n): ")
                # conditional statements based on user choice 
                if choice.lower() == 'y':
                    print("If you want to restart you will have to delete the file.")
                    delete_or_not = input("Do you want to delete your existing file?(y/n): ")
                    if delete_or_not.lower() == 'y':
                        # using os to remove the file 
                        os.remove('grades.csv')
                        print("grades.csv has been deleted.")
                        # passing to continue after the file has been deleted to contine the loop 
                        pass
                    elif delete_or_not.lower() == 'n':
                        # making running = false and just quitting if they do not want to delete the file 
                        running = False
                else:
                    running = False

if __name__ == "__main__":
    main()