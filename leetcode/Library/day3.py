"""def number():
    nums = [2,7,11,15]
    target=9
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+ nums[j]==target:
                print(nums[i],nums[j])
number()"""
#Find Duplicate in List
#Write a program to find any duplicate numbers in a list.
"""def duplicate():
    dup=[]
    number=[1,3,4,2,2]
    for num in number:
        if num in dup:
            print(num)
        else:
            dup.append(num)
duplicate()"""
"""def number():
    nums=[2,7,11,15]
    target=17
    for i in range (len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j]== target:
                print(nums[i],nums[j])
number()
"""
"""def duplicate():
    dup=[]
    number=[1,2,2,3,4,5]
    for num in number:
      if num in dup:
        print(num)
      else:
         dup.append(num)
duplicate()"""
#Count frequency of elements (dict)
"""def frequency():
    freq={}
    number=[1,2,2,3,4]
    for num in number:
        
        if num in freq:
            freq[num] +=1
        else:
            freq[num] =1
    print(freq)
frequency()"""
#Merge two dictionaries
name={"Name": 'Musfira'}
marks={'Marks': 78}
result= name | marks
print(result)
