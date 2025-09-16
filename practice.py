"""def numbers():
    for i in range(10):
        print(i)
numbers()"""
#Print even numbers between 1–50.
"""def even():
    for number in range(1,51):
        if number%2==0:
            print(number)
even()"""
#Print a multiplication table of 7.
"""def multiplication():
    table=int(input("Enter Table: ").strip())
    print(f"\nMultiplication Table of {table}: ")
    for i in range(1,11):
        print(f"{table} * {i} = {table * i}")
multiplication()"""
#Find the sum of numbers from 1–100.
"""def sum():
    sum=0
    for number in range(1,101):
        sum += number
    print(f"Sum of all number is {sum}")
sum()"""
#Reverse a string using a loop.
"""def reverse():
    name=input("Name: ").strip()
    reversed=''
    for char in name:
        reversed= char +reversed
    print(f"Reversed: {reversed}")
reverse()
"""
"""def reverse():
    name=input("Name: ").strip()
    reversed=name[::-1]
    print(f"Reversed: {reversed}")
    
reverse()"""
"""#6. Print a triangle pattern:
def triangle():
    star=int(input("Star: ").strip())
    for i in range(1,star +1):
         print(f"*" * i)
triangle()
"""
#Print multiplication tables from 2–5.
"""def multiplication():
    for i in range(2,6):
        print(f"\nMultiplication Table Of {i}:")
        for j in range(1,11):
            print(f"{i} * {j} = {i * j}")
multiplication()"""
#Count how many vowels are in a string using a loop.
"""def count():
    count=0
    sentence=input("Enter: ").strip()
    vowels='AEIOUaeiou'
    for char in sentence:
        if char in vowels:
            count +=1
    print(f"Vowel Count: {count}")
count()"""
#Write a program to check if a number is prime using loops.
"""def prime():
    number=int(input("Number: ").strip())
    if number <=1:
        print(f"{number} is not a prime")
        return
    for i in range(2,number):
        if number%i==0:
            print(f"{number} is not a prime")
            break
    else:
        print(f"{number} is a prime")
prime()"""
#Print the factorial of a number using a loop.
"""def factorial():
    try:
        number=int(input("Number: ").strip())
        result=1
        for i in range(1,number+1):
            result *=i
        print(f"Factorial: {result}")
    except ValueError:
        print("Invalid Input, allow only integers.")
factorial()"""
#Print the fibonnaci of a number using a loop.
"""def fibonnaci():
    try:
        number=int(input("Number: ").strip())
        a,b=0,1
        for i in range(a,number+1):
            print(a, end='')
            a,b=b,a+b
    except ValueError:
        print("Invalid Input, allow only integers.")
fibonnaci() """ 
#11. Find the maximum number in a list without max().
"""def largest():
    numbers=[]
    for number in range(3):
        try:
            number=int(input("Number: ").strip())
            numbers.append(number)
        except ValueError:
            print("Invalid input, allow only integers.")
    largest=max(numbers)
    print(f"Largest: {largest}")
largest()"""
"""def largest():
    numbers=[]
    for number in range(3):
        try:
            number=int(input("Number: ").strip())
            numbers.append(number)
        except ValueError:
            print("Invalid input, allow only integers.")
    largest=numbers[0]
    for num in numbers:
        if num > largest:
            largest=num
    print(f"Largest: {largest}")
largest()"""
#12. Print all keys and values from a dictionary using a loop.
"""student = {
    "name": "Musfira",
    "age": 22,
    "city": "Lahore",
    "degree": "IT"
}
for key in student:
    print(key,student[key])"""
#13. Count the frequency of each word in a sentence.
"""def freq():
    freq={}
    sentence=input("Sentence: ").strip()
    for word in sentence:
        if word in freq:
          freq[word] +=1
        else:
          freq[word] =1
    print(f"Freq: {freq}")
freq()"""
#14. Create a new list with squares of numbers from 1–10.
"""def square():
    squares=[]
    for num in range(1,11):
        square=num **2
        squares.append(square)
    print(square)
square()"""
#15. Print only unique numbers from a list.
"""unique=[]

numbers = [2, 4, 2, 5, 7, 5, 8, 9, 8]
for num in numbers:
    if num not in unique:
      unique.append(num)
print(unique)"""
#16. Write a program to check if a string is a palindrome.
"""def palindrome():
    word=input("Enter word: ").strip()
    reverse=word[::-1]
    if word == reverse:
        print(f"Word {word} is Palindrome.")
    else:
        print(f"Word {word} is not  Palindrome.")

palindrome()"""
#17. Generate Fibonacci sequence up to 20 terms using loops.
"""def fibonnaci():
    try:
        number=int(input("Number: ").strip())
        a,b=0,1
        for i in range(number):
            print(a,end='')
            a,b=b,a+b
    except ValueError:
        print("Invalid Input, allow only integers.")
fibonnaci()"""
"""a,b=0,1
for i in range(20):
    print(a,end="")
    a,b=b,a+b"""
#18. Print numbers 1–50 but skip multiples of 3.
"""def numbers():
    for i in range(1,51):
        if i%3==0:
            continue
        print(i)
numbers()"""
#19. Loop through a nested list and flatten it into a single list.
"""nested_list = [[1, 2], [3, 4], [5, 6]]
flat=[]
for subtitle in nested_list:
    for items in subtitle:
        flat.append(items)
print(flat)"""




        






