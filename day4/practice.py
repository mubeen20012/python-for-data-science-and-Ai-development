#JSON Basics
import json
student = {
    "id": 1,
    "name": "Ali",
    "marks": 88,
    "grade": "A"
}
with open('student.json','w') as file:
    json.dump(student,file,indent=4)
with open('student.json','r') as file:
    data=json.load(file)
print(data)
data['marks']=98
with open('student.json','w') as file:
    json.dump(data,file,indent=4)
print("Updated Json Saved!")
with open('student.json','r') as file:
    data=json.load(file)
print(f"Loaded Json: {data}")
print(f"Name: {data['name']}")