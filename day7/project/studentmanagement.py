#Project
#Student Management System
import csv
import os
File_Name='Students.csv'
def load():
    students=[]
    if os.path.exists(File_Name):
        with open(File_Name,'r') as file:
            reader=csv.DictReader(file)
            for row in reader:
                row["ID"] =int(row['ID'])
                row['Marks'] =int(row['Marks'])

                students.append(row)
    return students
def save(students):
    with open(File_Name,'w',newline='') as file:
        fieldnames=['ID',"Name",'Marks','City']
        writer=csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
def students():
    students=load()
    if not students:
     students=[
        {'ID':1,'Name':'Ali','Marks':80,'City':'Lahore'},
        {'ID':2,'Name':'Aliya','Marks':89,'City':'Lahore'},
        {'ID':3,'Name':'Aliyan','Marks':86,'City':'Lahore'},
        {'ID':4,'Name':'Alina','Marks':82,'City':'Lahore'},
        {'ID':5,'Name':'Alyana','Marks':87,'City':'Lahore'} 
        ]
     save(students)
   #append more students
    """students.append({'ID':6,'Name':'Ayesha','Marks':90,'City':'Lahore'})
    #Update students
    students[1]['Marks']=95
    students[0]['Marks']=94
    del students [2]

    for student in students:
        print(f"ID: {student['ID']},Name: {student['Name']},Marks: {student['Marks']},City: {student['City']}")"""
    while True:
        print("\nStudent Management System")
        print("-" * 25)
        print("1. Add Students")
        print("2. View Students")
        print("3. Search Students")
        print("4. Update Students")
        print("5. Delete Students")
        print("0. Exit")
        try:
            choice=int(input("Select option: ").strip())
            if choice==1:
                try:
                 ID=int(input("Enter Id: ").strip())
                 Marks=int(input("Marks: ").strip())
                except ValueError:
                    print("Invalid Input, allow only integers.")
                    continue
                Name=input("Name: ").strip()
                City=input("City: ").strip().title()
                students.append({"ID": ID,"Name": Name,'Marks': Marks,'City': City})
                save(students)
                print(f"Student {Name} Saved Successfully in Students.")
            elif choice==2:
                print("\nList Of All Students")
                print("-" * 28)
                if not students:
                    print("List Is empty.\nStudents have not added in the list yet.")
                else:
                    for student in students:
                        print(f"ID: {student['ID']},Name: {student['Name']},Marks: {student['Marks']},City: {student['City']}")
            elif choice==3:
                try:
                    ID=int(input("ID: ").strip())
                except ValueError:
                    print("Invalid Input, allow only integers.")
                    continue
                found=False
                for student in students:
                    if student['ID']== ID:
                        print(f"Student {ID} Found.\nID: {student['ID']},Name: {student['Name']},Marks: {student['Marks']},City: {student['City']}")
                        found=True
                        break
                if not found:
                    print(f"Student {ID} not found in the list.")
            elif choice==4:
                try:
                    ID=int(input("ID: ").strip())
                except ValueError:
                    print("Invalid Input, allow only integers.")
                    continue
                found=False
                for student in students:
                    if student ['ID']== ID:
                        try:
                            Marks=int(input("Marks: ").strip())
                        except ValueError:
                            print("Invalid Input, allow only integers.")
                            continue
                        student['Marks']=Marks
                        save(students)
                        print(f"Student {ID} Marks has been updated.")
                        found=True
                        break
                if not found:
                    print(f"Student {ID} not found in the list.")
            elif choice==5:
                try:
                    ID=int(input("ID: ").strip())
                except ValueError:
                    print("Invalid Input, allow only integers.") 
                    continue
                found=False
                for student in students:
                    if student['ID'] == ID:
                        students.remove(student)
                        save(students)
                        print(f"Student {ID} deleted Successfully.")   
                        found=True
                        break
                if not found:
                    print(f"Student {ID} not found.")     
            elif choice==0:
                print("Exiting-----")
                break
            else:
                print("Invalid input, allow only integers. ")
        except ValueError:
            print("Invalid Input, allow only integers.")

students()