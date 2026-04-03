#menu of services:

def login():
    correct_username = "khalid"
    correct_password = "arham123"
    attempts = 0
    while attempts < 3:
        username = input("enter your username:")
        password = input("enter your password:")
        if username == correct_username and password == correct_password:
            print("login successful")
            return True
        else:
            print("invalid username or password. please try again.")
            attempts += 1
    print("you have reached the maximum number of attempts. please try again later.")
    return False

def load_balance():
    try:
        with open("amount.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0
    except (ValueError, IOError) as e:
        print(f"Error loading balance: {e}")
        return 0

def save_balance(balance):
    try:
        with open("amount.txt", "w") as file:
            file.write(str(balance))
    except IOError as e:
        print(f"Error saving balance: {e}")

def deposit(balance_enquiry, history, *args):
    for amount in args:
        try:
            amount = int(amount)
            if amount <= 0:
                print(f"invalid amount: {amount}")
            else:
                balance_enquiry += amount
                history.append(f"Deposited: {amount}")
                print(f"Deposited: {amount}")
        except ValueError:
            print(f"invalid input: {amount}")
    print(f"your new balance is {balance_enquiry}")
    return balance_enquiry

def withdraw(balance_enquiry, history):
    try:
        amount = int(input("enter the amount to withdraw:"))
        if amount <= 0:
            print("invalid amount")
        elif amount > balance_enquiry:
            print("insufficient balance")
        else:
            balance_enquiry -= amount
            history.append(f"Withdrew: {amount}")
            print(f"your new balance is {balance_enquiry}")
    except ValueError:
        print("invalid input")
    return balance_enquiry

def show_history(history):
    print("\n--- Transaction History ---")
    if not history:
        print("No transactions yet.")
    for entry in history:
        print(entry)

def show_user_details(**kwargs):
    print("\n--- User Details ---")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def main():
    if not login():
        return

    balance_enquiry = load_balance()
    transaction_history = []
    # Store user details using **kwargs
    user_info = {"name": "Khalid", "account_type": "Savings", "currency": "USD"}
    
    while True:
        print("\n--- Menu ---")
        print("1.balance enquiry")
        print("2.deposit")
        print("3.withdraw")
        print("4.transaction history")
        print("5.exit")   

        try:
            choose_service = input("choose the service:")
            
            if choose_service == "1":
                show_user_details(**user_info)
                print(f"your balance is {balance_enquiry}")
            elif choose_service == "2":
                amounts_input = input("enter amounts to deposit (separated by space): ").split()
                balance_enquiry = deposit(balance_enquiry, transaction_history, *amounts_input)
                save_balance(balance_enquiry)
            elif choose_service == "3":
                balance_enquiry = withdraw(balance_enquiry, transaction_history)
                save_balance(balance_enquiry)
            elif choose_service == "4":
                show_history(transaction_history)
            elif choose_service == "5":
                print("thank you for using our services")
                break
            else:
                print("invalid input")
                continue
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    save_balance(balance_enquiry)
main()
print("-----------------------------------")
print("THANKS FOR USING OUR SERVICES")
print("-----------------------------------")
print("HAVE A NICE DAY")