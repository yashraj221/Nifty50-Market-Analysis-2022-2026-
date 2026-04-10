import pandas as pd
import numpy as np

df = pd.read_csv('Nifty50.csv', skiprows=3, header=None)

df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

#convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

#sort by date and reset index
df = df.sort_values("Date").reset_index(drop=True)

print(df.shape)
print(df.head())
print(df.isnull().sum())
print((df == 0).sum())




#Replace 0 with NaN that forward fill
df["Volume"] = df["Volume"].replace(0, np.nan)
df["Volume"] = df["Volume"].ffill()

#save the cleaned data
df.to_csv('Nifty50_cleaned.csv', index=False)
print("cleaned data saved")
print(df.shape)