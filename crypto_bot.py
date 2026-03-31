import requests
from datetime import datetime
import time
import csv
from pathlib import Path

# CoinGecko API coin IDs mapped to display names
COIN_IDS = {
    "Bitcoin": "bitcoin",
    "Ethereum": "ethereum",
    "Solana": "solana",
    "Dogecoin": "dogecoin",
}

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"

class CryptoManager:
    def __init__(self):
        # 1. Configuration: Add any coin here!
        # Format: "Display Name": "CoinGecko coin ID"
        self.coins = COIN_IDS

        # 2. The Central Database
        # __file__ is the address of the script itself
        # .parent gets the folder the script is sitting in
        self.filepath = Path(__file__).parent / "general_cryptocurrency.csv"
        self.initialize_csv()

    def initialize_csv(self):
        """Creates the file with header columns if it doesn't exist."""
        if not self.filepath.exists():
            with self.filepath.open('w', newline='') as f:
                writer = csv.writer(f)

                # Dynamic Headers: Timestamp + Every display name in self.coins
                # Result: ['Timestamp', 'Bitcoin', 'Ethereum', 'Solana', 'Dogecoin']
                header_row = ["Timestamp"] + list(self.coins.keys())

                writer.writerow(header_row)
            print(f"Created new database: {self.filepath}")

    def fetch_all_prices(self):
        """Fetches prices for all configured coins in a single API call."""
        try:
            coin_ids = ",".join(self.coins.values())
            response = requests.get(
                COINGECKO_API_URL,
                params={"ids": coin_ids, "vs_currencies": "usd"},
                timeout=10,
            )
            response.raise_for_status()
            data = response.json()
            # Map display names back to prices
            return {
                name: data.get(coin_id, {}).get("usd")
                for name, coin_id in self.coins.items()
            }
        except Exception as e:
            print(f"Error fetching prices from CoinGecko: {e}")
            return {name: None for name in self.coins}

    def update_market(self):
        """Fetches ALL prices and writes ONE row to the CSV."""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"--- Fetching Prices [{now}] ---")

        prices = self.fetch_all_prices()

        # Start the row with the timestamp
        current_row = [now]

        for name, price in prices.items():
            if price is not None:
                print(f"  {name}: ${price:,.4f}")
                current_row.append(price)
            else:
                print(f"  {name}: Failed to retrieve")
                current_row.append(0)  # Store 0 if failed

        # Write the full row to CSV
        with self.filepath.open('a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(current_row)

        print("Data saved successfully.\n")


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    manager = CryptoManager()

    print("Starting General Market Tracker...")
    print(f"Tracking: {list(manager.coins.keys())}")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            manager.update_market()
            # Wait 60 seconds between requests to stay within CoinGecko rate limits
            time.sleep(60)

    except KeyboardInterrupt:
        print("\nTracker stopped.")