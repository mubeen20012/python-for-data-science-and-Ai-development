import json
import os

file_name = 'analyzer.json'

def load():
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    return []    

def save(Marks):
    with open(file_name, 'w') as file:  
        json.dump(Marks, file)

Marks = load()   

def Analyzer():
    print("\nWelcome To Student Marks Analyzer.")
    while True:
        print("1. Add Marks")
        print("2. View Marks")
        print("3. Update Marks")
        print("4. Delete Marks")
        print("5. Search Marks")
        print("6. Find Score")
        print("0. Exit")
        try:
            choice = int(input("Choice: ").strip())
            if choice == 1:
                Add()
            elif choice == 2:
                View()
            elif choice == 3:
                Update()
            elif choice == 4:
                Delete()
            elif choice == 5:
                Search()
            elif choice == 6:
                Find()
            elif choice == 0:
                print("Exiting---")
                break
            else:
                print("Invalid input, allow only integers. ")
        except ValueError:
            print("Invalid input, allow only integers.")

def Add():
    try:
        marks = int(input("Add Marks: ").strip())
        Marks.append(marks)
        save(Marks)
        print(f'Marks {marks} has been added in the Marks.')
    except ValueError:
        print("Invalid input, allow only integers.")

def View():
    if not Marks:
        print("Marks List is Empty.")
    else:
        for i, mark in enumerate(Marks, 1):
            print(f"{i}. {mark}")

def Update():
    if not Marks:
        print("Marks List is Empty.")
    else:
        print("\nList Of All Marks: ")
        for i, mark in enumerate(Marks, 1):
            print(f"{i}. {mark}")
        try:
            id = int(input("ID: ").strip())
            if 1 <= id <= len(Marks):
                new_marks = int(input("Enter Marks: ").strip())
                Marks[id-1] = new_marks
                save(Marks)
                print(f"Marks of {id} has been Updated successfully.")
            else:
                print(f"ID {id} not found.")
        except ValueError:
            print("Invalid input, allow only integers.")

def Delete():
    if not Marks:
        print("Marks List is Empty.")
    else:
        for i, mark in enumerate(Marks, 1):
            print(f"{i}. {mark}")
        try:
            id = int(input("ID: ").strip())
            if 1 <= id <= len(Marks):
                Marks.pop(id-1)
                save(Marks)
                print(f"Marks of {id} has been deleted successfully.")
            else:
                print(f"ID {id} not found.")
        except ValueError:
            print("Invalid input, allow only integers.")

def Search():
    if not Marks:
        print("List is Empty.")
    else:
        try:
            id = int(input("Enter Id to search: ").strip())
            if 1 <= id <= len(Marks):
                mark = Marks[id-1]
                print(f"ID {id} found. Marks = {mark}")  
            else:
                print(f"Id {id} not found.")
        except ValueError:
            print("Invalid input, allow only integers.")

def Find():
    while True:
        print("1. Find Max Score")
        print("2. Find Min Score")
        print("3. Find Sum Of All Score")
        print("4. Find Average Score")
        print('0. Back to Main Menu')
        try:
            choice = int(input("Choice: ").strip())
            if choice == 1:
                if not Marks:
                    print("Marks List is Empty.")
                    continue
                Max = Marks[0]
                for mark in Marks:
                    if mark > Max:
                        Max = mark
                print(f"Max Marks: {Max}")   
            elif choice == 2:
                if not Marks:
                    print("Marks List is Empty.")
                    continue
                Min = Marks[0]
                for mark in Marks:
                    if mark < Min:
                        Min = mark
                print(f"Min Marks: {Min}")   
            elif choice == 3:
                total = 0
                for mark in Marks:
                    total += mark
                print(f"Sum Of All Marks is {total}")  
            elif choice == 4:
                if not Marks:
                    print("Marks List is Empty.")
                    continue
                total = 0
                for mark in Marks:
                    total += mark
                Average = total / len(Marks)
                print(f"Average Of All Marks is {Average}")
            elif choice == 0:
                break
            else:
                print("Invalid Input, allow only integers.")
        except ValueError:
            print("Invalid Input, allow only integers.")

Analyzer()
