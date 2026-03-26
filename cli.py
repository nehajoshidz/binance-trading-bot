import argparse
import bot.logging_config   # initialize logging config
from bot.orders import place_order

parser = argparse.ArgumentParser()
parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
parser.add_argument("--order_type", required=True, choices=["MARKET", "LIMIT"])
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

response = place_order(args.symbol, args.side, args.order_type, args.quantity, args.price)
print("Order response:", response)
