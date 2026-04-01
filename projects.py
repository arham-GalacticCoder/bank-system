#menu of services:
# login system:
correct_username = "khalid"
correct_password = "arham123"
attempts = 0
logged_in = False
while attempts < 3:
    username = input("enter your username:")
    password = input("enter your password:")
    if username == correct_username and password == correct_password:
        print("login successful")
        logged_in = True
        break
    else:
        print("invalid username or password. please try again.")
        attempts += 1
if not logged_in:
        print("you have reached the maximum number of attempts. please try again later.")
        
else:
    try:
      with open("amount.txt", "r") as file:
        balance_enquiry = int(file.read())
    except:
      balance_enquiry = 0
    while True:
        print("1.balance enquiry")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")   

        choose_service = input("choose the service:")
        if choose_service == "1":
            print(f"your balance is {balance_enquiry}")
        elif choose_service == "2":
            try :
                deposit = int(input("enter the amount to deposit:"))
                if deposit <= 0:
                    print("invalid amount")
                else:
                    balance_enquiry += deposit
            except:
                print("invalid input")
            print(f"your new balance is {balance_enquiry}")
        elif choose_service == "3":
            try:
                withdraw = int(input("enter the amount to withdraw:"))
                if withdraw <= 0:
                    print("invalid amount")
                elif withdraw > balance_enquiry:
                    print("insufficient balance")
                else:
                    balance_enquiry -= withdraw
            except:
                print("invalid input")
            print(f"your new balance is {balance_enquiry}")
        elif choose_service == "4":
            print("thank you for using our services")
            break
        else:
            print("invalid input")
            break

        with open("amount.txt", "w") as file:
            file.write(str(balance_enquiry))
