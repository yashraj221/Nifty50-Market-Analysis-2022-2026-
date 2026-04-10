import pandas as pd 

df = pd.read_csv("Nifty50_cleaned.csv", parse_dates=["Date"])

#monthly averagae return
df["Daily_Return"] = df["Close"].pct_change()
monthly = df.groupby(df["Date"].dt.month)["Daily_Return"].mean()
print(monthly)

#monthly volatility (standard deviation of daily returns)
volatility = df.groupby(df["Date"].dt.month)["Daily_Return"].std()
print(volatility)

#volume vs next day price movement 
df["Next_Day_Return"] = df["Daily_Return"].shift(-1)
correlation = df["Volume"].corr(df["Next_Day_Return"])
print("Correlation between volume and next day Return:", correlation)
