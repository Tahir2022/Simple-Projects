#create class

class PaymentApp:
    def __init__(self):
        #initialize user balance to 0

        self.balance = 0
    
    #add money to balance

    def add_money(self, amount):
        self.balance += amount
        print(f"\u2705 Added ${amount}. New Balance: ${self.balance}")

    #method to make 

    def make_payment(self, amount):
        if amount > self.balance:
            print("\u274C Insufficient balance!")
        else:
            self.balance -= amount
            print(f"\u2705 Paid ${amount}. Remaining Balance: ${self.balance}")

    #method to view current balance

    def view_balance(self):
        print(f"\U0001F4B0 Current Balance: ${self.balance}")

def main():
    app = PaymentApp()

    while True:
        print("\n--- Payment App Menu ---")
        print("\n1.Add Money 2.Make Payment 3.View Balance 4.Exit")

        ch = input("Choose an option: ")
        if ch == "1":
            amount = float(input("Enter amount to add: "))
            app.add_money(amount)
        elif ch == "2":
            amount = float(input("Enter amount to pay: "))
            app.make_payment(amount)
        elif ch == "3":
            app.view_balance()
        elif ch == "4":
            print("\U0001F44B Exiting the App. Goodbye!")
            break
        else:
            print("\u274C Invalid choice. Try again.")

if __name__ == "__main__":
    main()