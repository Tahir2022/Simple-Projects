import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn-v0_8")
stocks = ["AAPL", "XPEV", "TSLA"]

data = yf.download(stocks, start="2020-01-01", end="2025-01-01")["Close"]

data.plot(figsize=(17,8), fontsize=18)
plt.title("Stock Prices", fontsize = 20)
plt.xlabel("Date", fontsize = 16)
plt.ylabel("Close Price (USD)", fontsize = 16)
plt.show()