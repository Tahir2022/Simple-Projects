#creating class

class Inventory:
    def __init__(self):
        self.items = {}

    #add new item or update quantity

    def add_item(self):
        name = input("Enter name of item: ")
        qty = int(input("Enter quantity of item: "))
        self.items[name] = self.items.get(name, 0) + qty
        print(f"{qty} of {name} added/updated.")

    #remove item from inventory

    def remove_item(self):
        name = input("Enter item name to remove: ")
        if name in self.items:
            del self.items[name]
            print(f"{name} removed.")
        else:
            print("Item not found.")

    #display all inventory items

    def show_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            for name, qty in self.items.items():
                print(f"{name}: {qty}")

    #search for an item

    def search_item(self):
        name = input("Enter item name to search: ")
        if name in self.items:
            print(f"{name} found with quantity: {self.items[name]}")
        else:
            print(f"{name} not found in inventory.")

#display menu and handle user choice

def menu():
    inv = Inventory()

    options = {
        '1': inv.add_item,
        '2': inv.remove_item,
        '3': inv.show_inventory,
        '4': inv.search_item,
        '5': exit
    }

    while True:
        print("\nInventory Menu:")
        print("1.Add Item")
        print("2.Remove Item")
        print("3.Show Inventory")
        print("4.Search Item")
        print("5.Exit")

        ch = input("Enter your choice: ")
        action = options.get(ch)

        if action:
            action()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()