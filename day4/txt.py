#Text Files (TXT)
#Practice:
#Write "Hello, Python!" into a file.
with open('file.txt','w') as file:
    file.write('Hello, Python')
#Append your name to the same file.
with open('file.txt','a') as file:
    file.write('\nMusfira')
#Read the file and print each line.   
with open('file.txt','r') as file:
    for line in file:
        print(line.strip())
