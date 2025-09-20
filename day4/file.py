#Practice problems:
# Write 5 student names into a text file (one per line).
"""with open('file.txt','w') as file:
    for i in range(5):
      name=input("Name: ").strip().title()
      file.write(name + '\n')
with open('file.txt','r') as file:
    for line in file:
        print(line.strip())"""
#Save a dictionary of student marks to JSON.
"""import json
student={
    'name': 'Alina',
    'marks':89

}
with open('students.json','w') as file:
    json.dump(student,file,indent=4)
with open('students.json','r') as file:
    data=json.load(file)
print(f"Loaded Data: {data}")
print(f"Name: {data['name']}")
print(f"Name: {data['marks']}")
#Load JSON and calculate average marks.

with open('students.json','r') as file:
    data=json.load(file)
total=0
for s in data:
    total +=s['marks']
average=total/len(data)
print(f"Loaded Data: {data}")
print(f"Total: {'total'}")
print(f"Average Marks: {average}")

"""
import json
def students():

    
    students=[
        {'id':1,'name':'ali','marks':89},
        {'id':2,'name':'aliyan','marks':99},
        {'id':3,'name':'aliya','marks':79}

    ]
    students.append({'id':4,'name':'alina','marks':69})
    #add new key
    for student in students:
        student['city']='lahore'
    students[1]['city']= 'islamabad'
    del students[1]
    for student in students:
        print(f"ID: {student['id']},Name: {student['name']},Marks: {student['marks']},City: {student['city']}")
    with open('marks.json','w') as file:
        json.dump(students,file,indent=4)
    try:
        id=int(input("Enter Id: ").strip())
        found=False
        for student in students:
            if student['id'] == id:
                print(f"ID Found-> ID: {id},Name: {student['name']},Marks: {student['marks']},City: {student['city']}")
                found=True
        if not found:
            print(f"ID {id} not found.")
    except ValueError:
        print("Invalid input, allow only integers.")
    with open('marks.json','r') as file:
        data=json.load(file)
    total=0
    for student in data:
        total+=student['marks']
    average=total/len(data)

    print(f"Loaded Data: {data}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average}")



students()




