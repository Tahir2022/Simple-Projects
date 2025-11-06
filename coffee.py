#create class

class Coffee:
    def __init__(s, name, price):
        #initialize coffee name and price
        s.name, s.price = name, price

class CoffeeMachine:
    def __init__(s):
        #initialize menu and balance
        
        s.menu = [
            Coffee("Espresso", 2),
            Coffee("Cappuccino", 4),
            Coffee("Latte", 5)
        ]

        s.balance = 0

    #show available coffees

    def show_menu(s):
        print("\n---- Coffee Menu ---")

        for i, c in enumerate(s.menu, 1):
            print(f"{i}. {c.name} - €.{c.price}")

    #add money to machine

    def insert_money(s, amount):
        s.balance += amount
        print(f"Balance: €.{s.balance}")

    #buy selected coffee

    def buy_coffee(s, choice):
        if 1 <= choice <= len(s.menu):
            c = s.menu[choice - 1]
            if s.balance >= c.price:
                s.balance  -= c.price
                print(f"Enjoy you {c.name}!")
            else:
                print("Not enough balance.") 
        else:
            print("Invalid choice.")

    #return remaining balance

    def refund(s):
        print(f"Refunded: €.{s.balance}")
        s.balance = 0

    #main app loop

def main():
    m = CoffeeMachine()

    while True:
        print("\n1. Show Menu \n2. Insert Money \n3. Buy Coffee \n4. Refund \n5. Exit")

        ch = input("Choose option: ")
        if ch == "1":
            m.show_menu()
        elif ch == "2":
            m.insert_money(int(input("Enter amount: ")))
        elif ch == "3":
            m.show_menu()
            m.buy_coffee(int(input("Select Coffee: ")))
        elif ch == "4":
            m.refund()
        elif ch == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()