import time

#create class

class Oven:
    def __init__(self):
        self.on = False
        self.temp = 0
        self.timer = 0
        self.ready = False

    #Turn on oven

    def turn_on(self):
        self.on = True
        print("Oven on.")

    #Turn off oven

    def turn_off(self):
        self.on = False
        self.temp = 0
        self.timer = 0
        self.ready = False
        print("Oven off.")

    #Set temperature

    def set_temp(self, t):
        if self.on:
            self.temp = t
        else:
            print("Turn on first.")

    #Preheat oven

    def preheat(self):
        if self.on and self.temp > 0:
            print(f"Preheating to {self.temp}°C...")
            time.sleep(1)
            self.ready = True
            print("Oven preheated.")
        else:
            print("Set temperature and turn on first.")

    #Set timer

    def set_timer(self, m):
        if self.on:
            self.timer = m
            print(f"Timer set to {m} min.")
        else:
            print("Turn on first.")

    #Bake item

    def bake(self, item):
        if not self.on:
            print("Turn on first.")
            return
        if not self.ready:
            print("Preheat first.")
            return
        if self.timer <= 0:
            print("Set timer first.")
            return
        print(f"Baking {item} for {self.timer} min.")
        for i in range(self.timer):
            print(f"{i+1} min passed...")
            time.sleep(1)
        print(f"{item} ready!")

    #Show status

    def status(self):
        print("\n --- Oven Status ---")
        print(f"On: {self.on}")
        print(f"Temperature: {self.temp}")
        print(f"Timer: {self.timer}")
        print(f"Preheated: {self.ready}")

def menu():
    ov = Oven()

    while True:
        print("\n1.ON \n2.OFF \n3.Temp \n4.Preheat \n5.Timer \n6.Bake \n7.Status \n8.Exit")

        c = input("Choose: ")
        if c == "1":
            ov.turn_on()
        elif c == "2":
            ov.turn_off()
        elif c == "3":
            ov.set_temp(int(input("Temperature: ")))
        elif c == "4":
            ov.preheat()
        elif c == "5":
            ov.set_timer(int(input("Minutes: ")))
        elif c == "6":
            ov.bake(input("Item: "))
        elif c == "7":
            ov.status()
        elif c == "8":
            break
        else:
            print("Invalid choice.")

#menu() --- Always runs, even when imported
if __name__ == "__main__":
    menu()
#if you wrap with if __name__ == "__main__" runs only directly