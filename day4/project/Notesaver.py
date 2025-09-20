#🔹 Mini Project – “Daily Notes Saver”
from datetime import datetime
def saver():
  while True:
    print("\nWelcome To Daily Notes Saver")
    print("Daily Notes Saver")
    print("1. Add Notes")
    print("2. View All Notes")
    print("3. Clear Note")
    print("4. Exiting Note")

    try:
        choice=int(input("Choice: ").strip())
        if choice==1:
           note=input("Enter Note: ").strip()
           timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           #save into txt file
           with open('saver.txt','a') as file:
                file.write(f"[{timestamp}] {note}\n")
        elif choice==2:
           print(f"\nAll Notes: ")
           try:
             with open('saver.txt','r') as file:
               for line in file:
                  print(line.strip())
           except FileNotFoundError:
              print("No Notes Found.")
        elif choice==3:
            print("\nClear Note")
            with open('saver.txt','w') as file:
               pass
            print("All Notes Cleared.")
        elif choice==4:
           print("Exiting Daily Note Saver.Gooodbye!")
           break
        else:
            print("Invalid Choice.")
    except ValueError:
        print("Invalid Input, allow only integers.")
saver()