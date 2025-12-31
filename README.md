# 📈 General Crypto Market Tracker

A full-stack data engineering tool that tracks real-time prices of multiple cryptocurrencies, builds a historical dataset, and performs statistical analysis.

![Project Screenshot](put_your_screenshot_filename_here.png)
*(Optional: Drag and drop your screenshot into the repo and link it here)*

## 🚀 Overview
I built this tool to automate the collection of financial data. Instead of relying on manual checks, this bot acts as a **24/7 Market Monitor**. It scrapes live data for Bitcoin, Ethereum, Solana, and Dogecoin, cleans the data using Pandas, and visualizes market trends.

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Core Concepts:** Object-Oriented Programming (OOP), Web Scraping, Data Persistence
* **Libraries:**
    * `pandas` (Data Analysis & Cleaning)
    * `beautifulsoup4` (Web Scraping / HTML Parsing)
    * `requests` (HTTP Requests)
    * `matplotlib` (Data Visualization)
    * `pathlib` (Modern File System Handling)

## ⚙️ How It Works
The project is split into three modular components:
1.  **The Tracker (`general_tracker.py`):** Uses a robust `CryptoManager` class to scrape multiple URLs simultaneously. It handles network errors and appends data to a self-healing CSV database.
2.  **The Analyzer (`analyze_data.py`):** Reads the raw CSV, filters out failed requests (zeros), and calculates statistical metrics (Mean, Max, Min).
3.  **The Visualizer (`visualize_data.py`):** Generates a time-series graph to visually identify market trends.

## 💻 Usage

### 1. Install Dependencies
```bash
pip install pandas requests beautifulsoup4 matplotlib
2. Start the Tracker

Run the bot in the background to start collecting data.

Bash
python general_tracker.py
Output: Scrapes prices every 30 seconds and saves to general_cryptocurrency.csv.

3. Analyze the Data

Once you have collected some data, run the analysis script to see the report.

Bash
python analyze_data.py
📊 Sample Output
Plaintext
--- 📈 Market Statistics ---
          Bitcoin     Ethereum     Solana    Dogecoin
count    50.000000    50.000000   50.000000   50.000000
mean  $95,120.45   $2,740.10     $145.20      $0.1200
max   $95,200.00   $2,750.00     $146.00      $0.1250
🔮 Future Improvements
[ ] Deploy to a cloud server (DigitalOcean) for 24/7 uptime.

[ ] Integrate Binance API for millisecond-precision data.

[ ] Add email alerts when price drops by 5%.