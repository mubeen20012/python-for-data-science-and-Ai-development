import csv
import os

file_name = 'list.csv'

def load():
    ToDo_list = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['completed'] = (row['completed'] == 'True') 
                ToDo_list.append(row)
    return ToDo_list

def save(ToDo_list):
    with open(file_name, 'w', newline='') as file:
        fieldnames = ['task', 'completed']   
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for task in ToDo_list:
            writer.writerow({'task': task['task'], 'completed': str(task['completed'])})   # ✅ fix

def Manager():
    ToDo_list = load()
    print("\nWelcome ToDo List Manager")
    print('-' * 23)
    while True:
        print('1.Add a new Task')
        print('2.View all Task')
        print('3.Update Task')
        print('4.Delete Task')
        print('5.Mark Task as Completed')
        print('0.Exit')
        try:
            choice = int(input("Choice: ").strip())
            
            if choice == 1:
                task = input("Task: ").strip().title()
                ToDo_list.append({'task': task, 'completed': False})
                save(ToDo_list)
                print(f"Task {task} has been added in ToDo_list")

            elif choice == 2:
                if not ToDo_list:
                    print("List is Empty.")
                else:
                    for i, task in enumerate(ToDo_list, 1):
                        status = '✔️ Completed' if task['completed'] else '❌ Not Completed'
                        print(f"{i}. {task['task']} [{status}]")

            elif choice == 3: 
                if not ToDo_list:
                    print("List is empty.")
                else:
                    for i, task in enumerate(ToDo_list, 1):
                        print(f"{i}. {task['task']}")
                    try:
                        id = int(input("Enter id to update task: ").strip())
                        if 1 <= id <= len(ToDo_list):
                            new_task = input("Enter new task: ").strip().title()
                            ToDo_list[id-1]['task'] = new_task
                            save(ToDo_list)
                            print(f"Task {id} updated to '{new_task}'.")
                        else:
                            print("Invalid ID.")
                    except ValueError:
                        print("Invalid input, allow only integers.")

            elif choice == 4:
                for i, task in enumerate(ToDo_list, 1):
                    print(f"{i}. {task['task']}")
                try:
                    id = int(input("Enter id to delete task: ").strip())
                    if 1 <= id <= len(ToDo_list):
                        removed = ToDo_list.pop(id-1)
                        save(ToDo_list)
                        print(f"Task '{removed['task']}' has been deleted from list.")
                    else:
                        print("ID not found.")
                except ValueError:
                    print("Invalid input, allow only integers.")

            elif choice == 5:
                if not ToDo_list:
                    print("List is empty.")
                else:
                    for i, task in enumerate(ToDo_list, 1):
                        print(f"{i}. {task['task']} [{'✔️' if task['completed'] else '❌'}]")
                    try:
                        id = int(input("Enter Task id to mark as completed: ").strip())
                        if 1 <= id <= len(ToDo_list):
                            ToDo_list[id-1]['completed'] = True
                            save(ToDo_list)
                            print(f"Task '{ToDo_list[id-1]['task']}' marked as completed.")
                        else:
                            print("Invalid ID.")
                    except ValueError:
                        print("Invalid input, allow only integers.")

            elif choice == 0:
                print("Exit----")
                break

            else:
                print("Invalid Choice.")

        except ValueError:
            print("Invalid input, allow only integers.")

Manager()
