import requests
from typing import List
from api import Student  


def url (route:str): 
    return f"http://127.0.0.1:8000{route}" #The ROUTE adds the end of the URL in each CRUD function.

print("Hello from Student App")

def print_menu():
    print(
        """
    1: Add Student 
    2: Get Student
    3: Delete Student
    4: Update Student
    5: Exit program
    """
    )

def add_student():
    print("Add student")
    id = input("Enter ID #:  ")
    first_name = input("Student first name: ")
    last_name = input("Student last name: ")
    email = input("Email: ")
    us_state = input("US State: ")
    birthdate = input("DOB: ")
    major = input("Major: ")
    new_student = Student(id = id, first_name=first_name, last_name=last_name, email=email, us_state=us_state, birthdate=birthdate, major=major)
    res = requests.post(url("/create_student"), json=new_student.dict())  
    print(res)
    

def get_student():
    print("Get student")
    res = requests.get(url("/all"))
    if not res.status_code ==200:
        return
    data = res.json()
    for College in data:
        print("_______")
        print(College)


#Will run but not delete.
def delete_student():
    print("Delete student")
    student_to_delete = input("Id of student you want to delete: ")
    if not str.isdigit(student_to_delete):
        print("Id's are integers")
        return
    res = requests.delete(url(f"/delete_student/{student_to_delete}"))
    print(res.json())
    

def update_student():
    print("Update student")
    Id_to_update = input("Id of student you want to update: ")
    first_name_to_update = input("First name of student you want to update: ")
    last_name_to_update = input("Last name of student you want to update: ")
    email_to_update = input("Email name of student you want to update: ")
    us_state_to_update = input("US State name of student you want to update: ")
    birthdate_to_update = input("Birthdate name of student you want to update: ")
    major_to_update = input("Major of student you want to update: ")
    new_student = Student(id=int(Id_to_update), first_name=first_name_to_update, last_name=last_name_to_update, email=email_to_update, us_state=us_state_to_update, birthdate=birthdate_to_update, major=major_to_update)
    res = requests.put(url("/update_student"), json=new_student.dict())
    print(res.json())
    
    
def main():
    print_menu()
    choice = input("Choose what you want to do: ")
    choice = choice.strip() #Takes away the blank space at end and still allows function to be called.
    if not str.isdigit(choice):
        print("Print correct option")
        return
    
    match int(choice): #MATCH is new in Python. To run varios IF/ELSE IF. It's like a SWITCH.
        case 1:
            add_student()
        case 2:
            get_student()
        case 3:
            delete_student()
        case 4:
            update_student()
        case 5:
            exit()
        case _:
            print("Enter a valid choice")

    pass

#This is a while loop with an installed function called NAME. To call the MAIN function over and over.
#
while __name__ == "__main__":
    main()