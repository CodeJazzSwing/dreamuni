import requests
from api import College


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
    new_student = College(id = id, first_name=first_name, last_name=last_name, email=email, us_state=us_state, birthdate=birthdate, major=major)
    res = requests.post(url("/create_student"), json=new_student.dict())  
    print(res)
    

def get_student():
    College_Students = []
    print("Get student")
    try:
        res = requests.get(url("/all"))
        res.raise_for_status()
        data = res.json()
        for College in data:
            print("_______")
            print(f"ID: {College.id}")
            print(f"First Name: {College.first_name}")
            print(f"Last Name: {College.last_name}")
            print(f"Email: {College.email}")
            print(f"US State: {College.us_state}")
            print(f"Birthdate: {College.birthdate}")
            print(f"Major: {College.major}")
            print(res.json())
            College_Students.append(College)
        return College_Students
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)   


def delete_student():
    print("Delete student")
    res = requests.delete(url("/delete_student/{id}")) #Something is messed up here....printing a different error message. 
    print(res.json())
    pass

def update_student():
    print("Update student")
    res = requests.put(url("/update_student"))
    print(res.json())
    pass

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
    print(__name__)
    main()
