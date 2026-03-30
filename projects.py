#menu of services:
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
        deposit= int(input("enter the amount to deposit:"))
        if balance_enquiry <= 0:
            print("invalid amount")
        else:
            balance_enquiry += deposit
        print(f"your new balance is {balance_enquiry}")
    elif choose_service == "3":
        withdraw= int(input("enter the amount to withdraw:"))
        if withdraw > balance_enquiry:
            print("insufficient funds")
        else:
            balance_enquiry -= withdraw
        print(f"your new balance is {balance_enquiry}")
    elif choose_service == "4":
        print("thank you for using our services")
        break
    else:
        print("invalid input")
        break

    with open("amount.txt", "w") as file:
        file.write(str(balance_enquiry))