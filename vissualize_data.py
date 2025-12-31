import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Load Data
file_path = Path(__file__).parent / "general_cryptocurrency.csv"
df = pd.read_csv(file_path)

# 2. Clean Data (Same logic as Analyzer)
clean_df = df[df['Bitcoin'] > 0].copy()
clean_df['Timestamp'] = pd.to_datetime(clean_df['Timestamp'])
clean_df.set_index('Timestamp', inplace=True)

# 3. The Visualization Setup
plt.figure(figsize=(10, 6)) # Size: 10 inches wide, 6 inches tall

# Plot Bitcoin
plt.plot(clean_df.index, clean_df['Bitcoin'], label='Bitcoin', color='orange', linewidth=2)

# Optional: Plot Ethereum on a secondary axis (since price difference is huge)
# If you want to see them together, we normalize them or just plot BTC for now.

# 4. Styling (Make it look professional)
plt.title("Live Bitcoin Price History", fontsize=16)
plt.xlabel("Time", fontsize=12)
plt.ylabel("Price (USD)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5) # Add a grid
plt.legend()

# 5. Show the Graph
print("Opening Graph...")
plt.show()