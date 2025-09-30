#Two-Sum Problem
"""def num():
    number=[2, 7, 11, 15]
    target=9
    for i in range(len(number)):
        for j in range(i+1,len(number)):
            if number[i] + number[j]== target:
                print(number[i] , number[j])
num()"""
#find Duplicate in List
"""dup=[]
number=[1,2,3,2,3,4]
for num in number:
    if num not in dup:
        dup.append(num)
print(dup)"""
dup=[]
number=[1,2,3,2,3,4]
for num in number:
    if num in dup:
      print(f"Duplicate Found: {num}")
    else:
       dup.append(num)
        