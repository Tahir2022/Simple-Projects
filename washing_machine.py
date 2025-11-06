# creating class for washing machine

class WashingMachine:
    
    def __init__(s):
        #default settings

        s.mode = "Normal"
        s.timer = 30
        s.water = "Medium"
        s.spin = "Normal"
        s.running = False

    #start washing

    def start(s):
        if not s.running:
            s.running = True
            print("Washing started.")
        else:
            print("Already running!")

    # stop washing

    def stop(s):
        if s.running:
            s.running = False
            print("Washing stopped.")
        else:
            print("Machine not running!")

    #setting mode

    def set_mode(s):
        s.mode = input("Please enter mode (Normal/Quick/Heavy): ")
        print(f"Mode set to {s.mode}")

    # set timer

    def set_timer(s):
        s.timer = int(input("Enter timer (mins): "))
        print(f"Timer set to {s.timer}")

    #set water level

    def set_water(s):
        s.water = input("Enter water (Low/Medium/High): ")
        print(f"Water set to {s.water}")


    #set spin speed

    def set_spin(s):
        s.spin = input("Enter spin (Low/Medium/High): ")
        print(f"Spin set to {s.spin}")

    #show status

    def status(s):
        print("\n---Machine Status---")
        print(f"Running: {s.running}")
        print(f"Mode: {s.mode}")
        print(f"Timer: {s.timer}")
        print(f"Water: {s.water}")
        print(f"Spin: {s.spin}")
        print("------------------------")

    #main 

def main():
    wm = WashingMachine()

    while True:
        print("\n1. Start")
        print("2. Stop")
        print("3. Set Mode")
        print("4. Set Timer")
        print("5. Set Water")
        print("6. Set Spin")
        print("7. Show Status")
        print("8. Exit")

        ch = input("Choose: ")
        if ch == "1":
            wm.start()
        elif ch == "2":
            wm.stop()
        elif ch == "3":
            wm.set_mode()
        elif ch == "4":
            wm.set_timer()
        elif ch == "5":
            wm.set_water()
        elif ch == "6":
            wm.set_spin()
        elif ch == "7":
            wm.status()
        elif ch == "8":
            print("Exiting....")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()