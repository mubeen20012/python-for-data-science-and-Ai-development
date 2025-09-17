#Mini Project: Simple Address Book
def book():
    phone_book={
        1:{'name':'Ali','Number':923184762687},
        2:{'name':'Aliya','Number':923184662697},
        3:{'name':'Aliyan','Number':923184962657}
    }
    #Update phone number.
    phone_book[1]['Number']=923224717539
    print(phone_book[1]['name'])
    for id in phone_book:
       phone_book[id]['city']='Lahore'
    phone_book[1]['city']='Islamabad'
    phone_book[4]={'name':'amina','Number':923185962659,'city':'Rawalpindi'}
    #Delete a contact.
    del phone_book[3]
            
    #Print the full address book.      
    for id,info in phone_book.items():
        print(f"ID: {id},Name: {info['name']},Number: {info['Number']},City: {info['city']}")
#Search by name or id. 
    try:
            id=int(input("ID: ").strip())
            if id in phone_book:
                info=phone_book[id]
                print(f"ID: {id},Name: {info['name']},{info['Number']},City: {info['city']}")
            else:
                print(f"Id {id} not found.")
    except ValueError:
            print("Invalid Input, allow only integers.")     
book()