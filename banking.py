#create class

class BankAccount:

    #initialize account with pin and history

    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.history = []

    #deposit money

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited ${amount}")
        print(f"${amount} deposited! New balance: ${self.balance}")

    #withdraw money

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdraw ${amount}")
            print(f"${amount} withdrawn! New balance: ${self.balance}")

        else:
            print("Insufficient balance!")
    
    #show balance

    def show_balance(self):
        print(f"Account Holder: {self.name}, Balance: ${self.balance}")

    #show transaction history

    def show_history(self):
        print("\n--- Transaction History ---")
        for t in self.history:
            if self.history:
                print(t)
            else:
                print("No transaction yet!")

#main program

name = input("Enter your name: ")
pin = input("Set a 4 - digit PIN: ")

account = BankAccount(name, pin)

#ask for pin before access

if input("Enter PIN to login: ") != account.pin:
    print("Wrong PIN! Access Denied.")
    exit()

while True:
    print("\n1.Deposit 2.Withdraw 3.Show Balance 4.History 5.Exit")

    ch = input("Enter your choice: ")
    if ch == "1":
        account.deposit(int(input("Enter amount: ")))
    elif ch == "2":
        account.withdraw(int(input("Enter amount to withdraw: ")))
    elif ch == "3":
        account.show_balance()
    elif ch == "4":
        account.show_history()
    elif ch == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")