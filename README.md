# 📈 General Crypto Market Tracker

A full-stack data engineering tool that tracks real-time prices of multiple cryptocurrencies, builds a historical dataset, and performs statistical analysis.

## 🚀 Overview
I built this tool to automate the collection of financial data. Instead of relying on manual checks, this bot acts as a **24/7 Market Monitor**. It fetches live data for Bitcoin, Ethereum, Solana, and Dogecoin from the CoinGecko API, cleans the data using Pandas, and visualizes market trends.

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Core Concepts:** Object-Oriented Programming (OOP), API Integration, Data Persistence
* **Libraries:**
    * `pandas` (Data Analysis & Cleaning)
    * `requests` (HTTP Requests / API calls)
    * `matplotlib` (Data Visualization)
    * `pathlib` (Modern File System Handling)

## ⚙️ How It Works
The project is split into three modular components:
1.  **The Tracker (`crypto_bot.py`):** Uses a `CryptoManager` class to fetch prices for all coins in a single CoinGecko API call. It handles network errors and appends data to a self-healing CSV database every 60 seconds.
2.  **The Analyzer (`analyze_data.py`):** Reads the raw CSV, filters out failed requests (zeros), and calculates statistical metrics (Mean, Max, Min).
3.  **The Visualizer (`vissualize_data.py`):** Generates time-series graphs for all tracked coins to visually identify market trends.

## 💻 Usage

### 1. Install Dependencies
```bash
pip install pandas requests matplotlib
```

### 2. Start the Tracker

Run the bot in the background to start collecting data.

```bash
python crypto_bot.py
```

Output: Fetches prices every 60 seconds and saves to `general_cryptocurrency.csv`.

### 3. Analyze the Data

Once you have collected some data, run the analysis script to see the report.

```bash
python analyze_data.py
```

### 4. Visualize the Data

```bash
python vissualize_data.py
```

## 📊 Sample Output
```
--- 📈 Market Statistics ---
          Bitcoin     Ethereum     Solana    Dogecoin
count    50.000000    50.000000   50.000000   50.000000
mean  $95,120.45   $2,740.10     $145.20      $0.1200
max   $95,200.00   $2,750.00     $146.00      $0.1250
```

## 🔮 Future Improvements
- [ ] Deploy to a cloud server (DigitalOcean) for 24/7 uptime.
- [ ] Add email/SMS alerts when price drops by 5%.
- [ ] Expand coin list with more altcoins.
