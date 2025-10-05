#Project:Library Management System
def library():
    while True:
        print("1. Add New Book")
        print("2. View Book")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Search Book")
        print("0. Exit")
        try:
            choice=int(input("Choice: ").strip())
            if choice==1:
                Add()
            elif choice==2:
                View()
            elif choice==3:
                Update()
            elif choice==4:
                Delete()
            elif choice==5:
                Search()
            else:
                print("Invalid Choice.")
        except ValueError:
            print("Invalid Input, allow only integers.")
Library={}
def Add():
    try:
        ID=int(input("Enter ID: ").strip())
        Year=int(input("Enter Year: ").strip())
        Copies=int(input("Enter Copies: ").strip())
    except ValueError:
            print("Invalid Input, allow only integers.")
    Title=input("Enter Title: ").strip().title()
    Author=input("Enter Author: ").strip().title()
    Library[ID]={'Year':Year,'Copies':Copies,'Title':Title,'Author':Author}
    print(f"Book {Title} has been added in the Library.")
def View():
    if not Library:
        print("Book is not available in the Library.")
    else:
        for ID,book in Library.items():
            print(f"ID: {ID},Title: {book['Title']},Author: {book['Author']},Year: {book['Year']},Copies: {book['Copies']}")
def Update():
    if not Library:
        print("Book is not available in the Library.")
        return
    try:
        ID=int(input("Enter ID to update: ").strip())
    except ValueError:
        print("Invalid Input, alllow only integers.")
        return
    found=False
    for ID in Library:
        print(f"ID {ID} Found.")
        try:
            Copies=int(input("Copies: ").strip())
            Library[ID]['Copies']=Copies
            book=Library[ID]  
            print(f"ID: {ID},Title: {book['Title']},Author: {book['Author']},Year: {book['Year']},Copies: {book['Copies']}")
            found=True
            break
        except ValueError:
            print("Invalid Input, allow only integers.")
    if not found:
        print(f"ID {ID} Found.")
def Delete():
    if not Library:
        print("Book List is Empty.")
        return
    try:
        ID=int(input("Enter ID: ").strip())
    except ValueError:
        print("Invalid Input, allow only integers.")
        return
    if ID in Library:
        del Library[ID]
        print(f"ID {ID} has been deleted.")
    else:
        print(f"ID {ID} not Found.")
def Search():
    if not Library:
        print("Book list is empty.") 
        return
    try:
        id=int(input("Enter ID: ").strip())
    except ValueError:
        print("Invalid input, allo only integers.") 
        return
    found=False
    for ID in Library:
        if Library[ID] == id:
            print(f"ID {id} Found.")
            book=Library[ID]
            print(f"ID: {ID},Title: {book['Title']},Author: {book['Author']},Year: {book['Year']},Copies: {book['Copies']}")
            found=True
            break
    if not found:
        print(f"ID {id} not found.")

library()




       

