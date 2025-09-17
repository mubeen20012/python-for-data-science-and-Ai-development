#Dictionaries
#Basics of Dictionaries
#Create a dict with your own details (id, name, age).
"""def students():
    students={'id': 1,'name':'Ali','marks':56}
    print(students['name'])
    #Update your age.
    students['marks'] =90
    #Delete one key.
    del students['marks']
    print(students)
    #Access a value safely with .get().
    print(students.get('age','not found'))
students()
"""
#Nesting (Dict in List, List in Dict)
"""students=[
    {'id':1,'name':'ali','age':21},
    {'id':2,'name':'aliya','age':23}
]

students.append({'id':3,'name':'aliyan','age':24})
for student in students:
    print(student['id'],student['name'],student['age'])
"""
#5. Store 3 students with their marks (list of dicts).

"""students=[
    {"id":1,'name':'ali','marks':[20,39,45]},
    {"id":2,'name':'aliya','marks':[21,33,50]},
    {"id":3,'name':'aliyan','marks':[23,31,49]}
]
for student in students:
    print(student['id'],student['name'],student['marks'])
for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"marks: {student['marks']}")
    print("-" * 20)
#6. Access the 2nd student’s name.
print(students[1]['name'])
#7. Print all marks of the first student.
print(students[0]['marks'])"""
#Looping in Dicts
"""students={
    'name': 'Ali',
    'age': 23,
    'marks': 67
}
#8. Print all keys of a student dict.
for key in students.keys():
    print(key)
#9. Print all values.
for value in students.values():
    print(value)
for key, value in students.items():
    print(key,value)
print(students.get('id','not found'))
students=[
    {'name': 'Ali','age': 22},
    {'name': 'Aliya','age': 23},
    {'name': 'Aliyan','age': 24}
]
for student in students:
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print("-"*20)
#Create a dictionary of 3 students with their ages. Print all names and ages.
students={
    "amina":{'Age':21,'city':"Lahore"},
    "amin":{'Age':22,'city':"Lahore"},
    "ali":{'Age':23,'city':"Lahore"}

}
#Add a new key "city" to the dictionary and update its value.
#Add a new key "marks" to the dictionary and update its value.

for name, info in students.items():
    info['marks']=78

    print(f"Name: {name} ,Age: {info['Age']},'City': {info['city']},Marks: {info['marks']}")"""
##Create a dictionary of 3 students with their marks in Math. Print it.
def students():
    students={
        'ali': {'marks': 67},
        'aliya': {'marks': 67},
        'aliyan': {'marks': 67}

    }
    students['aliyan']['marks']=90
    students['aliya']['marks']=70
    del students['ali']
    for name in students:
      students[name]['City']='Lahore'
    print(students['aliya'])
#Add a new key-value pair: Add "Usman": 95 to the dictionary.
    students['usman']={'marks':90,'City':"Lahore"}
    for name,info in students.items():
        print(f"Name: {name},Marks: {info['marks']},City: {info['City']}")
#Check if a key exists: Write a program that asks for a student name and checks if it exists in the dictionary.
    name=input("Enter Name: ").strip()
    if name in students:
       print(f"Name: {name},Marks: {students[name]['marks']}")
    else:
       print(f"Student {name} not found.")
students()



