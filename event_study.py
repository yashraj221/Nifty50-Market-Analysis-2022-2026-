import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Nifty50_cleaned.csv", parse_dates=["Date"])
df["Daily_Return"] = df["Close"].pct_change()

# Define macro events
events = {
    "Russia-Ukraine War" : "2022-02-24",
    "RBI Rate Hike" : "2022-05-04",
    "US Fed Rate Hike" : "2022-06-15",
    "Adani Crisis" : "2023-01-25",
    "Election Results" : "2024-06-04"
}

# Convert to datetime
events = {k: pd.to_datetime(v) for k, v in events.items()}

print("Event loaded: ")
for name, date in events.items():
    print(f" {name}: {date.date()}")


# Expected return = average daily return over entire period 
expected_return = df["Daily_Return"].mean()
print(f"Expected daily return: {expected_return:.6f}")

# Event window = 5 days before and after each event
window = 5
results = {}

for event_name, event_date in events.items():
    # Get index of event date (find closest trading day)
    idx = df["Date"].searchsorted(event_date)

    # Make sure window doesn't go out of bounds
    if idx < window or idx + window >= len(df):
        continue

    # Slice the event window
    window_df = df.iloc[idx - window: idx + window + 1].copy()
    window_df["Abnormal_Return"] = window_df["Daily_Return"] - expected_return
    window_df["CAR"] = window_df["Abnormal_Return"].cumsum()
    window_df["Day"] = range(-window, window + 1)

    results[event_name] = window_df
    print(f"\n{event_name}: ")
    print(window_df[["Date", "Daily_Return", "Abnormal_Return", "CAR"]].to_string(index=False))


fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes = axes.flatten()

for i, (event_name, window_df) in enumerate(results.items()):
    ax = axes[i]
    ax.plot(window_df["Day"], window_df["CAR"] * 100, 
            color="navy", linewidth=2, marker="o", markersize=4)
    ax.axvline(0, color="red", linestyle="--", linewidth=1.5, label="Event Day")
    ax.axhline(0, color="gray", linestyle="--", linewidth=0.8)
    ax.set_title(event_name, fontsize=10, fontweight="bold")
    ax.set_xlabel("Days Relative to Event")
    ax.set_ylabel("CAR (%)")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)


# Hide the 6th subplot (empty)
axes[5].set_visible(False)

plt.suptitle("Cumulative Abnormal Returns Around Major Events - Nifty50", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("event_study.png")
plt.show()