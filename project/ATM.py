def ATM():
    balance=0
    pincode=1234
    attempt=0
    while attempt <3:
        try:
            pin=int(input("Enter Pin: ").strip())
            if pin!= pincode:
                attempt +=1
                print(f"Invalid Pin code.\nAttempt Left: {3 - attempt}")
            else:
                print(f"PinCode {pin} is Valid.")
                break
        except ValueError:
            print("Invalid Input, allow only integers.")
    if attempt == 3:
        print("Account Locked.")
    while True:
        print("\n--Menu--\n")
        print("1.Deposit")
        print("2.Withdraw")  
        print("3.Check Balance") 
        print("4.Exit")
        try:
            choice=int(input("Option: ").strip())
            if choice==1:
                try:
                  deposit=int(input("Deposit Money: ").strip())
                  balance += deposit
                  print(f"The amount {deposit} has been deposited.")
                  print(f"Balance: {balance}")
                except ValueError:
                    print("Invalid Input, allow only integers.")
            elif choice==2:
                try:
                    withdraw=int(input("Enter Money to withdraw: ").strip())
                    if withdraw >balance:
                        print(f"Withdraw money {withdraw} greater than balance, kindly recharge your account.")
                        print(f"Balance: {balance}")
                    else:
                        balance -= withdraw
                        print(f"Money {withdraw} has been withdrawn.")
                        print(f"Balance: {balance}")
                except ValueError:
                    print("Invalid Input, allow only integers.")
            elif choice==3:
                print(f"Balance: {balance}")
            elif choice==4:
                print("Thank You\nExiting------")
                break
            else:
                print("Invalid Input, allow only integers.")
        except ValueError:
                    print("Invalid Input, allow only integers.")
ATM()


