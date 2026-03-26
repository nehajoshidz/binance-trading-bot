import logging
from bot.client import client

logger = logging.getLogger(__name__)

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        if order_type == "MARKET":
            response = client.futures_create_order(symbol=symbol, side=side, type="MARKET", quantity=quantity)
        elif order_type == "LIMIT":
            response = client.futures_create_order(symbol=symbol, side=side, type="LIMIT",
                                                   quantity=quantity, price=price, timeInForce="GTC")
        else:
            raise ValueError("Unsupported order type")

        logger.info(f"Order placed: {response}")
        return response
    except Exception as e:
        logger.error(f"Error placing order: {e}")
        raise
