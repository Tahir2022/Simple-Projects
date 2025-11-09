#represent a tiny in memory stock market and user portfolio
import yfinance as yf 
#import time


class StockMarketApp:
    def __init__(self):
        self.symbols = ["AAPL", "GOOG", "TSLA", "AMZN"]
        self.prices = {}
    
    def fetch_prices(self):
        print("--- Fetching live prices ---")
        for symbol in self.symbols:
            data = yf.Ticker(symbol)
            price = data.info["regularMarketPrice"]
            self.prices[symbol] = price
        print("Prices updated")

    def show_prices(self):
        print("\n--- Current Stock Prices ---")
        for symbol, price in self.prices.items():
            print(f"{symbol}: ${price}")
        print("------------------------")

    def run(self):
        self.fetch_prices()
        self.show_prices()

if __name__ == "__main__":
    app = StockMarketApp()
    app.run()