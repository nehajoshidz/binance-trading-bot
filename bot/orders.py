from bot.client import client
from bot.logging_config import setup_logger

logger = setup_logger()

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )
        else:
            raise ValueError("Unsupported order type")

        logger.info(f"Order placed: {order}")
        return order
    except Exception as e:
        logger.error(f"Error placing order: {e}")
        return {"error": str(e)}
