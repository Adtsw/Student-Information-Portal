from model.user import User
from model.student import Student
from services.auth_service import AuthService
from services.student_service import StudentService
from mysql.connector import Error
from database.db_manager import DBManager
from config import DB_CONFIG
from validators.validator import student_validator, user_validator

def userOptions(db):
    
    while True:
        print("\nUser Options: ")
        print("1. Add User")
        print("2. Authenticate User to see Student Options")
        print("Any other key to Exit")
        
        choice = int(input("Enter your choice (1-2): "))
        auth = AuthService(db)
        
        if choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (admin/viewer): ")
            
            userValidator = user_validator(username, password, role)
            
            if isinstance(userValidator, str):
                print(userValidator)
                break
            
            user = User(username, password, role)
            
            try:
                rowID = auth.addUser(user.username, user.password, user.role)
                print(f"User {username} added successfully!")
            except Error as e:
                print(f"Error adding user: {e}")
                rowID = None
                
        elif choice == 2:
            print("Welcome to the User Login Portal!")
            username = input("Enter username: ")
            password = input("Enter password: ")
            
            userRole = auth.authenticate(username, password)
            
            if userRole == "admin":
                print("\nLogged in as Admin.")
                adminOptions(db)
            elif userRole == 'viewer':
                print("\nLogged in as Viewer.")
                viewerOptions(db)
            else:
                print(userRole)
        
        else:
            print("Exiting User Options.")
            db.close()
            break

def adminOptions(db):
    while True:
        print("\nAdmin Options: ")
        print("1. Add a student")
        print("2. Update a student")
        print("3. Delete a student")
        print("4. Search for a student")
        print("Any other key to Logout")
        
        choice = int(input("Enter your choice: "))
        service = StudentService(db)
        
        if choice == 1:
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            email = input("Enter student email: ")
            course = input("Enter student course: ")
            
            studentValidator = student_validator(name, age, email, course)
            
            if isinstance(studentValidator, str):
                print(studentValidator)
                break
            
            student = Student(name, age, email, course)
            
            try:
                rowID = service.addStudent(student)
                print(f"Student {name} added successfully!")
            except Error as e:
                print(f"Error adding student {name}: {e}")
                rowID = None
        
        elif choice == 2:
            email = input("Enter student email: ")
            
            newName = input("Enter new name (leave blank to keep unchanged): ")
            newAge = int(input("Enter new age (leave blank to keep unchanged): "))
            newEmail = input("Enter new email (leave blank to keep unchanged): ")
            newCourse = input("Enter new course (leave blank to keep unchanged): ")
            
            newData = {}
            
            if newName:
                newData['name'] = newName
            if newAge:
                newData['age'] = newAge
            if newEmail:
                newData['email'] = newEmail
            if newCourse:
                newData['course'] = newCourse
            
            try:
                result = service.updateStudents(email, newData)
                print(f"Student with email {email} updated successfully!")
            except Error as e:
                print(f"Erro rupdating student with email {email}: {e}")
                result = None
                
        elif choice == 3:
            email = input("Enter student email to delete: ")
            
            try:
                result = service.deleteStudent(email)
                print(f"Student with email {email} deleted successfully!")
            except Error as e:
                print(f"Error deleting student with email {email}: {e}")
                result = None
                
        elif choice == 4:
            name = input("Enter student name to search: ")
            
            try:
                student = service.getStudent(name)
                
                if isinstance(student, str):
                    print(student)
                else:
                    for s in student:
                        print(f"\nStudent ID: {s['student_id']}")
                        print(f"Name: {s['name']}")
                        print(f"Age: {s['age']}")
                        print(f"Email: {s['email']}")
                        print(f"Course: {s['course']}")
                        print("\n")
            except Error as e:
                print(f"Error searching for student with name {name}: {e}")
                student = None
            
        else:
            print("Logging out from Viewer Options.")
            break
                
def viewerOptions(db): 
    while True:
        print("\nViewer Options: ")
        print("1. Search for a student")
        print("Any other key to Logout")
        
        choice = int(input("Enter your choice: "))
        service = StudentService(db)
        
        if choice == 1:
            name = input("Enter student name to search: ")
            
            try:
                student = service.getStudent(name)
                
                if isinstance(student, str):
                    print(student)
                else:
                    for s in student:
                        print(f"\nStudent ID: {s['student_id']}")
                        print(f"Name: {s['name']}")
                        print(f"Age: {s['age']}")
                        print(f"Email: {s['email']}")
                        print(f"Course: {s['course']}")
                        print("\n")
            except Error as e:
                print(f"Error searching for student with name {name}: {e}")
                student = None
            
        else:
            print("Logging out from Viewer Options.")
            break
        
def main():
    try:
        dbManager = DBManager(**DB_CONFIG)
        userOptions(dbManager)
    except Error as e:
        print(f"Database connection failed: {e}")
    finally:
        if 'dbManager' in locals():
            dbManager.close()
    
if __name__ == "__main__":
    main()
    
        
            
            
            
            