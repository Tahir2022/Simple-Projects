#represent a tiny in memory stock market and user portfolio

class StockMarketApp:
    def __init__(self):
        self.prices = {"AAPL": 195.2, "GOOG": 2845.9, "TSLA": 242.5 }
        self.portfolio = Portfolio()

    #display the main command menu

    def menu(self):
        print("\n=== Mini Stock Market ===")
        print("\n1. View prices 2. Buy shares 3. Sell shares 4. View portfolio 5. Exit")

        #handle with user choices in loop

        def run(self):
            while True:
                self.menu()
                ch = input("Select option: ").strip()

                if ch == "1":
                    self.show_prices()
                elif ch == "2":
                    self.buy_flow()
                elif ch == "3":
                    self.sell_flow()
                elif ch == "4":
                    self.portfolio.show()
                elif ch == "5":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice.")
        
        #print current stock prices

    def show_prices(self):
        for sym, price in self.prices.items():
            print(f"{sym:<4} : ${price:.2f}")

    #guide user through buying