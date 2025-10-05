"""import json
import os
file_name='list.json'
def load():
    if os.path.exists(file_name):
      with open(file_name,'r') as file:
          return json.load(file)
    return []
def save(Marks):
    with open(file_name,'w',newline='') as file:
        json.dump(Marks,file)
def list():
    Marks=load()
    while True:
        print("1.Add")
        print("2.View")
        print("3.Update")
        print("4.Delete")
        print("5.Search")
        print("0.Exit")
        try:
            choice=int(input("Choice: ").strip())
            if  choice==1:
                marks=int(input("Marks: ").strip())
                Marks.append(marks)
                save(Marks)
                print(f"Marks {marks} has been added in he list.")
            elif choice==2:
                for i, marks in enumerate(Marks,1):
                    print(f"{i}: {marks}")
            elif choice==3:
                if not Marks:
                    print("Marks List is Empty Now.")
                    return
                id=int(input("ID: ").strip())
                if 1<= id <=len(Marks):
                    new_marks=int(input("Marks: ").strip())
                    Marks[id-1]=new_marks
                    save(Marks)
                    print(f"Marks {new_marks} has been updated.")
                else:
                    print(f"ID {id} not found.")
            elif choice==4:
                if not Marks:
                    print("Marks List is Empty Now.")
                    return
                id=int(input("ID: ").strip())
                if 1<= id <=len(Marks):
                    Marks.pop(id-1)
                    save(Marks)
                    print(f"Marks {id} has been deleted.")
                else:
                    print(f"ID {id} not found.")
            elif choice==5:
                if not Marks:
                    print("Marks List is Empty Now.")
                    return
                id=int(input("ID: ").strip())
                if 1<= id <=len(Marks):
                    marks=Marks[id-1]
                    print(f"ID: {id} found. Marks: {marks}")     
                else:
                    print(f"ID {id} not found.")
            elif choice==0:
                print("Exiting----")
                break
        except ValueError:
            print("Invalid Input, allow only integers.") 

list() """
import csv
import os
file_name='grade.csv'
def load():
    Grades={}
    if os.path.exists(file_name):
        with open(file_name,'r') as file:
            reader=csv.DictReader(file)
            for row in reader:
                ID= int(row['ID'])
                Grades[ID]={
                    'Name': row['Name'],
                    'Class': int(row['Class']),
                    'Grade': int(row['Grade'])
                }
    return Grades

def save(Grades): 
    with open(file_name,'w',newline='') as file:
        fieldnames=['ID',"Name",'Class','Grade']
        writer=csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        print(f"File {Grades} has been saved.")
        for ID,info in Grades.items():
            writer.writerow({'ID':ID,'Name':info['Name'],'Class':info['Class'],'Grade':info['Grade']})
    print(f"File has been saved.")    
def Marks() :

    Grades=load()
    while True:
        print("1.Add")
        print("2.View")
        print("3.Update")
        print("4.Delete")
        print("5.Search")
        print("0.Exit")
        try:
            choice=int(input("Choice: ").strip())
            if  choice==1:
                ID=int(input("ID: ").strip())
                Name=input("Name: ").strip().title()
                Class=int(input("Class: ").strip())
                Grade=int(input("Grade: ").strip())
                Grades[ID]={'Name': Name,'Class': Class,'Grade': Grade}
                save(Grades)
                print(f"Grade of {Name} has been added in list.")
            elif choice==2:
                if not Grades:
                    print("Grade List is Empty Now.")
                    return
                print("\nList of Grade")
                for ID,info in Grades.items():
                    print(f"ID: {ID}: Name: {info['Name']},Class: {info['Class']},Grade: {info['Grade']}")
            elif choice==3:
                if not Grades:
                    print("Grade List is Empty Now.")
                    return
                ID=int(input("ID: ").strip())
                if ID in Grades:
                    print(f"ID {ID} Found.")
                    Grade=int(input("Grade: ").strip())
                    Grades[ID]['Grade']=Grade
                    info=Grades[ID]
                    save(Grades)
                    print(f"ID: {ID}: Name: {info['Name']},Class: {info['Class']},Grade: {info['Grade']} ")
                else:
                    print(f"ID {ID} not Found.")
            elif choice==4:
                if not Grades:
                    print("Grade List is Empty Now.")
                    return
                ID=int(input("ID: ").strip())
                if ID in Grades:
                    print(f"ID {ID} Found.")
                    info=Grades[ID]

                    del Grades[ID]
                    save(Grades)
                    print(f"Grade of {info['Name']} has been deleted.")
                else:
                    print(f"ID {ID} not Found.")
            elif choice==5:
                if not Grades:
                    print("Grade List is Empty Now.")
                    return
                ID=int(input("ID: ").strip())
                if ID in Grades:
                    print(f"ID {ID} Found.")
                    info=Grades[ID]
                    print(f"ID: {ID}: Name: {info['Name']},Class: {info['Class']},Grade: {info['Grade']} ")
                else:
                    print(f"ID {ID} not Found.")
            elif choice==0:
                print("Exiting-----") 
                break    
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input, allow only integers.")
Marks()