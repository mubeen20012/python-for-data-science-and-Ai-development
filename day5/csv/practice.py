"""import csv
## Step 1: Write 5 students to CSV
with open('students.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['ID',"Name",'Marks'])
    writer.writerow([1,'Ali',78]),
    writer.writerow([2,'Aliya',79]),
    writer.writerow([3,'Aliyan',75]),
    writer.writerow([4,'Alina',76]),
    writer.writerow([5,'Aina',72])
    writer.writerow([6,'Alyiana',71])
with open('students.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
with open('students.csv','r') as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        id=row[0]
        marks=row[2]
        print(f"ID: {id}, Marks: {marks}")
with open('students.csv','r') as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        name=row[1]
        marks=row[2]
        print(f"{name} got {marks} marks")"""
#Using csv.DictWriter
"""import csv
students=[
    {'ID':1, 'Name':'Ali', 'Marks':85},
    {'ID':2, 'Name':'Aliya', 'Marks':90},
    {'ID':3, 'Name':'Aliyan', 'Marks':78},
    {'ID':4, 'Name':'Alina', 'Marks':88},
    {'ID':5, 'Name':'Aina', 'Marks':92}
]
with open('marks.csv','w',newline='') as file:
    fieldnames=['ID','Name',"Marks"]
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    for student in students:
        writer.writerow(student)
with open('marks.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)"""
"""import csv
with open('student.csv','w',newline='')as file:
    writer=csv.writer(file)
    writer.writerow(['ID','Name','Marks'])
    writer.writerow([1,'Ali',85]),
    writer.writerow([2,'Aliya',84]),
    writer.writerow([3,'Aliyan',83]),
    writer.writerow([4,'Alina',82]),
    writer.writerow([5,'Aliyana',81])
with open('student.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
students=[
    {'ID':1, 'Name':'Ali', 'Marks':85},
    {'ID':2, 'Name':'Aliya', 'Marks':90},
    {'ID':3, 'Name':'Aliyan', 'Marks':78},
    {'ID':4, 'Name':'Alina', 'Marks':88},
    {'ID':5, 'Name':'Aina', 'Marks':92}
]
with open('student.csv','w',newline='') as file:
    fieldnames=['ID','Name','Marks']
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    for student in students:
        writer.writerow(student)
with open('student.csv','r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row)
"""
#⏰ Hour 3 – Applied CSV Problems
import csv
with open('mark.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['ID','Name','Marks'])
    writer.writerow([1,'Ali','99']),
    writer.writerow([2,'Alina','89']),
    writer.writerow([3,'Aliyana','98'])
#Read student marks from CSV → calculate average marks.
total=0
count=0
with open('mark.csv','r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row['Name'],row['Marks'])
        total +=int(row['Marks'])
        count+=1
average=total/count if count > 0 else 0
print(f"Average Marks: {average}")
#8. Read CSV → find student with highest mark.
with open('mark.csv','r') as file:
    reader=csv.DictReader(file)
    highest_student=None
    highest_marks=-1
    for row in reader:
        marks=int(row['Marks'])
        if marks > highest_marks:
            highest_marks=marks
            highest_student=row['Name']
print(f"Highest Student: {highest_student} with Marks: {highest_marks}")
#9. Read CSV → print all students with marks > 80.
with open('mark.csv','r')as file:
    reader=csv.DictReader(file)
    print("Students with Marks >80")
    if int(row['Marks']) >80:
        print(f"ID: {row['ID']},Name: {row['Name']},Marks: {row['Marks']}")






    
