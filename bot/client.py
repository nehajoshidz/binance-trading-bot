from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

if not API_KEY or not API_SECRET:
    raise RuntimeError("BINANCE_API_KEY and BINANCE_API_SECRET must be set")

# Connect to Binance Futures Testnet using python-binance
client = Client(API_KEY, API_SECRET, testnet=True)
