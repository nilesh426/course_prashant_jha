# WAP to implement CRUD operations for a student management system using classes in Python.
import sys

class CRUD:
    def __init__(self):
        print("Welcome to Student Management System")
        self.studentID = []
        self.studentName = []
        self.studentRollNo = []
        self.studentCity = []
        
    def addStudent(self):
        self.studentID.append(int(input("Enter student ID: ")))
        self.studentName.append(input("Enter student name: "))
        self.studentRollNo.append(int(input("Enter student roll number: ")))
        self.studentCity.append(input("Enter student city: "))
        
        #view student in table format
    def viewStudent(self):
        print(f"{'ID':<10} {'Name':<20} {'Roll No':<10} {'City':<20}")
        for i in range(len(self.studentID)):
            print(f" {self.studentID[i]:<10} {self.studentName[i]:<20} {self.studentRollNo[i]:<10} {self.studentCity[i]:<20}")
            print("------------------------------------------------------------------")
    
    def updateStudent(self):
        id = int(input("Enter student ID to update:"))
        if id in self.studentID:
            index = self.studentID.index(id)
            print("1. Update Name")
            print("2. Update Roll No")
            print("3. Update City")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.studentName[index] = input("Enter new name: ")
            elif choice == 2:
                self.studentRollNo[index] = int(input("Enter new roll number: "))
            elif choice == 3:
                self.studentCity[index] = input("Enter new city: ")
            else:
                print("Invalid choice.")
                
        print("Student updated successfully.")
            
    def deleteStudent(self):
        id = int(input("Enter student ID to delete:"))
        if id in self.studentID:
            index = self.studentID.index(id)
            print(f"ID: {self.studentID[index]}, Name: {self.studentName[index]}, Roll No: {self.studentRollNo[index]}, City: {self.studentCity[index]}")
            print("Are you sure you want to delete this student? (y/n5" \
            ")")
            confirm = input().lower()
            if confirm == "y":
                self.studentID.pop(index)
                self.studentName.pop(index)
                self.studentRollNo.pop(index)
                self.studentCity.pop(index)
                print("Student deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print("Student ID not found.")
            
crud = CRUD()
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        crud.addStudent()
    elif choice == 2:
        crud.viewStudent()
    elif choice == 3:
        crud.updateStudent()
    elif choice == 4:
        crud.deleteStudent()
    elif choice == 5:
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")