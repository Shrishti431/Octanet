# ATM Machine Simulation in Python

class ATMSimulation:
    def __init__(self, pin, balance=0):
        """Initialize the ATM with a pin, a balance, and an empty transaction history."""
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def verify_pin(self):
        """Prompt the user to enter their PIN and verify it."""
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN!")
            return False

    def balance_inquiry(self):
        """Display the current balance."""
        print(f"Your current balance is: ${self.balance:.2f}")
        self.transaction_history.append("Balance inquiry")

    def cash_withdrawal(self, amount):
        """Withdraw a specified amount of cash if sufficient balance is available."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"You have successfully withdrawn ${amount:.2f}")
            self.transaction_history.append(f"Withdrawn: ${amount:.2f}")
        else:
            print("Insufficient balance!")

    def cash_deposit(self, amount):
        """Deposit a specified amount of cash into the account."""
        self.balance += amount
        print(f"You have successfully deposited ${amount:.2f}")
        self.transaction_history.append(f"Deposited: ${amount:.2f}")

    def change_pin(self):
        """Change the account PIN after verification."""
        old_pin = input("Enter your current PIN: ")
        if old_pin == self.pin:
            new_pin = input("Enter your new PIN: ")
            self.pin = new_pin
            print("Your PIN has been successfully changed.")
            self.transaction_history.append("PIN change")
        else:
            print("Incorrect current PIN!")

    def show_transaction_history(self):
        """Display the transaction history."""
        print("Transaction History:")
        if self.transaction_history:
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

def main():
    # Create an ATM object with a default PIN and balance
    atm = ATMSimulation(pin="1234", balance=1000.0)

    while True:
        print("\n--- ATM Menu ---")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            if atm.verify_pin():
                atm.balance_inquiry()
        elif choice == "2":
            if atm.verify_pin():
                amount = float(input("Enter the amount to withdraw: "))
                atm.cash_withdrawal(amount)
        elif choice == "3":
            if atm.verify_pin():
                amount = float(input("Enter the amount to deposit: "))
                atm.cash_deposit(amount)
        elif choice == "4":
            if atm.verify_pin():
                atm.change_pin()
        elif choice == "5":
            if atm.verify_pin():
                atm.show_transaction_history()
        elif choice == "6":
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
