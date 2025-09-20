#Mini Project: Todo List App
import json
import os
def todo():
    todos=[]
    if os.path.exists('Todo.json'):
        with open('Todo.json','r')as file:
            todos=json.load(file)
    while True:
        print("\n--Mini ToDo List App--")
        print("1.View ToDo")
        print("2.Add ToDo")
        print("3.Delete ToDo") 
        print("4.Save ToDo to json")
        print("5.Load ToDo from Json")
        print("6.Exit ToDo")
        try:
            choice=int(input("Choice: ").strip())
            if choice==1:
                print("\nView ToDo")
            
                if not todos:
                      print("ToDos is empty.No task available.")
                else:
                  print("\nYour Tasks:")
                  for i, task in enumerate(todos,1):
                      print(f"{i}.{task}")
                
            elif choice==2:
                print("\nAdd ToDo")
                while True:
                   task=input("Enter task: ").strip().title()
                   todos.append(task)
                   print(f"Task {task} has been add in todos.")

                   more_task=input("Do you want to add more Task: ").strip().lower()
                   if more_task !='yes':
                       break                    
            elif choice==3:
                if not todos:
                    print("ToDos is empty.No task available.")
                else:
                    print("\nYour Tasks:")
                    for i, task in enumerate(todos,1):
                      print(f"{i}.{task}")
                    try:
                        id=int(input("Enter task number to delete: ").strip())
                        if 1 <= id  <= len(todos):
                              removed=todos.pop(id-1)
                              print(f"task {removed} has been deleted.")
                        else:
                            print(f"ID {id} is not in todos.")
                    except ValueError:
                        print("Invalid Input, allow only integers.")
        
            elif choice==4:
                with open('Todo.json','w') as file:
                    json.dump(todos,file) 
                print("ToDos Saved to todo.json.")
            elif choice==5:
                try:
                    with open('Todo.json','r') as file:
                        todos=json.load(file)
                    print("ToDos Loaded from todo.json.")
                except FileNotFoundError:
                    print("File Not Found.") 
            elif choice==6:
                print("Exit----") 
                break 
            else:
                print("Invalid Input, allow only integers.")
        except ValueError:
            print("Invalid Input, allow only integers.")
                
todo()
