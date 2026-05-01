import argparse
from bot.client import BinanceClient
from bot.orders import OrderService
from bot.validators import validate_order

def main():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price,
        )

        client = BinanceClient().get_client()
        order_service = OrderService(client)

        result = order_service.place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price,
        )

        print("\n===== ORDER RESULT =====")
        for key, value in result.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
