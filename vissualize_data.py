import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Load Data
file_path = Path(__file__).parent / "general_cryptocurrency.csv"

# Check if file exists first
if not file_path.exists():
    print(f"❌ Error: Could not find {file_path.name}")
    print("Make sure you run crypto_bot.py first!")
    exit()

print(f"📂 Loading data from: {file_path.name}...")
df = pd.read_csv(file_path)

# 2. Clean Data (Same logic as Analyzer)
clean_df = df[df['Bitcoin'] > 0].copy()
clean_df['Timestamp'] = pd.to_datetime(clean_df['Timestamp'])
clean_df.set_index('Timestamp', inplace=True)

# Get all coin columns (everything except the index)
coin_columns = clean_df.columns.tolist()

# 3. The Visualization Setup
fig, axes = plt.subplots(len(coin_columns), 1, figsize=(12, 4 * len(coin_columns)), sharex=True)

# If there's only one coin, axes won't be a list
if len(coin_columns) == 1:
    axes = [axes]

color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

for ax, coin, color in zip(axes, coin_columns, color_cycle):
    ax.plot(clean_df.index, clean_df[coin], label=coin, color=color, linewidth=2)
    ax.set_title(f"{coin} Price History", fontsize=14)
    ax.set_ylabel("Price (USD)", fontsize=11)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()

plt.xlabel("Time", fontsize=12)
plt.tight_layout()

# 5. Show the Graph
print("Opening Graph...")
plt.show()