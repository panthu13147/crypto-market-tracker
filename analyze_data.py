import pandas as pd
from pathlib import Path

# 1. Load the CSV file
# We use __file__ parent to make sure we find the CSV in the same folder
file_path = Path(__file__).parent / "general_cryptocurrency.csv"

# Check if file exists first
if not file_path.exists():
    print(f"❌ Error: Could not find {file_path.name}")
    print("Make sure you run general_tracker.py first!")
    exit()

print(f"📂 Loading data from: {file_path.name}...")
df = pd.read_csv(file_path)

# --- CLEANING PHASE ---

# 2. Filter out "Failed" rows
# Logic: If Bitcoin is 0, the scrape failed. We drop those rows.
clean_df = df[df['Bitcoin'] > 0].copy()

# 3. Fix the Timestamp
# Convert the text string to a real DateTime object
clean_df['Timestamp'] = pd.to_datetime(clean_df['Timestamp'])

# --- ANALYSIS PHASE ---

# 4. Basic Statistics (Max, Min, Average)
# We exclude the Timestamp column for the math part
stats = clean_df.drop(columns=['Timestamp']).describe()

# --- DISPLAY PHASE ---

print("\n" + "="*40)
print("📊 CRYPTO DATA REPORT")
print("="*40)

# Print the last 5 valid entries
print("\n--- Recent Valid Data (Last 5 Rows) ---")
print(clean_df.tail(5).to_string(index=False))

print("\n\n--- 📈 Market Statistics ---")
# Format the stats table to look like money
pd.options.display.float_format = '${:,.2f}'.format
print(stats)

print("\n" + "="*40)
print(f"✅ Analysis Complete. Total valid records: {len(clean_df)}")