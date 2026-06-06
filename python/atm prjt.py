def check_balance(balance):
    print(f"\n[BALANCE] Your current balance is: ₹{balance:.2f}")

def print_history(history_list):
    print("\n--- Transaction History ---")
    
    if len(history_list) == 0:
        print("No transactions yet.")
    else:
        for transaction in history_list:
            print(transaction)
            
    print("---------------------------")

def deposit(balance, history_list):
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        
        if amount > 0:
            balance += amount
            print(f"Success! Deposited ₹{amount:.2f}")
            history_list.append(f"Deposited: +₹{amount:.2f}")
        else:
            print("Error: Amount must be greater than ₹0.")
            
    except ValueError:
        print("Error: Please enter a valid number.")
        
    return balance

def withdraw(balance, history_list):
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        
        if amount > balance:
            print("Error: Insufficient funds.")
        elif amount <= 0:
            print("Error: Amount must be greater than ₹0.")
        else:
            balance -= amount
            print(f"Success! Withdrew ₹{amount:.2f}")
            history_list.append(f"Withdrew: -₹{amount:.2f}")
            
    except ValueError:
        print("Error: Please enter a valid number.")
        
    return balance
def user_details(user=None):
    print("\n--- User Details ---")

    if user is None or not user:
        print("No user details found. Please enter your details:")
        name = input("Name: ")
        account = input("Account Number: ")
        IFSC = input("IFSC Number: ")
        user = {
            "name": name,
            "account": account,
            "IFSC": IFSC,
        }
        print("\nUser details saved.")
    else:
        print("Current user details:")
        for k, v in user.items():
            print(f"{k.title()}: {v}")

        update = input("Would you like to update details? (y/n): ").strip().lower()
        if update == 'y':
            name = input(f"Name [{user.get('name','')}]: ") or user.get('name','')
            account = input(f"Account Number [{user.get('account','')}]: ") or user.get('account','')
            IFSC = input(f"IFSC Number [{user.get('IFSC','')}]: ") or user.get('IFSC','')
            user.update({"name": name, "account": account, "IFSC": IFSC})
            print("\nUser details updated.")

    return user
    
def atm_program():
    my_balance = 1000.00
    my_history = []
    my_user = {}
    is_running = True

    print("Welcome to Python Bank ATM")

    while is_running:
        print("\nPlease choose an option:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View History")
        print("5. User details")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            check_balance(my_balance)
            
        elif choice == '2':
            my_balance = deposit(my_balance, my_history)
            
        elif choice == '3':
            my_balance = withdraw(my_balance, my_history)
            
        elif choice == '4':
            print_history(my_history)

        elif choice == '5':
            my_user = user_details(my_user)
        elif choice == '6':
            print("Thank you for banking with us. Goodbye!")
            is_running = False 
            
        else:
            print("Invalid choice. Please try again.")

# --- 4. START THE PROGRAM ---
if __name__ == "__main__":
    atm_program()