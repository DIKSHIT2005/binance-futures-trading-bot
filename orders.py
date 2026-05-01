from bot.logging_config import logger

class OrderService:
    def __init__(self, client):
        self.client = client

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }

            if order_type == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"

            response = self.client.futures_create_order(**params)

            logger.info(f"Order placed: {response}")

            return {
                "status": "SUCCESS",
                "orderId": response.get("orderId"),
                "symbol": response.get("symbol"),
                "status_desc": response.get("status"),
                "executedQty": response.get("executedQty"),
                "avgPrice": response.get("avgPrice", "N/A"),
            }

        except Exception as e:
            logger.error(f"Order failed: {str(e)}")
            return {"status": "FAILED", "error": str(e)}
