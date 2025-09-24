#function
def main():
    try:
        mark=int(input("Marks: ").strip())
        result=marks(mark)
        print(f"Result: {result}")
    except ValueError:
        print("Invalid Input, allow only integers.")
    
def marks(mark):
    if mark >=90:
        return 'A+'
    else:
        return 'keep Try'
main()
