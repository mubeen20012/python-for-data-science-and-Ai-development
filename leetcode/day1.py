#Reverse string
"""def reverse():
    words=input("Word: ").strip()
    reverse=''
    for word in words:
        reverse =word + reverse
    print(f"Reverse: {reverse}")
reverse()"""
"""def main():
    words=input("Word: ").strip()
    print(f"Reverse: {reversed(words)}")
def reversed(words):
    reversed=''
    for word in words:
        reversed=word+ reversed
    return reversed
main()"""
"""def reverse():
    words=input("Word: ").strip()
    reversed=words[::-1]
    print(f"Reversed: {reversed}")
reverse()"""
#palindrome check
"""def palindrome():
    word=input("Word: ").strip()
    reversed=word[::-1]
    if word== reversed:
        print(f"Word: {word} is Palindrome.")
    else:
        print(f"Word: {word} is not Palindrome.")
palindrome()"""
#FizzBuzz
"""def fizzbuzz():
    for number in range(1,100):
        if number %3==0 and number% 5==0:
            print("FizzBuzz") 
        elif number%3==0:
            print("Fizz") 
        elif number%5==0:
            print("Buzz")  
        else:
            print(number)
fizzbuzz()
"""
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
"""def prime():
    try:
        number=int(input("Number: ").strip())
        if number <2:
            print(f"{number} is not prime.")
            return
        for i in range(2,int(number *0.5)+1):
            if number%i==0:
               print(f"Number: {number} is not prime.")
               return
        print(f"Number: {number} is prime.")
    except ValueError:
        print("Invalid input, allow only integers.")
prime()"""
#Find max/min without max()
def max():
    list=[]
    for number in range(5):
        try:
            number=int(input("Enter Number: ").strip())
            list.append(number)
        except ValueError:
            print("Invalid input,allow only integers.")
    max=list[0]
    for num in list:
        if num >max:
            max=num
    max=list=second[0]
    for num in list:
        if num > max:
            second=max
            max=num
        elif num> second and num !=second:
            num=second
    min=list[0]
    for num in list:
        if num < min:
            min=num
    print(f"Minimum: {min}")
    print(f"Second Largest: {second}")
    print(f"Maximum: {max}")

max()








