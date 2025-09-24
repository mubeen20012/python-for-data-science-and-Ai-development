#Mini Project: Calculator with Error Handling
import csv
import os
File_Name='calculator.csv'
def load():
  if os.path.exists(File_Name):
    with open(File_Name,'r') as file:
        reader=csv.DictReader(file)
        print("\n---Previous Calculation---")
        for row in reader:
            print(f"{row['Num1']} {row['Operator']} {row['Num2']} = {row['Result']}")
  else:
      print("No Previous History Found.")
def save(num1,operator,num2,result):
    file_exists = os.path.exists(File_Name)

    with open(File_Name,'a') as file:
        fieldnames=['Num1','Operator','Num2','Result']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        if not file_exists:  # write header only once
            writer.writeheader()
        
        writer.writerow({
            "Num1": num1,
            "Operator": operator,
            "Num2": num2,
            "Result": result
        })
        

def calculator():
    print("\nWelcome To Mini Calculator!")
    load()
    while True:
        try:
            num1=float(input("Number: ").strip())
            num2=float(input("Number: ").strip())
            operator=input("Enter Operator(+,-,*,/) or q to quit: ").strip().lower()
            if operator == 'q':
                print("Exiting-----")
                break
            operations={
            '+': num1 + num2,
            '-': num1 - num2,
            '*': num1 * num2,
            '/': num1 / num2 if num2!=0  else 'Error: Division By Zero'
            }
            result=(operations.get(operator,'invalid operator'))
            print(f"Result: {result}")
            save(num1,operator,num2,result)
        except ValueError:
            print("Invalid Input, allow only integers.")
calculator()
