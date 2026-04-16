def login():
    correct_username = "khalid"
    correct_password = "arham123"
    attempts = 0

    while attempts < 3:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == correct_username and password == correct_password:
            print("Login successful\n")
            return True
        else:
            print("Invalid username or password. Try again.")
            attempts += 1

    print("Maximum attempts reached. Try again later.")
    return False


# -------- LOAD BALANCE --------
def load_balance():
    try:
        with open("amount.txt", "r") as file:
            content = file.read().strip()
            return int(content) if content else 0
    except FileNotFoundError:
        # Create the file if it doesn't exist
        save_balance(0)
        return 0
    except ValueError:
        print("File data corrupted. Resetting balance to 0")
        return 0


# -------- SAVE BALANCE --------
def save_balance(balance):
    with open("amount.txt", "w") as file:
        file.write(str(balance))


# -------- DEPOSIT --------
def deposit(balance, history):
    try:
        amount = int(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount")
        else:
            balance += amount
            history.append(f"Deposited: {amount}")
            print(f"Deposited: {amount}")
    except ValueError:
        print("Invalid input")

    return balance


# -------- WITHDRAW --------
def withdraw(balance, history):
    try:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            history.append(f"Withdrew: {amount}")
            print(f"Withdrew: {amount}")
    except ValueError:
        print("Invalid input")

    return balance


# -------- SHOW HISTORY --------
def show_history(history):
    print("\n--- Transaction History ---")
    if not history:
        print("No transactions yet.")
        return
    for entry in history:
        print(entry)


# -------- MAIN PROGRAM --------
def main():
    if not login():
        return

    balance = load_balance()
    history = []

    while True:
        print("\n--- MENU ---")
        print("1. Balance enquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction history")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print(f"Your balance is: {balance}")
        elif choice == "2":
            balance = deposit(balance, history)
            save_balance(balance)

        elif choice == "3":
            balance = withdraw(balance, history)
            save_balance(balance)

        elif choice == "4":
            show_history(history)

        elif choice == "5":
            print("Thank you for using our service!")
            break

        else:
            print("Invalid choice.Please try again.")

    save_balance(balance)


# -------- RUN PROGRAM --------
if __name__ == "__main__":
    main()
    