def students():
    students=[
        {"id":1,'name':'ali','marks':[20,30,34]},
        {"id":2,'name':'aliya','marks':[24,37,35]},
        {"id":3,'name':'aliyan','marks':[29,31,44]},
        {"id":4,'name':'alina','marks':[22,38,39]},

    ]
    #Add student
    students.append({"id":5,'name':'aina','marks':[25,28,49]})
    print(students[1]['name'])
    #update marks
    students[1]['marks']=[26,31,34]
    #Delete student
    del students[1]
    for student in students:
        print(f"ID: {student['id']},Name: {student['name']},Marks: {student['marks']}")
    #Search by ID
    try:
        id=int(input("ID: ").strip())
        found=False
        for student in students:
            if student['id']==id:
              print(f"{id} Found ID: {student['id']},Name: {student['name']},Marks: {student['marks']}")
              found=True
              break
        if not found:
            print(f"ID {id} not found.")
    except ValueError:
        print("Invalid Input,allow only integers.")
        
students()