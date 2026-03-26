# Binance Trading Bot

A simplified trading bot built in Python for the **Binance Futures Testnet (USDT-M)**.  
This bot supports placing **MARKET** and **LIMIT** orders on both **BUY** and **SELL** sides, with proper logging, error handling, and a clean project structure.

---

## Features
- Place **MARKET** and **LIMIT** orders
- Support for **BUY** and **SELL** sides
- CLI interface with argument validation
- Structured code (client layer, order logic, CLI layer)
- Logging of API requests, responses, and errors to `bot.log`
- Exception handling for invalid input, API errors, and network failures

---

## Project Structure
trading_bot/
│
├── bot/
│   ├── client.py          # Binance client wrapper
│   ├── orders.py          # Order placement logic
│   ├── logging_config.py  # Logging setup
│   └── init.py
│
├── cli.py                 # CLI entry point
├── requirements.txt       # Dependencies
├── README.md              # Documentation
├── .env.example           # Environment variable template
└── bot.log                # Log file (sample MARKET + LIMIT orders)


---

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd trading_bot

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt

3. **Configure environment variables:**
Copy .env.example to .env
Add your Binance Testnet API key and secret:

##  **Usage**
Run commands from the project root:

1. Place a MARKET BUY order:
python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.01

2. Place a LIMIT SELL order:
python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.01 --price 67000


## **Output Example**
The bot prints order details and logs them in bot.log:

Order placed: {'orderId': 12994418295, 'symbol': 'BTCUSDT', 'status': 'NEW',
'type': 'MARKET', 'side': 'BUY', 'executedQty': '0.010', 'avgPrice': '67000.00', ...}

## **Assumptions**
Using Binance Futures Testnet (https://testnet.binancefuture.com)

LIMIT orders may remain in NEW status until the market price reaches the limit

API keys must be set in .env

.env is ignored in Git; only .env.example is committed for reference

