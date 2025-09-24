#Project To-Do List Manager
def manager():
    To_Do_List=[]
    while True:
       print("\nTo-Do List Manager")
       print('-' * 22)
       print("1. Add Task")
       print("2. View Task")
       print("3. Delete Task")
       print("4. Update Task")
       print("5. Search Task")
       print("0. Exit Task")
       try:
           choice=int(input("Choice: ").strip())
           if choice==1:
               task=input("Task: ").strip().title()
               To_Do_List.append(task)
               print(f"Task {task} has been added in list.")
           elif choice==2:
               if not To_Do_List:
                   print("List is Empty.")
               else:
                 for i,task in enumerate(To_Do_List,1):
                     print(f" {i}: {task}")
           elif choice==3:
               if not To_Do_List:
                    print('Task is not available.')
               else:
                 try:
                     num=int(input("Enter Task number to delete: ").strip())
                     if 1 <= num <=len(To_Do_List):
                         removed=To_Do_List.pop(num -1)
                         print(f"Task {removed} deleted.")
                 except ValueError:
                     print("Invalid Input, allow only integers.")
           elif choice==4:
               if not To_Do_List:
                   print("List is Empty.")
               else:
                   try:
                       num=int(input("Enter task number to update: "))
                       if 1<= num <=len(To_Do_List):
                           new_task=input("Task: ").strip().title()
                           To_Do_List[num -1]= new_task
                           print("Task Updated Successfully.")
                       else:
                           print("Invalid task number.")
                   except ValueError:
                       print("Invalid Input, allow only integers.")
           elif choice==5:
               search=input("Enter Task to search: ").strip().title() 
               if search in  To_Do_List:
                   print(f"Task {search} {To_Do_List.index(search) + 1}.")
               else:
                   print("Invalid Input, allow only integers.")            
           elif choice==0:
               print("Exiting----")
               break
           else:
               print("Invalid choice.")
       except ValueError:
           print("Invalid Input, allow only integers.")               
manager()               

