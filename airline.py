#create class

class AirlineApp:
    def __init__(s):
        #initialize flights and bookings

        s.flights = []
        s.bookings = []

    #adding method 

    def add_flight(s, num, dest, seats):
        s.flights.append({"num": num, "dest": dest, "seats": seats})

    #viewing method

    def view_flights(s):
        for f in s.flights:
            print(f"Flight {f['num']} {f['dest']} | Seats: {f['seats']}")

    #booking method

    def book(s, num, name):
        for f in s.flights:
            if f["num"] == num and f["seats"] > 0:
                f["seats"] -= 1
                s.bookings.append({"name": name, "flight": num})
                print(f"{name} booked on {num}")
                return
            print("Booking failed")

    def view_bookings(s):
        for b in s.bookings:
            print(f"{b['name']} Flight {b['flight']}")

#main menu

app = AirlineApp()

while True:
    print("\n1.Add Flight 2.View Flights 3.Book 4.View Bookings 5.Exit")

    ch = input("Enter choice: ")
    if ch == "1":
        app.add_flight(input("Flight No: "), input("Destination: "), int(input("Seats: ")))
    elif ch == "2":
        app.view_flights()
    elif ch == "3":
        app.book(input("Flight No: "), input("Name: "))
    elif ch == "4":
        app.view_bookings()
    elif ch == "5":
        break
    else:
        print("Invalid choice.")