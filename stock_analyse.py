import yfinance as yf
import matplotlib.pyplot as plt
import seaborn 

stock = ["AAPL", "XPEV", "TSLA"]

stocks = yf.download(stock, start="2020-01-01", end="today")
data = stocks.loc[:, "Close"].copy()

data.plot(figsize=(17,8), fontsize=18)
plt.style.use("seaborn-v0_8")
plt.show()