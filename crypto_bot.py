import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import csv
from pathlib import Path

class CryptoManager:
    def __init__(self):
        # 1. Configuration: Add any coin here!
        # Format: "Name": "URL"
        self.coins = {
            "Bitcoin": "https://coinmarketcap.com/currencies/bitcoin/",
            "Ethereum": "https://coinmarketcap.com/currencies/ethereum/",
            "Solana": "https://coinmarketcap.com/currencies/solana/",
            "Dogecoin": "https://coinmarketcap.com/currencies/dogecoin/"
        }
        
        # 2. The Shared Settings
        # The selector you found (works for most CMC pages)
        self.selector = '.sc-65e7f566-0.WXGwg.base-text' 
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # 3. The Central Database
        # __file__ is the address of the script itself
# .parent gets the folder the script is sitting in
        self.filepath = Path(__file__).parent / "general_cryptocurrency.csv"
        self.initialize_csv()

    def initialize_csv(self):
        """Creates the file with specific columns if it doesn't exist."""
        if not self.filepath.exists():
            with self.filepath.open('w', newline='') as f:
                writer = csv.writer(f)
                
                # Dynamic Headers: Timestamp + Every Key in our self.coins dictionary
                # Result: ['Timestamp', 'Bitcoin', 'Ethereum', 'Solana', 'Dogecoin']
                header_row = ["Timestamp"] + list(self.coins.keys())
                
                writer.writerow(header_row)
            print(f"Created new database: {self.filepath}")

    def get_single_price(self, url):
        """Fetches the price for one specific URL."""
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
             
            price_element = soup.select_one(self.selector)
            
            if price_element:
                # Cleanup: $95,123.45 -> 95123.45
                clean_price = price_element.text.replace('$', '').replace(',', '')
                return float(clean_price)
            else:
                return None
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return None

    def update_market(self):
        """Fetches ALL prices and writes ONE row to the CSV."""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Start the row with the timestamp
        current_row = [now]
        
        print(f"--- Scraping Round [{now}] ---")
        
        # Loop through every coin in our list
        for name, url in self.coins.items():
            price = self.get_single_price(url)
            
            if price:
                print(f"Found {name}: ${price}")
                current_row.append(price)
            else:
                print(f"Failed to find {name}")
                current_row.append(0) # Store 0 or "N/A" if failed
        
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
            # Wait 30 seconds (Tracking multiple coins takes more requests!)
            time.sleep(30) 
            
    except KeyboardInterrupt:
        print("\nTracker stopped.")