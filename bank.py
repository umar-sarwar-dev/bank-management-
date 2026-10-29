class BankAccount:
    def __init__(self, account_holder, initial_deposit=0.0):
        self.account_holder = account_holder
        self.balance = initial_deposit
        print(f"Account successfully created for {self.account_holder} with initial balance: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            print("Invalid withdrawal amount.")

    def check_balance(self):
        print(f"Current Account Balance for {self.account_holder}: ${self.balance:.2f}")


def main():
    print("--- Welcome to Bank Management System ---")
    name = input("Enter account holder name: ")
    try:
        initial = float(input("Enter initial deposit amount ($): "))
    except ValueError:
        initial = 0.0
        print("Invalid input, starting with $0.00")

    account = BankAccount(name, initial)

    while True:
        print("\n--- Menu ---")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            try:
                amt = float(input("Enter amount to deposit: "))
                account.deposit(amt)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '2':
            try:
                amt = float(input("Enter amount to withdraw: "))
                account.withdraw(amt)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Thank you for using Bank Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please select between 1 to 4.")

if __name__ == "__main__":
    main()
