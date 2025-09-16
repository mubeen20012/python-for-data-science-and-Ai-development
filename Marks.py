#Mini Project: Student Marks List Analyzer
def marks():
    total=0
    freq={}
    unique=[]
    marks=[78, 90, 56, 88, 90, 78]
    for mark in marks:
        if mark in freq:
            freq[mark]+=1
        else:
            freq[mark]=1

        if mark not in unique:
            unique.append(mark)
    #sum of marks
        total+=mark
    
    average=total/len(marks)
    
    highest=marks[0]
    for mark in marks:
        if mark > highest:
            highest=mark
    lowest=marks[0]
    for mark in marks:
        if mark < lowest:
            lowest=mark
    highest=second=marks[0]
    for mark in marks:
        if mark > highest:
            second=highest
            highest=mark
        elif mark > second and mark != second:
             second= mark
    print(f"\n--Student Marks Analyzer--\n")
    print("--------------------------------")
    print(f"Marks: {marks}")
    print(f"Sum Of all Marks is: {total}")
    print(f"Average: {average:.2f}")
    print(f"Highest Marks is: {highest}")
    print(f"Second Highest Marks is: {second}")
    print(f"Lowest Marks is: {lowest}")
    print(f"Unique: {unique}")
    print(f"Frequency: {freq}")
    """unique=set(marks)
    print(unique)"""
    

marks()