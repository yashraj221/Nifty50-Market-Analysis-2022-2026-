import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Nifty50_cleaned.csv", parse_dates=["Date"])
df["Daily_Return"] = df["Close"].pct_change()
monthly = df.groupby(df["Date"].dt.month)["Daily_Return"].mean() * 100

plt.figure(figsize=(10, 5))
plt.bar(monthly.index, monthly.values, color="steelblue")
plt.title("Average Monthly Return - Nifty50 (2022 - 2026)")
plt.xlabel("Month")
plt.ylabel("Average Daily Return (%)")
plt.xticks(range(1, 13), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
plt.axhline(0, color="red", linestyle="--")
plt.tight_layout()
plt.savefig("monthly_return.png")
plt.show()


volatility = df.groupby(df["Date"].dt.month)["Daily_Return"].std() * 100
plt.figure(figsize=(10, 5))
plt.bar(volatility.index, volatility.values, color="tomato")
plt.title("Monthly Volatility - Nifty50 (2022 - 2026)")
plt.xlabel("Month")
plt.ylabel("Std Dev of Daily Returns (%)")
plt.xticks(range(1, 13), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
plt.tight_layout()
plt.savefig("monthly_volatility.png")
plt.show()


plt.figure(figsize=(12, 5))
plt.plot(df["Date"], df["Volume"], color="green", linewidth=0.8)
plt.title("Trading Volume Over Time - Nifty50 (2022 - 2026)")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.tight_layout()
plt.savefig("volume_over_time.png")
plt.show()


plt.figure(figsize=(12, 5))
plt.plot(df["Date"], df["Close"], color="navy", linewidth=1)
plt.title("Nifty50 Closing Price (2022 - 2026)")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.tight_layout()
plt.savefig("price_trend.png")
plt.show()


df["Rolling_Vol"] = df["Daily_Return"].rolling(window=30).std() * 100

plt.figure(figsize=(12, 5))
plt.plot(df["Date"], df["Rolling_Vol"], color="darkorange", linewidth=1)
plt.title("30-Day Rolling Volatility - Nifty50 (2022 - 2026)")
plt.xlabel("Date")
plt.ylabel("Volatility (%)")
plt.tight_layout()
plt.savefig("rolling_volatility.png")
plt.show()