"""#Lists
#Make a list of 5 student names and update the 3rd one.
students=['Ali','Aiman','Ayesha','bilal','Aina']
students[2]='Alina'
#Remove an item from the list.
del students[1]

for student in students:
    print(student)
#Slice first 3 items from the list.
students[:3]
#Use list comprehension: [x**2 for x in range(1, 6)].
square=[x**2 for x in range(1,6)]
print(square)
#14. Create a new list with squares of numbers from 1–10.
squares=[]
for i in range(1,11):
    square=i **2
    squares.append(square)
print(squares)
square=[x**2 for x in range(1,11)]
print(square)


"""
"""#Create a list of 5 numbers and print it.
numbers=[1,2,3,4,5]
#Access elements: print the first, last, and middle element.
print(numbers[0])
print(numbers[4])
print(numbers[2])
for num in numbers:
    print(num)"""
##Modify a list: change the 2nd element to a new value.
"""def numbers():
    numbers=[1,2,3,4,5]
    numbers[1]=9
    for num in numbers:
        print(num)
numbers()"""
#Add a new element at the end and at the beginning of a list.
"""def list():
    number=[1,2,3,4,5]
    number.append(9)
    number.insert(0,8)
#Remove an element by value and by index.
    del number[3]
    for num in number:
        print(num)
list()"""
#Take a list of numbers → print only even numbers using a loop.
"""def even():
    numbers=[]
    for number in range(1,21):
        numbers.append(number)
        if number %2==0:
            print(number)
even()
"""
"""def even():
    numbers=[]
    for number in range(1,21):
        numbers.append(number)
    print(numbers)
even()"""
"""def even():
    numbers=[]
    for number in range(1,21):
        numbers.append(number)
        for number in numbers:
          if number %2==0:
            print("Even")
          else:
             print(number)
even()"""
##Find the sum and average of a list of numbers.
"""def sum():
    sum=0
    numbers=[]
    for number in range(1,11):
        numbers.append(number)
        for number in numbers:
          sum += number
    print(f"Sum of All numbers is: {sum}")
    average=sum/len(numbers)
    print(f"Average: {average}")
sum()"""
#Find largest and smallest number in a list without using max() or min().
"""def largest():
    numbers=[]
    for number in range(3):
        number=int(input("Enter Numbers: ").strip())
        numbers.append(number)
    largest=numbers[0]
    for num in numbers:
        if num > largest:
            largest= num
    print(f"Largest: {largest}")
largest()"""
"""def largest():
    numbers=[]
    for number in range(3):
        number=int(input("Enter Numbers: ").strip())
        numbers.append(number)
    smallest=numbers[0]
    for num in numbers:
        if num < smallest:
            smallest= num
    print(f"Smallest: {smallest}")
largest()"""
"""def largest():
    numbers=[]
    for number in range(3):
        number=int(input("Enter Numbers: ").strip())
        numbers.append(number)
    largest=second=numbers[0]
    for num in numbers:
        if num > largest:
            second= largest
            largest= num
        elif num > second and num != second:
            num=second
    print(f"Largest: {largest}")
    print(f"Second Largest: {second}")

largest()
"""
#Reverse a list using a loop (don’t use [::-1] or reverse()).
"""def reverse():
    numbers=[1,2,3]
    reverse=[]
    for num in numbers:
        reverse.insert(0,num)
    print(f"Reverse: {reverse}")
reverse()"""
"""text=input("Enter Text: ").strip()
reverse=text[::-1]
print(reverse)
"""
"""def reverse():
    text=input("Text: ").strip()
    reverse=''
    for char in text:
        reverse=char + reverse
    print(f"Reversed: {reverse}")
reverse()"""
"""def reverse():
    numbers=[1,2,3]
    reverse=numbers[::-1]
    print(f"Reverse: {reverse}")
reverse()"""
"""def reverse():
    try:
        number=int(input("Enter Number: ").strip())
        reverse=0
        while number >0:
            digit=number%10
            reverse=reverse * 10 + digit
            number//=10
        print(f"Number: {reverse}")
    except ValueError:
        print("Invalid Input, allow only integers")
reverse()"""
"""def armstrong():
    try:
        number=int(input("Number: ").strip())
        number_digit=len(str(number))
        sum=0
        temp=number
        while temp>0:
            digit=temp%10
            sum+=digit ** number_digit
            temp//=10
        if sum == number:
            print(f"{number} is armstrong.")
        else:
            print(f"{number} is not armstrong.")
    except ValueError:
        print("Invalid Input,allow only integers.")
armstrong()"""
#factorial
"""def factorial():
    try:
        number=int(input("Enter Number: ").strip())
        result=1
        for i in range(1,number+1):
            result *=i
        print(f"Factorial: {result}")
    except ValueError:
        print("Invalid Input, allow only integers.")
factorial()"""
#fibonnaci
"""def fibonnaci():
    try:
        number=int(input("Enter Number: ").strip())
        a,b=0,1
        for i in range(1,number+1):
            print(a,end='')
            a,b=b,a+b
    except ValueError:
        print("Invalid Input,allow only integers.")
fibonnaci()"""
#Find unique numbers from [1,2,2,3,4,4,5].
"""def unique():
    unique=[]
    numbers=[1,2,2,3,4,4,5]
    for num in numbers:
        if num not in unique:
            unique.append(num)
    print(unique)
unique()"""
#Count frequency of elements in [‘apple’,‘banana’,‘apple’,‘orange’].
"""def frequency():
    freq={}
    fruits=['apple','banana','apple','orange']
    for fruit in fruits:
        if fruit in freq:
            freq[fruit] +=1
        else:
            freq[fruit] =1
    print(f"Fruits: {freq}")
frequency()"""
#🔹 Tuple Examples
#Create a Tuple
"""student=('Musfira',22,'IT Graduate')
print(student)
#Tuple Unpacking
name,age,profession=student
print(name)
print(age)
print(profession)"""
#Swap Variables
"""a=7
b=9
a,b=b,a
print(a,b)"""
#Store Coordinates
"""point=(4,7)
print('X: ',point[0])
print('Y: ',point[1])
"""
#Convert List → Tuple
"""numbers=[1,2,3]
num=tuple(numbers)
print(num)
"""
#Sets
"""numbers={1,2,3,3,4}
print(numbers)"""
#Create a Set
"""fruits={"apple", "banana", "orange", "apple"}
print(fruits)"""
#Convert List → Set
"""numbers=[1,2,3,3,4,4,5]
number=set(numbers)
print(number)"""
#Add & Remove Elements
"""numbers={1,2,3}
numbers.add(7)
numbers.remove(2)
numbers.discard(10)
print(numbers)"""
#Check if an Item Exists
"""nums={1,2,3,4}
print(3 in nums)
print(10 in nums)"""
#5. Union (OR) & Intersection (AND)
"""a={2,3,4}
b={4,5,6}
print(a | b)
print(a & b)
print(a - b)
"""
#Practice Problems
#Convert [1,2,2,3,3,4] into a set.
"""numbers=[1,2,2,3,3,4]
number=set(numbers)
print(number)"""
#Find union and intersection of {1,2,3} and {3,4,5}.
"""a={1,2,3}
b={3,4,5}
print(a | b)
print(a & b)
print(a - b)
"""
#Remove an element from {10,20,30,40}.
numbers={10,20,30,40}
numbers.remove(20)
numbers.add(60)
#Check if 50 exists in {10,20,30,40}.
print(50 in numbers)
print(10 in numbers)

print(numbers)







